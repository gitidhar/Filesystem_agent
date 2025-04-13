from playwright.sync_api import sync_playwright


def activate_crawler(url, head_or_not):
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=head_or_not)
    context = browser.new_context()
    page = context.new_page()
    page.goto(url)

    return (p, browser)

def shutdown(crawler, browser):
    # include any manual shutdowns required
    browser.close()
    crawler.stop()
    

    



    
