# You have source_directory with nested directories (any level of nesting).
#
# In all those directories could be text files (with extension *.txt) and any other files.
#
# Create file combined_files.txt.
#
# For every text file in source_directory that smaller or equal to 120 bytes, add filename (without full path) and content to combined_files.txt

import os

my_garbage_bin = "/Users/vadymr/python_project/python_lerning/Lesson_6_homework"

# Create a file for appending
with open("combined_file_123.txt", "a") as combined_file:
    # Iterate through my folder
    for root, dirs, files in os.walk(my_garbage_bin):
        for my_file_name in files:
            file_address = os.path.join(root, my_file_name)
            # Check for text file and specified size
            if my_file_name.endswith('.txt') and os.path.getsize(file_address) <= 120:
                with open(file_address, "r") as my_file:
                    file_content = my_file.read()
                # Write files names and content in new file
                combined_file.write(f"Filename: {my_file_name }\nContent:\n{file_content}\n\n")