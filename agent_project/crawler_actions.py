from playwright.sync_api import Playwright, Browser, sync_playwright, expect
from crawler import activate_crawler, shutdown
import ffmpeg
import time


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
        print("Caught potential audio REQUEST =>", url)
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
    page.on("request", handle_request)
    page.on("response", handle_response)

    page.goto("https://soundcloud.com/")
    page.locator("#content").get_by_role("searchbox", name="Search").click()
    page.locator("#content").get_by_role("searchbox", name="Search").fill("dominic fike unreleased tracks")
    page.locator("#content").get_by_role("searchbox", name="Search").press("Enter")
    page.get_by_label("Playlist: Dominic Fike ~").get_by_role("button", name="Play").click()

    
    # page.get_by_role("button", name="Pause", exact=True).click()


