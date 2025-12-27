from pathlib import Path

current_dir = Path.cwd()
current_fie = Path(__file__).name

print(f"Files in {current_dir}:")

for filepath in current_dir.iterdir():
    if filepath == current_fie:
        continue

    print (f" - {filepath.name}")

    if filepath.is_file():
        content = filepath.read_text(encoding='utf-8')
        print (f" Content: {content}")

