from collections import defaultdict
import os
from functools import partial
import re
from pprint import pprint

dedup_name_files = defaultdict(list)

urls_path = r'C:\Users\SONY\Desktop\Github_Projects\Celebrity-Face-Matcher\Image_Scrapper\Url_List'
get_abs_file_name = partial(os.path.join, urls_path)


for file_name in os.listdir(urls_path):
    write_file_name = "dedup_"+re.split(r'(\d+)', file_name)[0]
    dedup_name_files[get_abs_file_name(write_file_name)].append(get_abs_file_name(file_name))

for dedup_name, files in dedup_name_files.items():
    url_list = []
    with open(dedup_name, "w") as writer:
        for file_name in files:
            url_list.extend(open(file_name))
        url_set = set(url_list)
        url_set = [url for url in url_set if not url.endswith("gif")]
        writer.writelines(url_set)



