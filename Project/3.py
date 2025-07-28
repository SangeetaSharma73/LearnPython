


from playwright.sync_api import sync_playwright
import pandas as pd

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    # Better wait strategy and timeout
    page.goto(
        "https://sourcing.alibaba.com/rfq/rfq_search_list.htm?country=AE&recently=Y",
        wait_until="domcontentloaded",
        timeout=60000
    )
    page.wait_for_timeout(15000)  # Wait 15 seconds more just in case

    # Screenshot for confirmation
    page.screenshot(path="page_debug.png", full_page=True)

    rfqs = page.locator("div.brh-rfq-item__main-info h1 a")
    print(f"Found {rfqs.count()} RFQs")

    data = []
    for i in range(rfqs.count()):
        title = rfqs.nth(i).inner_text()
        link = rfqs.nth(i).get_attribute("href")

        data.append({
            "Title": title.strip(),
            "Link": "https:" + link if link.startswith("//") else link
        })
    
    browser.close()

    df = pd.DataFrame(data)
    df.to_csv("alibaba_rfq_data.csv", index=False)
    print("Saved to alibaba_rfq_data.csv!")

