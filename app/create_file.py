import sys
from pathlib import Path
from datetime import datetime


def main() -> None:
    args = sys.argv[1:]

    if not args:
        print("Usage: python create_file.py -d <dirs...> -f <filename>")
        return

    dir_parts: list[str] = []
    file_name: str | None = None

    # Обробка прапора -d
    if "-d" in args:
        d_index = args.index("-d")
        for i in range(d_index + 1, len(args)):
            if args[i].startswith("-"):
                break
            dir_parts.append(args[i])

    # Обробка прапора -f
    if "-f" in args:
        f_index = args.index("-f")
        if f_index + 1 < len(args):
            file_name = args[f_index + 1]

    if file_name is None:
        print("No file name provided. Use -f <filename>")
        return

    # Формування шляху
    if dir_parts:
        dir_path = Path(*dir_parts)
        dir_path.mkdir(parents=True, exist_ok=True)
        full_path = dir_path / file_name
    else:
        full_path = Path(file_name)

    # Збір контенту
    lines: list[str] = []
    while True:
        line = input("Enter content line: ")
        if line.strip().lower() == "stop":
            break
        lines.append(line)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    numbered_lines = [f"{i + 1} {line}" for i, line in enumerate(lines)]

    # Запис у файл
    with full_path.open("a", encoding="utf-8") as f:
        f.write(timestamp + "\n")
        f.write("\n".join(numbered_lines) + "\n\n")

    print(f"File created/updated at: {full_path}")


if __name__ == "__main__":
    main()
