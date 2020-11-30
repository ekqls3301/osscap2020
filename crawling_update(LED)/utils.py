import csv
import json

import requests


def get_raw_data(url):
    with requests.Session() as s:
        download = s.get(url)
        decoded_content = download.content.decode("utf-8")
        data = list(csv.reader(decoded_content.splitlines(), delimiter=","))
        return data


def write_data(total_data, save_dir, crawler_name, var_name):
    with open(save_dir, "w", encoding="utf-8") as make_file:
        json.dump(total_data, make_file, ensure_ascii=False, indent=4)

    data = ""
    with open(save_dir, "r", encoding="utf-8") as f:
        line = f.readline()
        while line:
            data += line
            line = f.readline()

