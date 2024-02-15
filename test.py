# from xml.dom import minidom
# import sys


# xml_output = minidom.Document()
# header = xml_output.createElement('program')
# header.setAttribute('language', 'IPPcode24') 
# xml_output.appendChild(header)

# instruction = xml_output.createElement('instruction') 
# instruction.setAttribute('order', '1') 
# instruction.setAttribute('opcode', 'DEFVAR') 
# header.appendChild(instruction)

# arg = xml_output.createElement('arg')
# arg1_text = xml_output.createTextNode('GF@a')
# arg.appendChild(arg1_text)
# instruction.appendChild(arg)

# arg2 = xml_output.createElement('arg2')
# arg2.setAttribute('type', 'var')
# instruction.appendChild(arg2)

# instruction = xml_output.createElement('instruction') 
# instruction.setAttribute('order', '0') 
# instruction.setAttribute('opcode', 'BREAK') 
# header.appendChild(instruction)

# #arg = xml_output.createElement('arg')

# print(xml_output.toprettyxml(encoding="UTF-8").decode())
import re

# Regular expression to match all characters with \ followed by exactly 3 numbers
# regex_pattern = r'\\[0-9]{3}$'

# # Test string
# test_string = "\123"

# # Check if the test string matches the regex pattern
# if re.match(regex_pattern, test_string):
#     print("The string matches the pattern.")
# else:
#     print("The string does not match the pattern.")


# Define your string
my_string = r'\111He\126llo\111w091howareyou'
print(my_string)
modified_string = my_string.replace("\\", "\\\\")
print(modified_string)

# regex_pattern = r'([^\\]*)(\\[0-9]{3})'
# #regex_pattern = r'\\[0-9]{3}$'

# # Check if the test string matches the regex pattern
# matches = re.findall(regex_pattern, modified_string)

# if matches:
#     for match in matches:
#         print(match)
#     print("All backslashes in the string are followed by exactly three numbers.")
# else:
#     print("There is a backslash in the string that is not followed by exactly three numbers.")

# Define a regular expression pattern
pattern = "((\\\\{1}[0-9]{3})(?![0-9]))"

# Find all matches of the pattern in the string
matches = re.findall(pattern, my_string)

# Count the number of backslashes in the string
backslash_count = my_string.count('\\')

if len(matches) == backslash_count:
    for match in matches:
        print(match[1])  # Printing only the part that matches the backslash and three numbers
    print("All occurrences of backslashes in the string are followed by exactly three numbers.")
else:
    print("There is a backslash in the string that is not followed by exactly three numbers.")

modified_string = modified_string.replace("\\\\", "\\")
print(modified_string)

# Define a regular expression pattern
# pattern = r"\\[0-9]{3}"

# # Find all matches of the pattern in the string
# matches = re.findall(pattern, modified_string)

# # Check if all matches are found
# if len(matches) == len(re.findall(r"\\", modified_string)):
#     print("All backslashes are followed by exactly three numbers.")
# else:
#     print("There is a backslash that is not followed by exactly three numbers.")