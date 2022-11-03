from gethoney_agent.parsers.crowlie_parser import CrowlieParser


class Agent:
    def __init__(self, name: str, parser: str) -> None:
        agent_map = {"crowlie": CrowlieParser}
        self.name = name
        self.parser = agent_map[parser]()
