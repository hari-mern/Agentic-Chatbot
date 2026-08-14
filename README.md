# Agentic AI Chatbot (LangGraph + Streamlit)

A conversational chatbot built with **LangGraph**, **LangChain**, and **Streamlit**, powered by **Groq's LLM API**. The project demonstrates a stateful, graph-based agent pipeline where every step — from state definition to node execution to graph compilation — is modular and config-driven.

This was my attempt at building an end-to-end agentic AI application the "right way": a clean separation between the UI layer, the LLM integration, and the graph logic, so adding new use cases later is just a matter of adding a node and an edge.

## What it does

- A Streamlit sidebar where you pick your LLM provider, model, and paste your API key
- A stateful conversation graph: user message goes in → chatbot node processes it → response comes out
- Conversation state tracked through LangGraph's `add_messages` reducer, so multi-turn chat behaves like a real conversation
- All UI options (models, use cases, page title) are loaded from a config file instead of being hardcoded in the UI code

## Project structure

```
AgenticChatbot/
├── app.py                                 # Entry point
├── requirements.txt
├── src/langgraphagenticai/
│   ├── main.py                            # App orchestration: UI → LLM → graph → output
│   ├── LLMS/
│   │   └── groqllm.py                     # Groq LLM wrapper (ChatGroq)
│   ├── graph/
│   │   └── graph_builder.py               # Builds the StateGraph for each use case
│   ├── nodes/
│   │   └── basic_chatbot_node.py          # Chatbot node logic (invokes the LLM)
│   ├── state/
│   │   └── state.py                       # TypedDict state with messages reducer
│   └── ui/
│       ├── uiconfigfile.ini               # UI options: models, use cases, title
│       ├── uiconfigfile.py                # Reads the .ini and exposes options
│       └── streamlitui/
│           ├── loadui.py                  # Sidebar controls
│           └── display_result.py          # Streams the response to the UI
```

## How the graph works

```
START ──▶ chatbot ──▶ END
```

1. **State** (`state/state.py`) — a `TypedDict` holding a `messages` list. The `add_messages` annotation merges new messages into the existing history instead of overwriting it.
2. **Node** (`nodes/basic_chatbot_node.py`) — receives the state, calls the LLM with the full message history, and returns the model's reply as a new message.
3. **Graph** (`graph/graph_builder.py`) — wires the node between `START` and `END`, then compiles it. The `setup_graph()` method is designed to branch by use case, so a second chatbot type (e.g. a RAG or tool-calling bot) can be added without touching the existing code.

The config file (`ui/uiconfigfile.ini`) controls what shows up in the sidebar, so most UI changes are config edits rather than code changes.

## Getting started

### Prerequisites

- Python 3.12+
- A [Groq API key](https://console.groq.com/keys) (free tier works)

### Installation

```bash
# clone and enter the project
git clone <your-repo-url>
cd AgenticChatbot

# create and activate a virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS / Linux

# install dependencies
pip install -r requirements.txt
```

### Running it

```bash
streamlit run app.py
```

Then open the local URL Streamlit prints (default `http://localhost:8501`), paste your Groq API key in the sidebar, pick a model, and start chatting.

## Configuring the UI

Everything in the sidebar is driven by `src/langgraphagenticai/ui/uiconfigfile.ini`:

```ini
[DEFAULT]
PAGE_TITLE = LangGraph: Build Statful Agentic AI Graph
LLM_OPTIONS = Groq
USECASE_OPTIONS = Basic Chatbot
GROQ_MODEL_OPTIONS = llama-3.1-8b-instant, llama-3.3-70b-versatile, qwen/qwen3.6-27b
```

To add a model or a new use case, just edit this file — the app picks up the options automatically. Options are split on `", "`, so keep that separator when adding more models.

## Roadmap

- RAG use case with a retrieval node feeding context into the prompt
- Tool-calling agent (Groq supports function calling via LangChain's tool decorators)
- Persistence layer with `MemorySaver` so chat history survives page refreshes

## License

This is a personal learning project — feel free to fork it and build on it.
