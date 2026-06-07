# Vozera AI v0.5

Vozera AI is a beginner-friendly chatbot.

Version 0.5 adds a Streamlit web app with a modern chat interface, the Vozera AI logo at the top, visible chat history, commands, and Gemini API support.

## Files created for v0.5

| File | What it does |
| --- | --- |
| `streamlit_app.py` | The main file path for Streamlit Community Cloud deployment. |
| `app.py` | The new Streamlit web app. |
| `assets/vozera-logo.svg` | The Vozera AI logo shown at the top of the web app. |
| `requirements.txt` | Lists the Python package needed to run the web app. |

## Files updated for v0.5

| File | What changed |
| --- | --- |
| `vozerai.py` | The old command-line logic was cleaned into reusable functions so both the terminal app and Streamlit app can use it. |
| `README.md` | This guide now explains the v0.5 web app. |

## Roadmap

- v0.1 - Chat Loop ✅
- v0.2 - Built-in Responses ✅
- v0.3 - Commands ✅
- v0.4 - Real AI API ✅
- v0.5 - Streamlit Web App ✅
- v0.6 - Voice
- v0.7 - PDF Reader
- v1.0 - Public Release

## What the web app does

- Shows the Vozera AI logo at the top.
- Shows the title `Vozera AI`.
- Lets the user chat in a modern web chat interface.
- Shows user messages and AI replies as chat bubbles.
- Shows chat history in the sidebar.
- Keeps the commands `help`, `time`, `date`, `history`, and `bye`.
- Keeps the built-in responses from v0.2.
- Uses Gemini for messages that are not commands or built-in responses.

## How to run the Streamlit web app

Install the needed package:

```bash
pip install -r requirements.txt
```

Run the web app:

```bash
streamlit run streamlit_app.py
```

You can also run the app with:

```bash
streamlit run app.py
```

Streamlit will show a local web address. Open that address in your browser.


## Streamlit deploy settings

On the Streamlit Community Cloud deploy page, use these values:

| Field | What to enter |
| --- | --- |
| Repository | `VozeraAI/Vozera-AI` |
| Branch | `main` |
| Main file path | `streamlit_app.py` |

The screenshot shows the `Main file path` box. Type `streamlit_app.py` there.

## How to get a free Gemini API key

Google AI Studio has a free tier for getting started with the Gemini API, but limits can change.

Official pages:

- Gemini API docs: <https://ai.google.dev/gemini-api/docs>
- Gemini API key docs: <https://ai.google.dev/gemini-api/docs/api-key>
- Gemini API pricing: <https://ai.google.dev/gemini-api/docs/pricing>
- Gemini API rate limits: <https://ai.google.dev/gemini-api/docs/rate-limits>

Steps:

1. Go to Google AI Studio: <https://aistudio.google.com/>
2. Sign in with your Google account.
3. Open the API key page.
4. Create a Gemini API key.
5. Copy the key.
6. Keep the key private.
7. Do not paste your real key into public code or GitHub.

## How to save your API key

Run this command in your terminal.

Replace `your_api_key_here` with your real API key:

```bash
export GEMINI_API_KEY='your_api_key_here'
```

Then run the web app in the same terminal:

```bash
streamlit run streamlit_app.py
```

If you do not add an API key, the commands and built-in responses still work. Gemini replies need the API key.

## Commands

| Command | What it does |
| --- | --- |
| `help` | Shows the list of commands. |
| `time` | Shows the current time. |
| `date` | Shows the current date. |
| `history` | Shows previous chat messages. |
| `bye` | Says goodbye. |

## Built-in responses

| If you type | Vozera AI replies |
| --- | --- |
| `hello` | `Hello! How can I help?` |
| `how are you` | `I am doing great.` |
| `what is your name` | `I am Vozera AI.` |

Messages that are not commands or built-in responses go to Gemini when your API key is available.

## What changed simply

### 1. `vozerai.py` now has reusable logic

The chatbot logic is now inside functions:

```python
def get_reply(message, chat_history, gemini_history, api_key=None):
```

This lets the terminal app and the Streamlit web app use the same chatbot brain.

### 2. `streamlit_app.py` is the deploy file

Streamlit Community Cloud can use this as the main file path:

```python
import app
```

This opens the real web app from `app.py`.

### 3. `app.py` is the new web app

The new file starts Streamlit and creates the web page:

```python
st.set_page_config(page_title="Vozera AI", page_icon="💬", layout="centered")
```

### 4. The logo is shown at the top

The web app shows the logo with:

```python
st.image("assets/vozera-logo.svg", width=260)
```

### 5. The title is Vozera AI

The web app title is:

```python
st.title("Vozera AI")
```

### 6. Chat messages use Streamlit chat bubbles

The app shows chat messages with:

```python
st.chat_message(...)
```

The user types with:

```python
st.chat_input("Ask Vozera AI something...")
```

### 7. Chat history is saved in Streamlit memory

Streamlit memory uses `st.session_state`.

The app saves:

- `messages` for chat bubbles
- `chat_history` for readable history
- `gemini_history` for Gemini API memory

### 8. The sidebar shows chat history

The sidebar shows previous messages and has a clear button.

```python
with st.sidebar:
```

### 9. `requirements.txt` was added

The new web app needs Streamlit:

```text
streamlit>=1.28
```

## Terminal version still works

You can still run the terminal chatbot:

```bash
python3 vozerai.py
```

## Example web chat

```text
You: hello
Vozera AI: Hello! How can I help?

You: time
Vozera AI: The time is 14:30.

You: history
Vozera AI: Chat history:
You: hello
Vozera AI: Hello! How can I help?
You: time
Vozera AI: The time is 14:30.
```
