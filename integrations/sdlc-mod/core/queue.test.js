import assert from "node:assert/strict";
import test from "node:test";
import { createQueue } from "./queue.js";

test("runs mutations in order", async () => {
  const enqueue = createQueue();
  const order = [];
  await Promise.all([
    enqueue(async () => {
      await new Promise((resolve) => setTimeout(resolve, 20));
      order.push(1);
    }),
    enqueue(async () => {
      order.push(2);
    }),
  ]);
  assert.deepEqual(order, [1, 2]);
});

test("keeps running after a failure", async () => {
  const enqueue = createQueue();
  await assert.rejects(enqueue(async () => {
    throw new Error("boom");
  }), /boom/);
  assert.equal(await enqueue(async () => "ok"), "ok");
});
