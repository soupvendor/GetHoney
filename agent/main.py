from config import working_dir as working_dir
from find_ips import ip_scan as ip_scan

if __name__ == "__main__":

    def process_data(data: dict):
        unique_ips = len(data.keys())
        total_connections: int = sum(data.values())
        
        print(f"Number unique connections: {unique_ips}")
        print(f"Total number of connections: {total_connections}")

    data = ip_scan(working_dir)
    process_data(data)
