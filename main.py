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
    return styles[style].join(words)


for folder in folders:
    dest = get_style(folder)
    if os.path.isdir(dest):
        failed.append(dest)
    else:
        os.rename(folder, dest)
        renamed.append(folder)

if renamed:
    print(f"Renamed:")
    for folder in renamed:
        print(f"  {folder}")
if failed:
    print(f"Failed to rename:")
    for folder in failed:
        print(f"  {folder}")
