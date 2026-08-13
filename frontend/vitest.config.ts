import { defineConfig } from "vitest/config";
import react from "@vitejs/plugin-react";
import path from "path";

export default defineConfig({
  plugins: [react()],
  test: {
    environment: "jsdom",
    setupFiles: ["./vitest.setup.ts"],
    globals: true, // optional: lets you use `describe`/`it` without importing
  },
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./"), // match your tsconfig paths
    },
  },
});
