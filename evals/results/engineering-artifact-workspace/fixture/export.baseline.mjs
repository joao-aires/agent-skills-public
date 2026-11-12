export function createExports(canRead) {
  const pending = [];
  return {
    schedule(user, document) {
      if (!canRead(user, document)) throw new Error('DENIED');
      pending.push({ user, document });
      return pending.length;
    },
    execute() {
      const job = pending.shift();
      if (!job) return null;
      return `export:${job.document}`;
    },
  };
}
