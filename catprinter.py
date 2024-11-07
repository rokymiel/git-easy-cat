from printer import pretty_print


def draw_cat():
    cat = r"""
 /\_/\      /\–/\      /\_/\
( o.o )    |.>ω<.|    ฅ •ﻌ• ฅ
 > ^ <      \___/      \___/
GOOD LUCK HAVE FUN!
GOOD LUCK HAVE FUN!
GOOD LUCK HAVE FUN!
"""
    return cat

def draw_cats():
    while True:
        pretty_print(draw_cat())

