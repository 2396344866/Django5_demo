import os
def generate_markdown_tree(folder_path, indent=0):
    markdown = ""
    items = sorted(os.listdir(folder_path))
    for index, item in enumerate(items):
        item_path = os.path.join(folder_path, item)
        is_last = index == len(items) - 1
        prefix = "└── " if is_last else "├── "
        if item in [".venv"]:
            markdown += "  " * indent + prefix + f"{item}/\n"
            continue
        if item in [".idea", "__pycache__"]:
            continue
        if os.path.isdir(item_path):
            markdown += "  " * indent + prefix + f"{item}/\n"
            markdown += generate_markdown_tree(item_path, indent + 1)
        else:
            markdown += "  " * indent + prefix + f"{item}\n"
    return markdown


def save_markdown_to_file(markdown_content, output_file):
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(markdown_content)
        print(f"Markdown 文件已保存至 {output_file}")
    except Exception as e:
        print(f"保存文件时出错: {e}")


if __name__ == "__main__":
    target_folder = r'E:\pycharmproject\DjangoProject\Django_demo'
    output_md_file = 'path_include_floder.md'
    md_tree = generate_markdown_tree(target_folder)
    save_markdown_to_file(md_tree, output_md_file)
