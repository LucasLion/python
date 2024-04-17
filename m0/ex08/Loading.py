import shutil
import sys
from time import sleep

def hide_cursor():
    sys.stdout.write("\033[?25l")  # Masque le curseur

def show_cursor():
    sys.stdout.write("\033[?25h")  # Rétablit le curseur

def clear_line():
    sys.stdout.write("\033[K")  # Efface la ligne actuelle dans la console
    sys.stdout.flush()


def ft_tqdm(lst: range):
    total_len = len(lst)
    terminal_width = int(shutil.get_terminal_size().columns)
    for i, elem in enumerate(lst, start=1):
        percent = int(i / total_len * 100)
        progress = int(i / total_len * (terminal_width - 10))
        bar = "█" * progress
        empty = " " * int(terminal_width - progress - 10)
        if percent % 10 == 0:
            print(f"{percent}% [{bar}{empty}]", end="\r", flush=True)
        yield elem
    print(f"{percent}% [{bar}{empty}]")
    clear_line()


def main():
    hide_cursor()  # Masque le curseur au début du programme
    try:
        for _ in ft_tqdm(range(333)):
            sleep(0.005)
    finally:
        show_cursor()  # Rétablit le curseur à la fin du programme

if __name__ == "__main__":
    main()

