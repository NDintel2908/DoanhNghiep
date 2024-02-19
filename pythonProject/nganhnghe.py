from congty import cong_ty


async def nganh_nghe(url, df, linh_vuc):
    global df1, df2
    df2 = df1 = df
    sl_nganh_tieu_diem = await url.querySelectorAll(
        "body > div.m-auto.h-auto.pt-5 > div.container-xxl > div.div_list_cty > div:nth-child(2) > div > div .counter_number")
    print(f"Lĩnh vực: {linh_vuc} -------- Số lượng ngành tiêu điểm: {len(sl_nganh_tieu_diem)}")
    url_cur = await url.evaluate("() => window.location.href")
    for n in range(1, len(sl_nganh_tieu_diem) + 1):
        await url.goto(url_cur)
        link = await url.querySelector(
            f"body > div.m-auto.h-auto.pt-5 > div.container-xxl > div.div_list_cty > div:nth-child(2) > div > div > div:nth-child({n}) > a")
        if link is not None:
            nganh_tieu_diem = await (await link.getProperty("textContent")).jsonValue()
            print(f"Lĩnh vực: {linh_vuc} --------- Ngành tiêu điểm: {nganh_tieu_diem}")
            await link.click()
            await url.waitForNavigation()
            df1 = await cong_ty(url, df, linh_vuc, nganh_tieu_diem)
            df2 = df2.append(df1, ignore_index=True)
    df2.to_excel(f"D:\\{linh_vuc}.xlsx")
