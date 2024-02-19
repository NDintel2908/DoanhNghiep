async def cong_ty(url, df, linh_vuc, nganh_tieu_diem):
    url_cur = await url.evaluate("() => window.location.href")
    for n in range(1, 1000):
        checkexist = await url.querySelector(".page_active")
        if checkexist is None:
            break
        else:
            await url.goto(url_cur + f"?page={n}")
            print(f"{nganh_tieu_diem} --- Page: {n}")
            ds_cty = await url.querySelectorAll("h2 > a")
            ds_sdt = await url.querySelectorAll(".listing_dienthoai > a")
            ds_email = await url.querySelectorAll(".email_web_section > a:nth-child(1)")

            for cty, sdt, email in zip(ds_cty, ds_sdt, ds_email):
                cty1 = await cty.getProperty("textContent")
                sdt1 = await sdt.getProperty("textContent")
                email1 = await email.getProperty("href")
                new_row = {"Lĩnh vực": linh_vuc, "Ngành Tiêu Điểm": nganh_tieu_diem, "Công ty": await cty1.jsonValue(), "Sdt": await sdt1.jsonValue(), "Email": await email1.jsonValue()}
                df = df.append(new_row, ignore_index=True)
    return df

