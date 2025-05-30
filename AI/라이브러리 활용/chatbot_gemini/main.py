import asyncio
import base64
import json
import os
import pyaudio
from websockets.client import connect
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class SimpleGeminiVoice:
    def __init__(self):
        self.audio_queue = asyncio.Queue()
        self.api_key = os.environ.get("GEMINI_API_KEY")
        self.model = "gemini-2.0-flash-exp"
        self.uri = f"wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1alpha.GenerativeService.BidiGenerateContent?key={self.api_key}"
        # Audio settings
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.CHUNK = 512
        self.RATE = 16000
        self.model_speaking = False

    async def start(self):
        # Initialize websocket
        self.ws = await connect(
            self.uri,
            extra_headers={"Content-Type": "application/json"}
        )
        await self.ws.send(json.dumps({"setup": {"model": f"models/{self.model}"}}))
        await self.ws.recv()
        print("인공지능이 연결되었습니다. 대화를 시작할께요.")
        # Start audio streaming
        async with asyncio.TaskGroup() as tg:
            tg.create_task(self.capture_audio())
            tg.create_task(self.stream_audio())
            tg.create_task(self.play_response())

    async def capture_audio(self):
        audio = pyaudio.PyAudio()
        stream = audio.open(
            format=self.FORMAT,
            channels=self.CHANNELS,
            rate=self.RATE,
            input=True,
            frames_per_buffer=self.CHUNK,
        )

        while True:
            data = await asyncio.to_thread(stream.read, self.CHUNK)
            # Only send audio when model is not speaking
            if not self.model_speaking:
                await self.ws.send(json.dumps({
                    "realtime_input": {
                        "media_chunks": [{
                            "data": base64.b64encode(data).decode(),
                            "mime_type": "audio/pcm",
                        }]
                    }
                }))

    async def stream_audio(self):
        async for msg in self.ws:
            response = json.loads(msg)
            try:
                audio_data = response["serverContent"]["modelTurn"]["parts"][0]["inlineData"]["data"]
                if not self.model_speaking:
                    self.model_speaking = True
                    print("\n인공지능이 대화를 시작합니다.")
                self.audio_queue.put_nowait(base64.b64decode(audio_data))
            except KeyError:
                pass
            
            try:
                turn_complete = response["serverContent"]["turnComplete"]
            except KeyError:
                pass
            else:
                if turn_complete:
                    print("\n대화가 끝났습니다.")
                    # Wait a bit to ensure all audio is processed
                    await asyncio.sleep(0.5)
                    while not self.audio_queue.empty():
                        self.audio_queue.get_nowait()
                    self.model_speaking = False
                    print("=" * 30)
                    print("당신의 음성을 기다리고 있습니다.")

    async def play_response(self):
        audio = pyaudio.PyAudio()
        stream = audio.open(
            format=self.FORMAT,
            channels=self.CHANNELS,
            rate=24000,
            output=True
        )
        while True:
            data = await self.audio_queue.get()
            await asyncio.to_thread(stream.write, data)


if __name__ == "__main__":
    client = SimpleGeminiVoice()
    asyncio.run(client.start())