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

#sleep how many times after each edit in 'abc' 
EDIT_SLEEP = 1
#edit how many times in 'abc' 
EDIT_TIMES = 28





#sleep how many times after each edit in 'iri' 
EDIT_SLEEP = 1
#edit how many times in 'iri' 
EDIT_TIMES = 6





#sleep how many times after each edit in 'sangee' 
EDIT_SLEEP = 1
#edit how many times in 'sangee' 
EDIT_TIMES = 14






abcdefg = [
        "bismillah"
        "a"
        "b"
        "c"
        "d"
        "e"
        "f"
        "g"
        "h"
        "i"
        "j"
        "k"
        "l"
        "m"
        "n"
        "o"
        "p"
        "q"
        "r"
        "s"
        "t"
        "u"
        "v"
        "w"
        "x"
        "y"
        "z"
        "hebat ga gue😎"
]


iri = [
     "**IRI?**"
     "**BILANG BOSS HAHAHHAA**"
     "**YAHAHAH WAHYUU**"
     "**PAPALEPAPALE**"
]


sangee = [
       "**P YANG SANGE PC AKU DONG**"
       "**AKU SANGE BANGET INI😔**"
       "**YANG MAU LIAT TITIT 5 HEKTAR PC AJA**"
       "**AKU LIMIT NIH AYO PC AJA DIJAMIN PUAS🥺**"
       "**KITA ENAK ENAK BARENG MAU GA🥺👉👈**"
       "**YANG MAU PC YA🥺**"


