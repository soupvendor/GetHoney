from abc import abstractmethod


class AbstractParser:
    def __init__(self, directory: str) -> None:
        self.directory = directory

    @abstractmethod
    def run(self) -> None:
        pass
