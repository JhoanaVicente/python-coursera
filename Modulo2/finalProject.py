import re
import csv
from collections import defaultdict

# Initialize dictionaries
error_dict = defaultdict(int)
user_dict = defaultdict(lambda: {"INFO": 0, "ERROR": 0})

# Regular expressions to match log entries
error_pattern = r"ERROR: ([\w\s]+)"
info_pattern = r"INFO: ([\w\s]+)"

# Open and parse the syslog.log file
with open('syslog.log', 'r') as file:
    for line in file:
        if re.search(error_pattern, line):
            match = re.search(error_pattern, line)
            error_message = match.group(1)
            error_dict[error_message] += 1
            user = re.search(r"\(([\w]+)\)", line).group(1)
            user_dict[user]["ERROR"] += 1
        elif re.search(info_pattern, line):
            user = re.search(r"\(([\w]+)\)", line).group(1)
            user_dict[user]["INFO"] += 1

# Sort dictionaries
sorted_error_dict = sorted(error_dict.items(), key=lambda x: x[1], reverse=True)
sorted_user_dict = sorted(user_dict.items())

# Create error_message.csv
with open('error_message.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Error", "Count"])  # Add column names
    for error, count in sorted_error_dict:
        writer.writerow([error, count])

# Create user_statistics.csv
with open('user_statistics.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Username", "INFO", "ERROR"])  # Add column names
    for user, stats in sorted_user_dict:
        writer.writerow([user, stats['INFO'], stats['ERROR']])

print("Reports generated successfully.")
