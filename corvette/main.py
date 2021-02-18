import os
import sys
from jinja2 import Environment, FileSystemLoader, select_autoescape

def get_icon(ext):
    icons = {
        "file-earmark-code": ["html", "css", "scss", "js", "ts", "py", "ipynb", "php", "rb", "haml", "c", "r"], # Woefully incomplete
        "file-earmark-image": ["jpg", "png", "tiff", "psd", "raw", "heic", "svg"],
        "file-earmark-music": ["mp3", "wav", "ogg", "m4a"],
        "file-earmark-play": ["mp4", "m4v", "mkv", "mov", "qt", "mpg", "gif", "gifv"],
        "file-earmark-ppt": ["pptx", "ppt"],
        "file-earmark-richtext": ["pdf"],
        "file-earmark-spreadsheet": ["csv", "xlsx", "xlsm", "xlsb", "xltx", "xls"],
        "file-earmark-text": ["txt", "md", "rtf", "tex", "xml", "yml"],
        "file-earmark-word": ["docx", "doc", "pages"],
        "file-earmark-zip": ["zip", "tar", "gz", "7z"]
    }
    for icon, extensions in icons.items():
        if ext in extensions:
            return icon
    else:
        return "file-earmark" # Default for unrecognized files


def insert_index(env, target, breadcrumbs, lines):
    # Make index.html from template + data (Jinja)
    # Insert into correct directory
    html = env.get_template("corvette.html").render({
        "breadcrumbs": [[x, y] for x, y in breadcrumbs.items()],
        "lines": lines
    })
    f = open(target+"/index.html", "w")
    f.write(html)
    f.close()
    return


def build_line(name, is_file):
    l = {}
    if not is_file:
        l["icon"] = "folder-fill"
        l["file"] = False
    else:
        l["icon"] = get_icon(name.split(".")[-1])
        l["file"] = True
    if name[0] == ".":
        l["hide"] = True
    else:
        l["hide"] = False
    l["text"] = name
    l["link"] = name
    return l

def autoindex(base_dir):
    # Don't index the index file
    os.system("rm {}/index.html {}/**/index.html".format(base_dir, base_dir))
    # Initialize jinja
    env = Environment(
        loader=FileSystemLoader(
            ["theme/templates"]),
        autoescape=select_autoescape(["html", "xml"]),
        auto_reload=True
    )
    # Walk directory to build pages
    for cur, subdirs, files in os.walk(base_dir):
        lines = []
        for s in subdirs:
            lines.append(build_line(s, False))
        for f in files:
            lines.append(build_line(f, True))
        # Build breadcrumbs
        path = [p for p in cur.split("/") if p not in base_dir.split("/")]
        breadcrumbs = {}
        for i in range(len(path)):
            breadcrumbs[path[i]] = "/".join(path[:i+1])
        # Define where we are going to put the output
        target = cur
        # Generate and insert the directory listing page
        insert_index(env, target, breadcrumbs, lines)
    return

if __name__=="__main__":
    # I probably want a site name parameter...and maybe a corvette_config file?
    autoindex(sys.argv[1])
