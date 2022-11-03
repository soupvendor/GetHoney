import json
import os
import time

from gethoney_agent.config import working_dir
from gethoney_agent.models import AgentData
from gethoney_agent.parsers.template import AbstractParser


class CrowlieParser(AbstractParser):
    def __init__(self):
        self.directory = working_dir

    def _parse(self) -> AgentData:
        files = os.listdir(self.directory)
        unique_ips: list = []
        total_list: dict = {}
        total: int = 0

        for file in files:
            with open(f"{self.directory}/{file}", "r") as open_file:
                fstring = open_file.readlines()
            total_connections = 0
            for line in fstring:
                data = json.loads(line)
                if data["eventid"] == "cowrie.session.connect":
                    total_connections += 1
                    if data["src_ip"] not in unique_ips:
                        unique_ips.append(data["src_ip"])
            total_list[file] = {"unique_ips": unique_ips, "total_connections": total_connections}

        for file in total_list:
            total += int(total_list[file]["total_connections"])
        payload = AgentData(files_scanned=list(total_list.keys()), total_connections=total)

        return payload

    def run(self) -> None:
        while True:
            print(self._parse())
            time.sleep(5)
