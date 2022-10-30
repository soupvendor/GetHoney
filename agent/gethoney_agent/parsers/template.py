from abc import abstractmethod

from agent.models import AgentData


class AbstractParser:
    def __init__(self, name: str, parser: str) -> None:
        self.name = name
        self.parser = parser

    @abstractmethod
    def read_logs(self) -> dict:
        pass

    @abstractmethod
    def parse(self) -> AgentData:
        pass

    @abstractmethod
    def run(self) -> None:
        pass

    def send_data(self) -> None:
        pass
