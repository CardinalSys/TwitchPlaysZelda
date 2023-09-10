import env
from twitchAPI.twitch import Twitch
from twitchAPI.oauth import UserAuthenticator
from twitchAPI.types import AuthScope, ChatEvent
from twitchAPI.chat import Chat, EventData, ChatMessage
import asyncio
import pydirectinput

USER_SCOPE = [AuthScope.CHAT_READ]


async def on_ready(ready_event: EventData):
    print("El bot está listo")

    await ready_event.chat.join_room(env.TARGET_CHANNEL)

async def on_message(msg: ChatMessage):
    print(msg.text)
    if msg.text == "!aba":
        pydirectinput.press("s", 2)
    if msg.text == "!arr":
        pydirectinput.press("w", 2)
    if msg.text == "!izq":
        pydirectinput.press("a", 2)
    if msg.text == "!der":
        pydirectinput.press("d", 2)
    if msg.text == "!a":
        pydirectinput.press("k")
    if msg.text == "!srt":
        pydirectinput.press("i")
    if msg.text == "!b":
        pydirectinput.press("j")



async def run():
    twitch = await Twitch(env.APP_ID, env.APP_SECRET)
    auth = UserAuthenticator(twitch, USER_SCOPE)
    token, refresh_token = await auth.authenticate()

    await twitch.set_user_authentication(token, USER_SCOPE, refresh_token)

    chat = await Chat(twitch)

    chat.register_event(ChatEvent.READY, on_ready)

    chat.register_event(ChatEvent.MESSAGE, on_message)

    chat.start()


asyncio.run(run())

