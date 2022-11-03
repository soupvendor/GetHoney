from sys import argv

from gethoney_agent.parsers.agent import Agent

if __name__ == "__main__":

    agent = Agent(argv[1], argv[2])

    if agent:
        print(f"{agent.name} is running...")
        agent.parser.run()
