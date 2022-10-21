import os
import re


def ip_scan(dir: str) -> dict:
    files = os.listdir(dir)
    valid_ips = {}
    ip_in_file = []
    for file in files:
        pattern = re.compile("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
        with open(f"./test-files/{file}", "r") as open_file:
            fstring = open_file.readlines()

        for line in fstring:
            ip = re.findall(pattern, line)
            if ip:
                if ip[0] in valid_ips.keys():
                    valid_ips[ip[0]] += 1
                else:
                    valid_ips[ip[0]] = 1
                    ip_in_file.append(file)
    # zip_list = zip(valid_ips, ip_in_file)
    # return print(list(zip_list))
    return valid_ips
