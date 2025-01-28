import os

# Define the common directory (relative to the script location)
common_folder = os.path.dirname(os.path.abspath(__file__))  # Get the directory of the current script

parent_dir = os.path.dirname(common_folder)

# Define relative paths for the input files and output file
file1 = os.path.join(parent_dir, "generated/followers_output.txt")  # Followed users
file2 = os.path.join(parent_dir, "generated/following_output.txt")  # Following users
output_file = os.path.join(parent_dir, "generated/followers_difference_output.txt")  # Path for non-common elements

# Read the values from the first file (followers) into a list (preserving order)
import os

# Define the common directory (relative to the script location)
common_folder = os.path.dirname(os.path.abspath(__file__))  # Get the directory of the current script

parent_dir = os.path.dirname(common_folder)

# Define relative paths for the input files and output file
file1 = os.path.join(parent_dir, "generated/followers_output.txt")  # Followed users
file2 = os.path.join(parent_dir, "generated/following_output.txt")  # Following users
output_file = os.path.join(parent_dir, "generated/followers_difference_output.txt")  # Path for non-common elements

# Read the values from the first file (followers) into a list (preserving order)
with open(file1, "r") as f1:
    values1 = [line.strip() for line in f1]

# Read the values from the second file (following) into a list (preserving order)
with open(file2, "r") as f2:
    values2 = [line.strip() for line in f2]

# Find unique elements in the following file (only following, not followed)
only_following = [value for value in values2 if value not in values1]

# Find unique elements in the followers file (only followed, not following)
only_followed = [value for value in values1 if value not in values2]

# Sort both lists alphabetically
only_following.sort()
only_followed.sort()

# Write the unique elements to the output file in two blocks
with open(output_file, "w") as out_file:
    # Write Only Following block with the count of elements
    out_file.write(f"Only Following ({len(only_following)}):\n\n")
    if only_following:
        for value in only_following:
            out_file.write(value + "\n")
    else:
        out_file.write("Empty List\n")

    # Write Only Followed block with the count of elements
    out_file.write(f"\nOnly Followed ({len(only_followed)}):\n\n")
    if only_followed:
        for value in only_followed:
            out_file.write(value + "\n")
    else:
        out_file.write("Empty List\n")
