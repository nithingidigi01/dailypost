const puppeteer = require("puppeteer");
const path = require("path");

(async () => {
  const browser = await puppeteer.launch({
    args: ["--no-sandbox"]
  });

  const page = await browser.newPage();

  await page.goto("file://" + path.resolve(__dirname, "poster.html"));

  await page.setViewport({ width: 1080, height: 1080 });

  await new Promise(r => setTimeout(r, 2000));

  await page.screenshot({ path: "poster.png" });

  await browser.close();
})();
