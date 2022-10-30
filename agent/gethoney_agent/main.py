from gethoney_agent.config import working_dir
from gethoney_agent.process_data import process_data
from gethoney_agent.scan_all_files import scan_all_files

if __name__ == "__main__":

    process_data(scan_all_files(working_dir))
