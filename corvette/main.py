import os
import sys

class Page:

    def __init__(self, parent, name, subdirs, files):
        self.parent = parent # None if root, else Page
        self.children = [] # Stays empty if leaf
        self.files = files
        self.name = name # The file or folder name, including extension
        if parent:
            self.path = parent.path + name + "/"
        else:
            self.path = name + "/"
        # self.modified = "" # The timestamp this was changed at
        # self.size = "" # In KB/MB/etc preferably
        self.add_children(subdirs)
    
    def __repr__(self):
        return "Page()"
    
    def __str__(self):
        return self.path
    
    # Populate children array from input
    def add_children(self, subdirs):
        for s in subdirs:
            if s[0] != ".": # Ignore hidden
                cur, s_subdirs, s_files = next(os.walk(self.path + s))
                self.children.append(Page(self, s, s_subdirs, s_files))

    def is_root(self):
        if self.parent:
            return False
        return True

    def is_leaf(self):
        if self.children == []:
            return True
        return False
    
    # Based on file type or folder, return appropriate icon
    def get_icon(self):
        folders = ["/"]  # These should be class variables
        # and so on, probably combine these in one object
        images = [".png", ".jpg"]
        # if extension in whatever
            # return icons[whatever]
        # return default
        return None


def traverse(base_dir):
    cur, subdirs, files = next(os.walk(base_dir))
    return Page(None, base_dir, subdirs, files)


if __name__=="__main__":
    print(traverse(sys.argv[1]))
