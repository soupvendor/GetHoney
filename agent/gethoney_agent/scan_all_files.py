import json
import os

from config import working_dir


def scan_all_files(directory: str) -> dict:
    files = os.listdir(directory)
    unique_ips = []
    total_list = {}

    for file in files:
        with open(f"./test-files/{file}", "r") as open_file:
            fstring = open_file.readlines()
        total_connections = 0
        for line in fstring:
            print(file)
            data = json.loads(line)
            if data["eventid"] == "cowrie.session.connect":
                total_connections += 1
                if data["src_ip"] not in unique_ips:
                    unique_ips.append(data["src_ip"])
        total_list[file] = {"unique_ips": unique_ips, "total_connections": total_connections}
    return total_list


scan_all_files(working_dir)
