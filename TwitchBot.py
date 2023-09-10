import env
from twitchAPI.twitch import Twitch
from twitchAPI.oauth import UserAuthenticator
from twitchAPI.types import AuthScope, ChatEvent
from twitchAPI.chat import Chat, EventData, ChatMessage
import asyncio
import pydirectinput

USER_SCOPE = [AuthScope.CHAT_READ]


async def on_ready(ready_event: EventData):
    print("The bot is ready")

    await ready_event.chat.join_room(env.TARGET_CHANNEL)

async def on_message(msg: ChatMessage):
    if msg.text == env.down:
        pydirectinput.press("s", env.steps)
    if msg.text == env.up:
        pydirectinput.press("w", env.steps)
    if msg.text == env.left:
        pydirectinput.press("a", env.steps)
    if msg.text == env.right:
        pydirectinput.press("d", env.steps)
    if msg.text == env.BtnA:
        pydirectinput.press("k")
    if msg.text == env.Select:
        pydirectinput.press("i")
    if msg.text == env.BtnB:
        pydirectinput.press("j")
    if msg.text == env.Select:
        pydirectinput.press("u")



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

