/**
 * Serialize async mutations. A failed task does not poison the queue.
 */
export function createQueue() {
  let tail = Promise.resolve();
  return function enqueue(task) {
    const run = tail.then(task, task);
    tail = run.catch(() => {});
    return run;
  };
}
