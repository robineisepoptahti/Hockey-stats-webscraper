import { test, expect } from "@playwright/test";

const baseUrl = "http://127.0.0.1:5173/";

test("should display the home page", async ({ page }) => {
  await page.goto(baseUrl);
  await expect(page).toHaveTitle(/frontend/);
});
