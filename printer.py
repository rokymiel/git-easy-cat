import random

colors = [
    "\033[91m",  # Red
    "\033[92m",  # Green
    "\033[93m",  # Yellow
    "\033[94m",  # Blue
    "\033[95m",  # Magenta
    "\033[96m",  # Cyan
    "\033[97m",  # White
]
reset_color = "\033[0m"

# Делает красивый вовод сообщений
def pretty_print(message):
    color = random.choice(colors)
    print(color + message + reset_color)

