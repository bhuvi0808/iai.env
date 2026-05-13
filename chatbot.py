import os

import google.generativeai as genai


def main() -> None:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("Set GEMINI_API_KEY before running this app.")

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")

    chat = model.start_chat(history=[])
    print("Gemini Chatbot (type 'exit' to quit)")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break
        if not user_input:
            continue

        response = chat.send_message(user_input)
        print(f"Bot: {response.text}\n")


if __name__ == "__main__":
    main()
