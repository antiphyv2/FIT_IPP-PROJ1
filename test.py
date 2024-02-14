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
regex_pattern = r'\\[0-9]{3}$'

# Test string
test_string = "\123"

# Check if the test string matches the regex pattern
if re.match(regex_pattern, test_string):
    print("The string matches the pattern.")
else:
    print("The string does not match the pattern.")