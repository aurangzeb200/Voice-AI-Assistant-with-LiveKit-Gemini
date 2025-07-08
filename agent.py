from dotenv import load_dotenv

from livekit import agents
from livekit.agents import AgentSession, Agent, RoomInputOptions
from livekit.plugins import (
    cartesia, 
    deepgram, 
    noise_cancellation,
    silero,
)

from livekit.plugins.turn_detector.multilingual import MultilingualModel
from livekit.plugins import google
from prompts import AGENT_INSTRUCTION,SESSION_INSTRUCTION
from tools import search, get_weather

load_dotenv()


class Assistant(Agent):
    def __init__(self) -> None:
        super().__init__(instructions=AGENT_INSTRUCTION)
        tools = [
            search,
            get_weather
        ]
        

async def entrypoint(ctx: agents.JobContext):
    session = AgentSession(
        stt=deepgram.STT(
            model="nova-3",
            language="multi",
            api_key="c5b394d51d34c7cb0be0cb0b5f4ab649e12f0805"
            ),
            
         llm=google.LLM(
        model="gemini-2.0-flash-exp",
        temperature=0.8,
        api_key="AIzaSyBtG2deAz3H_hpsOl5v-lIM88EZqYoXXOo"
    ),
    
        tts=cartesia.TTS(
            model="sonic-2",
            voice="f786b574-daa5-4673-aa0c-cbe3e8534c02",
            api_key="sk_car_Q5Wp6j1jQmx5MJWxnAKuxC"
            ),
        vad=silero.VAD.load()
        # turn_detection=MultilingualModel(),
    )

    await session.start(
        room=ctx.room,
        agent=Assistant(),
        room_input_options=RoomInputOptions(
            # LiveKit Cloud enhanced noise cancellation
            # - If self-hosting, omit this parameter
            # - For telephony applications, use `BVCTelephony` for best results
            video_enabled=True,
            noise_cancellation=noise_cancellation.BVC(), 
        ),
    )

    await ctx.connect()

    await session.generate_reply(
        instructions=SESSION_INSTRUCTION
    )


if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))