from models import AgentData
from scan_all_files import scan_all_files
import os
from config import working_dir as working_dir


def process_data(data: dict) -> AgentData:
    total = 0
    for file in data:
        total += data[file]["total_connections"]
    payload = AgentData(files_scanned=list(data.keys()), total_connections=total)
    
    return payload

print(process_data(scan_all_files(working_dir)))
