import { test } from 'node:test';
import assert from 'node:assert/strict';
import { createExports } from './exports.mjs';

test('allowed scheduling executes export', () => {
  const exports = createExports(() => true);
  exports.schedule('member', 'doc-1');
  assert.equal(exports.execute(), 'export:doc-1');
});

test('unauthorized scheduling is denied', () => {
  const exports = createExports(() => false);
  assert.throws(() => exports.schedule('member', 'doc-1'), /DENIED/);
  assert.equal(exports.execute(), null);
});

test('revocation after scheduling denies execution', () => {
  let permitted = true;
  const exports = createExports(() => permitted);
  exports.schedule('member', 'doc-1');
  permitted = false;
  assert.throws(() => exports.execute(), /DENIED/);
});
