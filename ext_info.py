#!/user/bin/python3

import sys
from pathlib import Path


#in_path = input("Please enter a folder path: ")
#folder = Path(in_path)

if not sys.argv[1:]:
    print("usage: ext_info.py path")
    print("displays number of files and total size of files per extension in the specified path.")
    quit()

folder = Path(sys.argv[1])
f_type_dict = {}

for p in folder.iterdir():
    if p.is_file():
        if p.suffix in f_type_dict:
            f_type_dict.update({p.suffix:(f_type_dict[p.suffix][0]+1,f_type_dict[p.suffix][1]+p.stat().st_size)})

        else:
            f_type_dict.update({p.suffix:(1,p.stat().st_size)})


f_type_dict[".."] = f_type_dict[""]
del f_type_dict[""]


for key in sorted(f_type_dict.keys()):
    print("{} {} {}".format(key[1:], f_type_dict[key][0],f_type_dict[key][1]))


