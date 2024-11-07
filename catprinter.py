from printer import pretty_print

def draw_cat():
    cat = r"""
 /\_/\    /\_/\    /\_/\
( o.o )  ( o.o )  ( o.o )
 > ^ <    > ^ <    > ^ <
"""
    return cat

def draw_cats():
    while True:
        pretty_print(draw_cat())

