import os


styles = {"S": "_", "K": "-", "R": " "}
folders = [f for f in os.listdir() if os.path.isdir(f)]
renamed = []
failed = []

style = ""
while style not in styles.keys():
    style = input(
        "Choose folder name style: S - Snake, K - Kebab, R - Regular: "
    ).upper()


def get_style(name):
    words = name.replace("_", " ").replace("-", " ").split()
    return styles[style].join(words).lower()


for folder in folders:
    dest = get_style(folder)
    if folder == dest:
        continue
    if os.path.isdir(dest):
        failed.append((folder, dest))
    else:
        os.rename(folder, dest)
        renamed.append((folder, dest))

if renamed:
    print(f"Renamed:")
    for folder, dest in renamed:
        print(f"  {folder} to {dest}")
if failed:
    print(f"Failed to rename:")
    for folder, dest in failed:
        print(f"  {folder}; {dest} already exists")
