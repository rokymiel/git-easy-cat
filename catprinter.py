from printer import pretty_print

def draw_cat():
    cat = r"""
<<<<<<< HEAD
 /\_/\    /\_/\    /\_/\
( o.o )  ( o.o )  ( o.o )
 > ^ <    > ^ <    > ^ <
=======
 /\_/\
( o.o )
 > ^ <

(press ctr+C to stop)
>>>>>>> feature-loop
"""
    return cat

def draw_cats():
    while True:
        pretty_print(draw_cat())

