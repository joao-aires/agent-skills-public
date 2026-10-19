#!/usr/bin/env node
// Optional existing Playwright dependency; never used by renderer or artifact.
const assert=require('node:assert/strict');
const path=require('node:path');
const {pathToFileURL}=require('node:url');
const {chromium}=require(require.resolve('playwright',{paths:[process.argv[3]||process.cwd()]}));
const file=path.resolve(process.argv[2]||'explorer.html');
async function main(){
  const browser=await chromium.launch({headless:true,...(process.env.PLAYWRIGHT_CHANNEL?{channel:process.env.PLAYWRIGHT_CHANNEL}:{})});
  try{
    const page=await browser.newPage();const errors=[];page.on('pageerror',e=>errors.push(e.message));
    await page.addInitScript(()=>{window.copied=null;Object.defineProperty(navigator,'clipboard',{configurable:true,value:{writeText:async value=>{window.copied=value;}}});});
    await page.goto(pathToFileURL(file).href);
    const model=await page.locator('#flow-model').evaluate(n=>JSON.parse(n.textContent));
    assert.equal(await page.title(),model.title,'dynamic title must be literal text');
    assert.equal(await page.locator('#title').textContent(),model.title);
    assert.equal(await page.locator('#title img, #payload script, #payload img').count(),0,'model data interpreted as HTML');
    assert.equal(await page.evaluate(()=>window.injected),undefined,'injected model script executed');
    assert.equal(await page.locator('#depth').inputValue(),model.exploration?.depth||'container','agent-selected starting level');
    for(const [id,value] of Object.entries(model.exploration?.overrides||{})){
      assert.equal(await page.locator(`select[data-depth-node="${id}"]`).inputValue(),value,'agent-selected local level');
    }
    const byId=new Map(model.messages.map(m=>[m.id,m]));
    const options=()=>page.locator('#picker option').evaluateAll(ns=>ns.map(n=>n.value));
    for(const flow of model.flows){
      await page.locator('#tab-'+flow.id).click();
      for(const depth of ['context','container','component']){
        if(!await page.locator('#reset-depth').isDisabled())await page.locator('#reset-depth').click();
        await page.locator('#depth').selectOption(depth);
        {
          const ids=await options();
          assert.deepEqual(ids.filter(id=>!byId.get(id).parentId),flow.messageIds,'outer interactions disappear or reorder');
          for(const id of ids){
            await page.locator('#picker').selectOption(id);
            const message=byId.get(id);assert.equal(await page.locator('#message-title').textContent(),message.label);
            await page.locator('#collapse').click();
            await page.locator('#copy').click();assert.deepEqual(JSON.parse(await page.evaluate(()=>window.copied)),message.payload,'copy must preserve complete JSON value after collapse');
            for(let sample=0;sample<(message.examples||[]).length;sample++){
              await page.locator('#payload-picker').selectOption(String(sample+1));await page.locator('#copy').click();
              assert.deepEqual(JSON.parse(await page.evaluate(()=>window.copied)),message.examples[sample].value,'example copy must preserve source value');
            }
            await page.locator('#payload-picker').selectOption('0');
            const text=await page.locator('#transport').textContent();
            if(message.transport.kind==='local'){assert.match(text,/No network endpoint/);assert.equal(await page.locator('#transport a').count(),0);}
            else{assert.ok(text.includes(message.transport.endpoint.status));assert.ok(text.includes(message.transport.direction));if(message.transport.endpoint.url===null)assert.match(text,/URL unresolved/);}
            for(const mode of ['c4','sequence']){await page.locator('#'+mode).click();assert.equal(await page.locator('#picker').inputValue(),id,'view switch changes selected identity');}
          }
          await page.locator('#c4').click();
          for(const node of model.nodes.filter(n=>n.external)){
            const drawn=page.locator(`[data-node-id="${node.id}"]`);
            if(await drawn.count()){
              assert.equal(await drawn.getAttribute('data-external'),'true');assert.equal(await drawn.getAttribute('data-owner'),node.parent||'');
              const bounds=await drawn.locator('rect').evaluate(r=>({x:+r.getAttribute('x'),y:+r.getAttribute('y'),w:+r.getAttribute('width'),h:+r.getAttribute('height')}));
              const internal=await page.locator('[data-boundary-id]').evaluateAll(rs=>rs.map(r=>({id:r.getAttribute('data-boundary-id'),x:+r.getAttribute('x'),y:+r.getAttribute('y'),w:+r.getAttribute('width'),h:+r.getAttribute('height')})));
              for(const boundary of internal.filter(b=>!model.nodes.find(n=>n.id===b.id).external)){
                assert.ok(!(bounds.x>=boundary.x&&bounds.x+bounds.w<=boundary.x+boundary.w&&bounds.y>=boundary.y&&bounds.y+bounds.h<=boundary.y+boundary.h),'external node drawn inside internal boundary');
              }
            }
          }
          for(const child of ids.filter(id=>byId.get(id).parentId)){
            await page.locator('#picker').selectOption(child);const parent=byId.get(child).parentId;
            assert.match(await page.locator('#message-status').textContent(),/MESSAGE \d+\.\d+ · PARENT \d+/,'child must use parent.child numbering');
            await page.locator('#depth').selectOption('context');assert.equal(await page.locator('#picker').inputValue(),parent,'child must map to parent');
            await page.locator('#depth').selectOption('component');assert.equal(await page.locator('#picker').inputValue(),child,'child selection must restore');
            await page.locator('#collapse').click();assert.equal(await page.locator('#payload details:not(.root)[open]').count(),0);
            await page.locator('#expand').click();assert.equal(await page.locator('#payload details:not([open])').count(),0);
          }
        }
      }
      await page.locator('#depth').selectOption('container');await page.locator('#picker').selectOption(flow.messageIds[0]);
      assert.equal(await page.locator('#previous').isDisabled(),true);
      if(flow.messageIds.length>1){await page.locator('#next').click();assert.equal(await page.locator('#picker').inputValue(),flow.messageIds[1]);await page.locator('#previous').click();assert.equal(await page.locator('#picker').inputValue(),flow.messageIds[0]);}
    }
    // Mixed depth: two independently expandable containers in the bundled fixture.
    await page.locator('[role=tab]').first().click();
    await page.locator('#depth').selectOption('container');
    const expandable=model.nodes.filter(n=>n.kind==='container'&&model.nodes.some(c=>c.parent===n.id));
    if(expandable.length>=2){
      const [a,b]=expandable;
      const childOf=id=>model.messages.find(m=>m.within===id&&model.flows[0].messageIds.includes(m.parentId));
      const childA=childOf(a.id),childB=childOf(b.id);
      await page.locator(`#diagram [data-depth-node="${a.id}"][data-depth-value="component"]`).first().focus();
      await page.keyboard.press('Enter');
      assert.ok((await options()).includes(childA.id));assert.ok(!(await options()).includes(childB.id));
      assert.equal(await page.locator(`#diagram [data-node-id="${b.id}"]`).count(),1,'neighbor stays summarized');
      await page.locator(`#diagram [data-depth-node="${b.id}"][data-depth-value="component"]`).first().click();
      assert.ok((await options()).includes(childA.id)&& (await options()).includes(childB.id),'both expansions coexist');
      await page.locator('#picker').selectOption(childA.id);
      await page.locator('#c4').click();assert.equal(await page.locator('#picker').inputValue(),childA.id);
      await page.locator(`#diagram [data-depth-node="${a.id}"][data-depth-value="container"]`).first().click();
      assert.equal(await page.locator('#picker').inputValue(),childA.parentId);
      assert.ok((await options()).includes(childB.id),'collapsing one container leaves the other expanded');
      await page.locator(`#diagram [data-depth-node="${a.id}"][data-depth-value="component"]`).first().click();
      assert.equal(await page.locator('#picker').inputValue(),childA.id,'local re-expansion restores selection');
      await page.locator('#local-depths summary').click();
      await page.locator(`select[data-depth-node="${a.parent}"]`).selectOption('context');
      assert.equal(await page.locator('#picker').inputValue(),childA.parentId,'system collapse maps child to root');
      assert.equal(await page.locator(`#diagram [data-node-id="${a.id}"]`).count(),0);
      assert.deepEqual((await options()).filter(id=>!byId.get(id).parentId),model.flows[0].messageIds);
      await page.locator(`select[data-depth-node="${a.parent}"]`).selectOption('container');
      assert.equal(await page.locator('#picker').inputValue(),childA.id,'system reopen restores child and saved container choices');
      await page.locator('#depth').selectOption('context');
      assert.equal(await page.locator('#picker').inputValue(),childA.id,'global level preserves overrides');
      await page.locator('#reset-depth').click();
      assert.equal(await page.locator('#picker').inputValue(),childA.parentId);
      assert.equal(await page.locator('#reset-depth').isDisabled(),true);
      await page.locator('#depth').selectOption('component');
      assert.ok((await options()).includes(childA.id)&& (await options()).includes(childB.id),'global component level expands all');
      await page.locator('#depth').selectOption('context');
      await page.locator('#picker').selectOption(model.flows[0].messageIds[0]);
      await page.locator('#depth').selectOption('component');
      assert.equal(await page.locator('#picker').inputValue(),model.flows[0].messageIds[0],'explicit selection cancels remembered child');
      await page.locator('#local-depths summary').click();
    }
    if(model.flows.length>1){await page.locator('[role=tab]').first().focus();await page.keyboard.press('ArrowRight');assert.equal(await page.locator('[role=tab][aria-selected=true]').getAttribute('id'),'tab-'+model.flows[1].id);}
    // Force clipboard failure: fallback remains a complete JSON string, not tree display text.
    await page.evaluate(()=>Object.defineProperty(navigator,'clipboard',{configurable:true,value:{writeText:async()=>{throw Error('unavailable');}}}));
    await page.locator('#copy').click();JSON.parse(await page.locator('#payload').textContent());assert.match(await page.locator('#copy-status').textContent(),/manual copy/);
    await page.setViewportSize({width:390,height:844});assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),true,'mobile page overflows');
    assert.deepEqual(errors,[],'browser runtime errors');
    if(process.env.SCREENSHOT)await page.screenshot({path:process.env.SCREENSHOT,fullPage:true});
    console.log(`BROWSER PASS: ${model.flows.length} scenarios; all views/depths, independent local expansion/reset, keyboard depth controls, parent identity, payload copy, transport, ownership, navigation, keyboard tabs, clipboard fallback, mobile layout; 0 page errors`);
  }finally{await browser.close();}
}
main().catch(error=>{console.error(error);process.exitCode=1;});
