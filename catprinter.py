from printer import pretty_print
# username: marhealw

def draw_cat():
    cat = r"""
 /\_/\    /\_/\    /\_/\
( o.o )  ( o.o )  ( o.o )
 > ^ <    > ^ <    > ^ <
"""
    return cat

def draw_cats(num_cats):
    for i in range(num_cats):
        pretty_print(draw_cat())

