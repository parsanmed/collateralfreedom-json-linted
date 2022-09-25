import os
import re
import json
from collections import defaultdict
import urllib.request


PER_SITES_PATTERN = r"\"(?P<original>\S+)\": \[\s+\"(?P<mirror>\S+)\"\s+\],?"
SITES_URI = "https://raw.githubusercontent.com/RSF-RWB/collateralfreedom/main/sites.json"



def get_original_sites_str():
    with urllib.request.urlopen(SITES_URI) as res:
        return res.read().decode(res.headers.get_content_charset("utf-8"))
    

def get_dict_from_sites_str(content):
    all_re = re.findall(PER_SITES_PATTERN, content)
    res = defaultdict(list)
    for original, mirror in all_re:
        res[original].append(mirror)
    return res

def save_sites_to_json(sites_dict):
    with open("sites.json", mode="w+") as f:
        json.dump(sites_dict, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    sites_str = get_original_sites_str()
    if not sites_str:
        exit(-1)
    sites_dict = get_dict_from_sites_str(sites_str)
    save_sites_to_json(sites_dict)
