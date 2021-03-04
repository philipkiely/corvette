import os
from jinja2 import Environment, FileSystemLoader, select_autoescape

def get_icon(conf, ext):
    for icon, extensions in conf["file_icons"].items():
        if ext in extensions:
            return icon
    else:
        return conf["default_icon"]


def insert_index(conf, env, target, breadcrumbs, lines):
    # Make index.html from template + data (Jinja)
    # Insert into correct directory
    html = env.get_template("corvette.html").render({
        "root_name": conf["root_name"],
        "root_link": conf["root_link"],
        "breadcrumbs": [[x, y] for x, y in breadcrumbs.items()],
        "lines": lines
    })
    f = open(target+"/index.html", "w")
    f.write(html)
    f.close()
    return


def build_line(conf, name, is_file):
    l = {}
    if not is_file:
        l["icon"] = conf["folder_icon"]
        l["file"] = False
    else:
        l["icon"] = get_icon(conf, name.split(".")[-1])
        l["file"] = True
    if name[0] == ".":
        l["hide"] = True
    else:
        l["hide"] = False
    l["text"] = name
    l["link"] = name
    return l

def autoindex(conf):
    base_dir = conf["build_dir"]
    # Don't index the index file
    os.system("rm {}/index.html {}/**/index.html".format(base_dir, base_dir))
    # Initialize jinja
    env = Environment(
        loader=FileSystemLoader(
            [conf["template_dir"]]),
        autoescape=select_autoescape(["html", "xml"]),
        auto_reload=True
    )
    # Walk directory to build pages
    for cur, subdirs, files in os.walk(base_dir):
        lines = []
        for s in subdirs:
            lines.append(build_line(conf, s, False))
        for f in files:
            lines.append(build_line(conf, f, True))
        # Build breadcrumbs
        path = [p for p in cur.split("/") if p not in base_dir.split("/")]
        breadcrumbs = {}
        for i in range(len(path)):
            breadcrumbs[path[i]] = "/".join(path[:i+1])
        # Define where we are going to put the output
        target = cur
        # Generate and insert the directory listing page
        insert_index(conf, env, target, breadcrumbs, lines)
    return