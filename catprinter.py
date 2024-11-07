from printer import pretty_print

def draw_cat():
    cat = r"""
 /\_/\      /\–/\      /\_/\
( o.o )    |.>ω<.|    ฅ •ﻌ• ฅ
 > ^ <      \___/      \___/

(press ctr+C to stop)
"""
    return cat

def draw_cats():
    while True:
        pretty_print(draw_cat())

