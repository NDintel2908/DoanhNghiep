import asyncio
from pyppeteer import launch
from nganhnghe import nganh_nghe
import pandas as pd


async def main():
    global url, df
    df = pd.DataFrame({"Lĩnh vực": [], "Ngành Tiêu Điểm": [], "Công ty": [], "Sdt": [], "Email": []})
    browser = await launch(headless=True,
                           executablePath='C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe')
    url = await browser.newPage()
    await url.goto('https://trangvangvietnam.com/')

    for i in range(1, 50):
        await url.goto('https://trangvangvietnam.com/')
        link = await url.querySelector(f"body > div.mt-5.mb-5 > div > div:nth-child(3) > div:nth-child({i}) > div > a")
        if link is not None:
            linh_vuc = await (await link.getProperty("textContent")).jsonValue()
            await link.click()
            await url.waitForNavigation()
            await nganh_nghe(url, df, linh_vuc)

    await browser.close()


asyncio.get_event_loop().run_until_complete(main())
