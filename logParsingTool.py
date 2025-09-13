import re
log_file = r"C:\Users\Dell\OneDrive\Documents\log_file.log"
with open(log_file, 'r') as f:

    # Define the regex pattern to match the log entries
    regex_pattern = r'(\d+\/\d+\s\d+:\d+:\d+)\s(\w+)\s+:......(\w+:\s\w+:\s+\w+)'
    for(line) in f:
        match = re.search(regex_pattern, line)
        if match:
            timestamp = match.group(1)
            log_level = match.group(2)
            massege = match.group(3)

            print(f'{timestamp} _ {log_level} _ {massege}')
        
