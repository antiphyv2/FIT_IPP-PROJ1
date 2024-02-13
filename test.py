from xml.dom import minidom
import sys


xml_output = minidom.Document()
header = xml_output.createElement('program')
header.setAttribute('language', 'IPPcode24') 
xml_output.appendChild(header)

instruction = xml_output.createElement('instruction') 
instruction.setAttribute('order', '1') 
instruction.setAttribute('opcode', 'DEFVAR') 
header.appendChild(instruction)

arg = xml_output.createElement('arg')
arg1_text = xml_output.createTextNode('GF@a')
arg.appendChild(arg1_text)
instruction.appendChild(arg)

arg2 = xml_output.createElement('arg2')
arg2.setAttribute('type', 'var')
instruction.appendChild(arg2)

instruction = xml_output.createElement('instruction') 
instruction.setAttribute('order', '0') 
instruction.setAttribute('opcode', 'BREAK') 
header.appendChild(instruction)

#arg = xml_output.createElement('arg')

print(xml_output.toprettyxml(encoding="UTF-8").decode())