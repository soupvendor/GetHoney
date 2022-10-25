import json
import os
import re

from config import working_dir

# def scan_all_files(dir: str) -> dict:
#     files = os.listdir(dir)
#     valid_ips = {}
#     pattern = re.compile("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")

#     for file in files:
#         with open(f"./test-files/{file}", "r") as open_file:
#             fstring = open_file.readlines()

#         for line in fstring:
#             ip = re.findall(pattern, line)
#             if ip:
#                 if ip[0] in valid_ips.keys():
#                     valid_ips[ip[0]] += 1
#                 else:
#                     valid_ips[ip[0]] = 1
#     return valid_ips


def scan_all_files(dir: str) -> dict:
    files = os.listdir(dir)
    unique_ips = []
    all_keys = []
    # pattern = re.compile("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")

    for file in files:
        with open(f"./test-files/{file}", "r") as open_file:
            fstring = open_file.readlines()

        for line in fstring:
            data = json.loads(line)
            for key in data.keys():
                if key not in all_keys:
                    all_keys.append(key)
    print(all_keys)


scan_all_files(working_dir)
