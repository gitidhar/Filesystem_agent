from playwright.sync_api import sync_playwright
# crawler setup and dismantle code. 

def activate_crawler(url, head_or_not):
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=head_or_not)
    return (p, browser)

def shutdown(crawler, browser):
    # include any manual shutdowns required
    browser.close()
    crawler.stop()
    

    



    
