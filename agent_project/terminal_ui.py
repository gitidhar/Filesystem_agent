from rich.console import Console
from rich.align import Align

console = Console()

def get_reply(user_message: str) -> str:
    """
    Replace this with your real backend / chatbot logic.
    """
    return f"{user_message}"

def user_interface():
    chat_history = []

    chat_history.append(
        Align(
            "Bot: Welcome! Type 'quit' or 'exit' to leave.",
            align="left",
            style="bold green"
        )
    )

    while True:
        console.clear()

        for message in chat_history:
            console.print(message)

        console.print("\n", end="")

        user_message = console.input("[bold cyan]Input:[/bold cyan] ")

        if user_message.strip().lower() in ("quit", "exit"):
            chat_history.append(
                Align("Bot: Goodbye!", align="left", style="bold green")
            )
            break

        chat_history.append(
            Align(f"You: {user_message}", align="right", style="bold magenta")
        )

        reply = get_reply(user_message)
        chat_history.append(
            Align(f"Bot: {reply}", align="left", style="bold green")
        )

    console.clear()
    for message in chat_history:
        console.print(message)
