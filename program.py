import subprocess
import os

# Define the common directory (relative to the script location)
common_folder = os.path.dirname(os.path.abspath(__file__))  # Get the directory of the current script

# Paths to the individual scripts
followers_script = os.path.join(common_folder, "scripts/getFollowers.py")  # Script for processing followers
following_script = os.path.join(common_folder, "scripts/getFollowing.py")  # Script for processing following
difference_script = os.path.join(common_folder, "scripts/getDifference.py")  # Script for calculating the difference

# Function to run a script
def run_script(script_path):
    try:
        subprocess.run(["python", script_path], check=True)  # Run the script
    except subprocess.CalledProcessError as e:
        print(f"Error running {script_path}: {e}")

# Run the scripts sequentially
run_script(followers_script)
run_script(following_script)
run_script(difference_script)

# Define the output file path
output_file = os.path.join(common_folder, "generated", "followers_difference_output.txt")

# Check if the file exists before attempting to open it
if os.path.exists(output_file):
    # Open and read the file
    with open(output_file, "r") as file:
        content = file.read()
        print(content)  # Print the content of the file
else:
    print(f"Error: The file {output_file} does not exist.")

# Add this line to prevent the command window from closing immediately
input("Press Enter to exit...")
