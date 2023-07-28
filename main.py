import os


styles = {"S": "_", "K": "-", "R": " "}
folders = [f for f in os.listdir() if os.path.isdir(f)]

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
        print(f"Failed to rename {folder}; {dest} already exists")
    else:
        os.rename(folder, dest)
        print(f"Renamed {folder} to {dest}")
