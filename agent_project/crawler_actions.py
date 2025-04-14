from playwright.sync_api import Playwright, Browser, sync_playwright, expect
from crawler import activate_crawler, shutdown
import ffmpeg
import time
import re


def convert_m3u8_to_mp3(input_m3u8_url, output_mp3_path):
    # command = [
    #     "ffmpeg",
    #     "-i", input_m3u8_url,
    #     "-c", "copy",
    #     output_mp3_path
    # ]
    # subprocess.run(command, check=True)
    (
        ffmpeg.input(input_m3u8_url).output(output_mp3_path, c="copy").run()
    )


def handle_request(request):
    url = request.url
    if "cf-hls-media.sndcdn.com" in url and "m3u" in url:
        print("Caught potential audio REQUEST")
        # convert_m3u8_to_mp3(url, "example_song.mp3")

def handle_response(response):
    url = response.url
    if "cf-hls-media.sndcdn.com" in url and "m3u" in url:
        print("Got audio RESPONSE =>", url)
        output_file = f"song_{int(time.time())}.mp3"
        convert_m3u8_to_mp3(url, output_file)

def run(browser: Browser) -> None:
    context = browser.new_context()
    page = context.new_page()
    
    page.goto("https://soundcloud.com/")
    page.locator("#content").get_by_role("searchbox", name="Search").click()
    page.locator("#content").get_by_role("searchbox", name="Search").fill("frank ocean unreleased tracks")
    page.locator("#content").get_by_role("searchbox", name="Search").press("Enter")
    
    found = False
    for scroll_attempt in range(20):
        # print(f"Scroll attempt {scroll_attempt + 1}")
        link = page.locator("a").filter(has_text=re.compile("trouble", re.IGNORECASE))
        
        try:
            if link.count() > 0:
                link.first.click()
                found = True
                break
        except Exception as e:
            print("Error checking link:", e)

        page.evaluate("window.scrollBy(0, document.body.scrollHeight / 2)")
        time.sleep(1)

    if not found:
        return

    page.on("request", handle_request)
    page.on("response", handle_response)
    
    time.sleep(2)
    page.get_by_role("button", name="Play", exact=True).click()
    time.sleep(2)
