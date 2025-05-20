import glob
from pathlib import Path

# dir_Path = Path("Dir1/Dir2/Dir3")
# Step 1: Create one parent directory and 3 subdirectories
parent_dir = Path("parent_dir")
parent_dir.mkdir(parents=True, exist_ok=True)

# Create 3 subdirectories inside parent_dir
dir1 = parent_dir / "dir1"
dir2 = parent_dir / "dir2"
dir3 = parent_dir / "dir3"
dir1.mkdir(parents=True, exist_ok=True)
dir2.mkdir(parents=True, exist_ok=True)
dir3.mkdir(parents=True, exist_ok=True)

# Step 2: Create test .txt files in each subdirectory
file_contents = {
    "file1.txt": "Line one\nLine two\nLine three",
    "file2.txt": "Only one line",
    "file3.txt": "First line\nSecond line",
}

# Files in dir1
for filename, content in file_contents.items():
    file_path = dir1 / filename
    with file_path.open("w", encoding="utf-8") as f:
        f.write(content)

# Files in dir2
for filename, content in file_contents.items():
    file_path = dir2 / filename
    with file_path.open("w", encoding="utf-8") as f:
        f.write(content)

# Files in dir3
for filename, content in file_contents.items():
    file_path = dir3 / filename
    with file_path.open("w", encoding="utf-8") as f:
        f.write(content)

if not parent_dir.exists():
    print(f"Directory {parent_dir} does not exist.")
else:

    print("Using Glob Module:")

    glob_module = glob.glob(str(parent_dir / "**/*.txt"), recursive=True)
    if not glob_module:
        print("no file found")
    else:
        for file_path in glob_module:
            with open(file_path, "r", encoding="utf-8") as f:
                line_count = sum(1 for _ in f)
            print(f"{file_path} - {line_count} lines")

    print("\n Using pathlib Module: ")

    pathlib_module = list(parent_dir.rglob("*.txt"))
    if not pathlib_module:
        print("No file found")
    else:
        for file_path in pathlib_module:
            with file_path.open("r", encoding="utf-8") as f:
                line_count = sum(1 for _ in f)
            print(f"{file_path}-{line_count} lines")
