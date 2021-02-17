import os
import sys

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

def autoindex(base_dir):
    for cur, subdirs, files in os.walk(base_dir):
        lines = []
        for s in subdirs:
            l = {}
            l["icon"] = "folder-fill"
            l["text"] = cur.split("/")[-1]
            l["link"] = base_dir + s[1:]
            lines.append(l)
        for f in files:
            l = {}
            l["icon"] = get_icon(f.split(".")[-1])
            l["text"] = cur.split("/")[-1]
            l["link"] = base_dir + s[1:]
            lines.append(l)
        breadcrumbs = cur[1:].split("/")



if __name__=="__main__":
    print(autoindex(sys.argv[1]))
