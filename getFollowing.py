import json
import os

# Define the common directory (relative to the script location)
common_folder = os.path.dirname(os.path.abspath(__file__))  # Get the directory of the current script

parent_dir = os.path.dirname(common_folder)

# Define relative paths for the input JSON file and output text file
input_file = os.path.join(parent_dir, "data/following.json")  # Input JSON file
output_file = os.path.join(parent_dir, "generated/following_output.txt")  # Output text file

# Ensure the output directory exists
output_dir = os.path.dirname(output_file)
os.makedirs(output_dir, exist_ok=True)  # Create the directory if it doesn't exist

# Load JSON data from the specified file
with open(input_file, "r") as file:
    data = json.load(file)

# Extracting values from "relationships_following" -> "string_list_data"
values = []
for entry in data.get("relationships_following", []):
    for sub_entry in entry.get("string_list_data", []):
        values.append(sub_entry["value"])  # Extracting "value" from each sub-entry

# Save the output to the custom file path
with open(output_file, "w") as file:
    for value in values:
        file.write(value + "\n")  # Write each value on a new line

