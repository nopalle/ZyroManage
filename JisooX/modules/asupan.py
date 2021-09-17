import requests
from JisooX.events import register
from JisooX import telethn as tbot


@register(pattern="^/asupan ?(.*)")
async def asupan(event):
    try:
        resp = requests.get("https://api-tede.herokuapp.com/api/asupan/ptl").json()
        asupannya = f"{resp['url']}"
        return await tbot.send_file(event.chat_id, asupannya)
    except Exception:
        await event.reply("`sabar coli dulu`")


@register(pattern="^/chika ?(.*)")
async def chika(event):
    try:
        resp = requests.get("https://api-tede.herokuapp.com/api/chika").json()
        chikanya = f"{resp['url']}"
        return await tbot.send_file(event.chat_id, chikanya)
    except Exception:
        await event.reply("`sabar coli dulu`")
