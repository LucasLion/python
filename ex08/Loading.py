import shutil

def ft_tqdm(lst: range) -> None:
    total_len = len(lst)
    terminal_width = shutil.get_terminal_size().columns
    print("Terminal width: ", terminal_width)
    print("Total length: ", total_len)
    for i, elem in enumerate(lst, start=1):
        progress = i / total_len
        bar = "█" * int(progress * terminal_width)
        print(f"\r{bar}", end="")
        yield elem


def main():
    for _ in ft_tqdm(range(0, 333)):
        pass


if __name__ == "__main__":
    main()
