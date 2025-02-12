import os
from pathlib import Path
from markdown_blocks import markdown_to_html_node

def generate_page(from_path, template_path, dest_path):
    print(f" * Generating page from {from_path} to {dest_path} using {template_path}")
    markdown = Path(from_path).read_text()
    template = Path(template_path).read_text()

    content = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)

    html = template.replace("{{ Title }}", title).replace("{{ Content }}", content)
    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    Path(dest_path).write_text(html)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for file in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, file)
        dest_path = os.path.join(dest_dir_path, file)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix('.html')
            generate_page(from_path, template_path, dest_path)
        else:
            generate_pages_recursive(from_path, template_path, dest_path)


def extract_title(md):
    lines = md.split('\n')
    for line in lines:
        if line.startswith('# '):
            return line[2:].strip()
    raise Exception("no header found")