import csv, re, os, glob, argparse

def parse_log_file(filepath):
    logs = []
    regex_pattern = r'(\d{1,2}/\d{1,2}\s\d{1,2}:\d{2}:\d{2})\s+(\w+)\s*:\s*(.*)'

    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            match = re.search(regex_pattern, line)
            if match:
                timestamp = match.group(1)
                log_level = match.group(2)
                message = match.group(3)

                print(f'{timestamp} _ {log_level} _ {message}')
                ip_match = re.search(r'(\d+\.\d+\.\d+\.\d+)', message)
                status_match = re.search(r'status:\s(\w+)', message, re.IGNORECASE)
                ip = ip_match.group(1) if ip_match else ""
                status = status_match.group(1) if status_match else ""
                logs.append({"timestamp": timestamp, "ip": ip, "status": status})
        if logs:
            file_exists = os.path.isfile("parsed_logs.csv")
            with open("parsed_logs.csv", "a", newline="") as f:
                csv_writer = csv.DictWriter(f, fieldnames=["timestamp", "ip", "status"])
                if not file_exists:
                    csv_writer.writeheader()
                csv_writer.writerows(logs)
            print(f"Logs from {os.path.basename(filepath)} saved to parsed_logs.csv") 
    
    if __name__ == "__main__":
        parser = argparse.ArgumentParser(description="Parse all log files in a directory.")
        parser.add_argument("directory", help="Path to the directory containing log files")
        args = parser.parse_args()
        print(f"Folder path received: {args.directory}")
    
    log_files = glob.glob(os.path.join(args.directory, "*.txt")) + glob.glob(os.path.join(args.directory, "*.log"))
    if not log_files:
        print("No log files found in the specified directory.")
        exit(0)
    for filepath in log_files:

            parse_log_file(filepath)
