from printer import pritty_print

def draw_cat():
    cat = r"""
 /\_/\
( o.o )
 > ^ <
"""
    return cat

def draw_cats(num_cats):
    for i in range(num_cats):
        pritty_print(draw_cat())

