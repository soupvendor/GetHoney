from config import working_dir as working_dir
from scan_all_files import scan_all_files
from process_data import process_data


if __name__ == "__main__":

    process_data(scan_all_files(working_dir))
