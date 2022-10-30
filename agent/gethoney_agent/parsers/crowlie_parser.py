from abc import abstractmethod

from gethoney_agent.models import AgentData
from gethoney_agent.parsers.template import AbstractParser


class CrowlieParser(AbstractParser):
    @abstractmethod
    def read_logs(self) -> dict:
        pass

    @abstractmethod
    def parse(self) -> AgentData:
        pass

    @abstractmethod
    def run(self) -> None:
        print("hello")
