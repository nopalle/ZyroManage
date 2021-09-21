import html
import random
import time
from typing import List

from telegram import Bot, Update, ParseMode
from telegram.ext import run_async

from JisooX import dispatcher
from JisooX.modules.disable import DisableAbleCommandHandler
from JisooX.modules.helper_funcs.chat_status import is_user_admin, user_admin
from JisooX.modules.helper_funcs.extraction import extract_user

register(outgoing=True, pattern="^.abc$")
async def koc(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("bismillah")
        sleep(1)
        await e.edit("a")
        sleep(1)
        await e.edit("b")
        sleep(1)
        await e.edit("c")
        sleep(1)
        await e.edit("d")
        sleep(1)
        await e.edit("e")
        sleep(1)
        await e.edit("f")
        sleep(1)
        await e.edit("g")
        sleep(1)
        await e.edit("h") 
        sleep(1) 
        await e.edit("i") 
        sleep(1) 
        await e.edit("j") 
        sleep(1) 
        await e.edit("k") 
        sleep(1) 
        await e.edit("l") 
        sleep(1) 
        await e.edit("m") 
        sleep(1) 
        await e.edit("n") 
        sleep(1) 
        await e.edit("o") 
        sleep(1) 
        await e.edit("p") 
        sleep(1) 
        await e.edit("q") 
        sleep(1) 
        await e.edit("r") 
        sleep(1) 
        await e.edit("s") 
        sleep(1) 
        await e.edit("t") 
        sleep(1) 
        await e.edit("u") 
        sleep(1) 
        await e.edit("v") 
        sleep(1) 
        await e.edit("w") 
        sleep(1) 
        await e.edit("x") 
        sleep(1) 
        await e.edit("y") 
        sleep(1) 
        await e.edit("z") 
        sleep(1) 
        await e.edit("hebat ga gue😎") 

@register(outgoing=True, pattern='^.iri(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**IRI?**")
    sleep(2)
    await typew.edit("**BILANG BOSS HAHAHHAA**")
    sleep(2) 
    await typew.edit("**YAHAHAH WAHYUU**")
    sleep(2)
    await typew.edit("**PAPALEPAPALE**") 

@register(outgoing=True, pattern='^.sangee(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**P YANG SANGE PC AKU DONG**")
    sleep(3)
    await typew.edit("**AKU SANGE BANGET INI😔**")
    sleep(3)
    await typew.edit("**YANG MAU LIAT TITIT 5 HEKTAR PC AJA**")
    sleep(3)
    await typew.edit("**AKU LIMIT NIH AYO PC AJA DIJAMIN PUAS🥺**") 
    sleep(3) 
    await typew.edit("**KITA ENAK ENAK BARENG MAU GA🥺👉👈**") 
    sleep(2)
    await typew.edit("**YANG MAU PC YA🥺**") 
