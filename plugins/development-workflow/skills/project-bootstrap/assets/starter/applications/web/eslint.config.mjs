import { fixupConfigRules } from "@eslint/compat";
import { defineConfig, globalIgnores } from "eslint/config";
import nextVitals from "eslint-config-next/core-web-vitals";
import nextTypescript from "eslint-config-next/typescript";
export default defineConfig([...fixupConfigRules(nextVitals), ...fixupConfigRules(nextTypescript), globalIgnores([".next/**", "src/lib/api-schema.d.ts", "next-env.d.ts"])]);
