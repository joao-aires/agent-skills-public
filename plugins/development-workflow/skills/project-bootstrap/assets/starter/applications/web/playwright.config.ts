import { defineConfig } from "@playwright/test";
export default defineConfig({ testDir: "./tests/e2e", workers: 1, retries: 0,
  outputDir: "../../artifacts/e2e", reporter: [["list"], ["html", { outputFolder: "../../artifacts/report", open: "never" }]],
  use: { baseURL: "http://localhost:3000", trace: "retain-on-failure", screenshot: "only-on-failure" },
  webServer: [
    { command: "uv run --directory ../api uvicorn notes.main:app --app-dir src --host 127.0.0.1 --port 8000", url: "http://127.0.0.1:8000/api/health", reuseExistingServer: false, timeout: 60000 },
    { command: "pnpm start", url: "http://localhost:3000", reuseExistingServer: false, timeout: 60000 },
  ],
});
