import json
import os
from datetime import datetime
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

MODEL = "gemini-2.5-flash"
URL = "https://generativelanguage.googleapis.com/v1beta/models/" + MODEL + ":generateContent"
RESPONSES = {
    "hello": "Hello! How can I help?",
    "how are you": "I am doing great.",
    "what is your name": "I am Vozera AI.",
}


def clean_message(message):
    return message.lower().strip()


def ask_gemini(message, gemini_history, api_key):
    new_message = {"role": "user", "parts": [{"text": message}]}
    data = json.dumps({"contents": gemini_history + [new_message]}).encode("utf-8")
    headers = {
        "Content-Type": "application/json",
        "x-goog-api-key": api_key,
    }
    request = Request(URL, data=data, headers=headers)
    response = urlopen(request, timeout=30)
    result = json.loads(response.read().decode("utf-8"))
    return result["candidates"][0]["content"]["parts"][0]["text"]


def get_reply(message, chat_history, gemini_history, api_key=None):
    command = clean_message(message)

    if command == "bye":
        return "Goodbye!", False
    if command == "help":
        return "Commands: help, time, date, history, bye", True
    if command == "time":
        return "The time is " + datetime.now().strftime("%H:%M") + ".", True
    if command == "date":
        return "The date is " + datetime.now().strftime("%Y-%m-%d") + ".", True
    if command == "history":
        if len(chat_history) == 0:
            return "No chat history yet.", False
        return "Chat history:\n" + "\n".join(chat_history), False
    if command in RESPONSES:
        return RESPONSES[command], True
    if not api_key:
        return "Please add your Gemini API key first. Type 'help' to see commands.", True

    try:
        return ask_gemini(message, gemini_history, api_key), True
    except (HTTPError, URLError, TimeoutError, KeyError, IndexError, json.JSONDecodeError):
        return "Sorry, I could not reach Gemini right now.", True


def save_chat(message, reply, chat_history, gemini_history):
    chat_history.append("You: " + message)
    chat_history.append("Vozera AI: " + reply)
    gemini_history.append({"role": "user", "parts": [{"text": message}]})
    gemini_history.append({"role": "model", "parts": [{"text": reply}]})


def main():
    print("Vozera AI v0.5")
    print("Type 'help' to see commands.")
    print("Type 'bye' to stop.\n")

    api_key = os.getenv("GEMINI_API_KEY")
    chat_history = []
    gemini_history = []

    while True:
        message = input("You: ")
        reply, should_save = get_reply(message, chat_history, gemini_history, api_key)
        print("Vozera AI: " + reply)

        if should_save:
            save_chat(message, reply, chat_history, gemini_history)

        if clean_message(message) == "bye":
            break


if __name__ == "__main__":
    main()
