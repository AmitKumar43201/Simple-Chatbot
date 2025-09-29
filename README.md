# Simple Chatbot with Gemini 2.0 Flash

This project demonstrates how to build a simple chatbot using **LangChain**, **Google’s Gemini 2.0 Flash model**, and a **state graph** for managing conversation flow. The chatbot supports multi-turn conversations, keeps track of chat history, and displays token usage after each response.

---

## Features
- Uses **Gemini 2.0 Flash** (Google Generative AI).
- Maintains **conversation history** with `HumanMessage` and `AIMessage`.
- Prints **token usage** (input and output tokens).
- Built with a **StateGraph** for structured processing.
- Simple **interactive loop** to chat until the user types `exit`.

---