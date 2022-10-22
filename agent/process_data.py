from models import AgentData
from scan_all_files import scan_all_files
import os
from config import working_dir as working_dir


def process_data(data: dict) -> AgentData:
    u_ips = len(data.keys())
    # total_connections: int = sum(data.values())
    dir_size = len(os.listdir(working_dir))
    payload = AgentData(unique_ips=u_ips, scanned_files=dir_size)

    return print(payload)


process_data(scan_all_files(working_dir))
