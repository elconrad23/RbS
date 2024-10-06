from rich.console import Console
from rich.live import Live
from rich.text import Text
import time
import sys

console = Console()

def render_lines(length):
    output = Text()
    for i in range(1, 6):
        output.append('-' * (length + i * 2) + "\n")
    return output

length = 5
with Live(render_lines(length), refresh_per_second=4) as live:
    while True:
        command = input("Winning (+) Losing (-) ").strip()
        if command == 'i':
            length += 2
        elif command == 'd':
            length = max(1, length - 2)
            # , or Quit (q):
        elif command == 'q' or length == 12:
            break
        live.update(render_lines(length))
