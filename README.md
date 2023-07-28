# Folder Style Converter

A Python script to rename all directories in the current path according to the selected naming convention: Snake, Kebab, or Regular case.

## Usage

```bash
python main.py
```

Prompt:

```bash
Choose folder name style: S - Snake, K - Kebab, R - Regular
```

The script will rename all folders accordingly, skipping those that cannot be renamed due to conflicts.

## Styles

- Snake (S): my_folder_name
- Kebab (K): my-folder-name
- Regular (R): my folder name
