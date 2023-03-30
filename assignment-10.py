import os

input_file_path = os.path.abspath('input_file.txt')
output_file_path = os.path.abspath('output_file.txt')

with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:

    # Read the contents of the input file
    contents = input_file.read()
    
    # Write the contents to the output file
    output_file.write(contents)
    
print("File copy successful!")
