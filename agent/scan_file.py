import re


def scan_file(dir: str, file: str) -> dict:
    valid_ips = {}
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
    return valid_ips
