def categorize_file(filename):
    category = {
        ".txt": "Text",
        ".docx": "Document",
        ".py": "Code"
    }
    get_category = lambda extension: category.get(extension, "Unknown")
    return get_category(filename[filename.rfind("."):])


def test(filename):
    category = categorize_file(filename)
    print(f"The file {filename} is of type {category}")


def main():
    files = [
        "document1.txt",
        "notes.docx",
        "essay.docx",
        "bot.py",
        "unknown.xyz",
    ]

    for file in files:
        test(file)


main()
