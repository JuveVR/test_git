# You have source_directory with nested directories (any level of nesting).
#
# In all those directories could be text files (with extension *.txt) and any other files.
#
# Create file combined_files.txt.
#
# For every text file in source_directory that smaller or equal to 120 bytes, add filename (without full path) and content to combined_files.txt

import os

my_garbage_bin = "/my/garbage/may"

# Create a file for appending
combined_file = open("combined_files.txt", "a")

# Iterate through my folder
for root, dirs, files in os.walk(my_garbage_bin):
    for my_file_name in files:
        file_address = os.path.join(root, my_file_name)
        # Check for text file and specified size
        if filename.endswith('.txt') and os.path.getsize(file_address) <= 120:
            my_file = open(file_address, "r")
            file_content = text_file.read()
            my_file.close()
            # Write files names and content in new file
            combined_file.write(f"Filename: {my_file_name }\nContent:\n{file_content}\n\n")

combined_file.close()

