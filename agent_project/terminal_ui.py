from rich.console import Console
from rich.align import Align
from crawler_actions import run
from playwright.sync_api import Browser
console = Console()

def process_a_reply(user_message: str, browser: Browser) -> list[str, bool]:
    outcome = run(browser, user_message)
    if outcome:
        return [f"fetched ya shit", True]
    return [f"i could not find that shit haha", False]

def user_interface(browser: Browser):
    chat_history = []

    chat_history.append(
        Align(
            "Bot: Welcome! Type 'quit' or 'exit' to leave.",
            align="left",
            style="bold green"
        )
    )

    while True:
        found = False
        console.clear()

        for message in chat_history:
            console.print(message)

        console.print("\n", end="")

        user_message = console.input("[bold cyan]Input:[/bold cyan] ")

        if user_message.strip().lower() in ("quit", "exit"):
            chat_history.append(
                Align("Bot: Goodbye!", align="left", style="bold magenta")
            )
            break

        chat_history.append(
            Align(f"You: {user_message}", align="right", style="bold white  ")
        )

        reply, found = process_a_reply(user_message, browser=browser)
        chat_history.append(
            Align(f"Bot: {reply}", align="left", style="bold green")  
        )
        if found:
            break

    console.clear()
    for message in chat_history:
        console.print(message)
