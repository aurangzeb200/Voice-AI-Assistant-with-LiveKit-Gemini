# 🗣️ Voice AI Assistant "Friday" with LiveKit & Gemini

This project implements a real-time, voice-enabled AI assistant inspired by Iron Man’s Friday. It uses the [LiveKit Agents SDK](https://docs.livekit.io/agents/) to handle speech input/output and orchestrates tasks with Google Gemini for LLM responses, Cartesia for TTS, and Deepgram for STT.

Friday is sarcastic, classy, and always responds in one sentence — just as you'd expect from a fictional AI butler.

---

## 🧠 Core Features

- Persona-based LLM prompt engineering (Friday from Iron Man)
- Voice-to-voice conversation loop using:
  - STT: Deepgram (multilingual)
  - LLM: Google Gemini 2.0 Flash
  - TTS: Cartesia Sonic-2
- Tools:
  - Web search using DuckDuckGo via LangChain
  - Real-time weather lookup via wttr.in
- Voice Activity Detection (VAD) and Noise Cancellation via Silero & BVC

---

## 🔧 Tech Stack

- [LiveKit Agents](https://docs.livekit.io/agents/)
- [Google Gemini API](https://ai.google.dev/)
- [Cartesia TTS](https://docs.cartesia.ai/)
- [Deepgram STT](https://developers.deepgram.com/)
- [LangChain](https://www.langchain.com/)
- [DuckDuckGo Search](https://python.langchain.com/docs/integrations/tools/duckduckgo_search/)
- Python | asyncio | dotenv

---

## ⚠️ Notes

- Requires API keys for Google Gemini, Deepgram, and Cartesia.
- Use `.env` to securely store credentials.
