import os
import sys
import shutil
from html import markdown_to_html_node

def generate_public():
    dst_path = "./public/"
    src_path = "./static/"
    shutil.rmtree(os.path.normpath(dst_path))
    shutil.copytree(os.path.normpath(src_path), os.path.normpath(dst_path))

def extract_title(md):
    if(not md.startswith("# ")):
        raise Exception("No header found")
    header = ""
    i = 2
    while(md[i] != "\n"):
        header += md[i]
        i+=1

    return header.strip()

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, 'r') as f: 
        md = f.read()

    with open(template_path, 'r') as f: 
        template = f.read()

    html_node = markdown_to_html_node(md)
    html_string = html_node.to_html()

    title = extract_title(md)

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html_string)
    template = template.replace(r'href="/', f'href="{basepath}')
    template = template.replace(r'src="/', f'src="{basepath}')

    path_dir = os.path.dirname(dest_path)
    if(not os.path.isdir(path_dir)):
        os.makedirs(path_dir)

    with open(dest_path, 'w') as f: 
        f.write(template)

    return

def generate_pages_recursively(dir_path_content, template_path, dest_dir_path, basepath):
    list_files = os.listdir(dir_path_content)

    for file in list_files:
        file_path = os.path.join(dir_path_content, file)
        if(os.path.isfile(file_path)):
            if file.endswith(".md"):
                dest_path = os.path.join(dest_dir_path, file[:-2:] + "html")
                generate_page(file_path, template_path, dest_path, basepath)

        else:
            dest_path = os.path.join(dest_dir_path, file)
            generate_pages_recursively(file_path, template_path, dest_path, basepath)


def main():
    if(len(sys.argv) > 1):
        basepath = sys.argv[1]
    else: 
        basepath = "/"
#    generate_public()
    from_path = "./content"
    dest_path = "./docs"
    template_path = "./template.html"

    generate_pages_recursively(from_path, template_path, dest_path, basepath)



if __name__ == "__main__":
    main()
