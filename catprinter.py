from printer import pretty_print

def draw_cat():
<<<<<<< HEAD
    cat = r"""
 /\_/\      /\–/\      /\_/\
( o.o )    |.>ω<.|    ฅ •ﻌ• ฅ
 > ^ <      \___/      \___/

(press ctr+C to stop)
>>>>>>> 7e9cee3 (Добавлен комментарий остановки)
"""
    return cat

def draw_cats():
    while True:
        pretty_print(draw_cat())

