import os
import sys
import json
from corvette.autoindex import autoindex

def main():
    if len(sys.argv) == 2:
            conf_path = sys.argv[1]
    else:
        print("Usage: python -m corvette path/to/corvetteconf.json")
        return
    dirname = os.path.dirname(__file__)
    # First load default conf
    default_path = os.path.join(dirname, "conf.json")
    default_file = open(default_path, "r")
    conf = json.loads(default_file.read())
    default_file.close()
    # Then load user conf
    conf_file = open(conf_path, "r")
    user_conf = json.loads(conf_file.read())
    conf_file.close()
    # Override default conf with user conf
    for key in conf.keys():
        if key in user_conf:
            conf[key] = user_conf[key]
    if conf["template_dir"] == "False":
        conf["template_dir"] = os.path.join(dirname, "theme/templates")
    autoindex(conf)
