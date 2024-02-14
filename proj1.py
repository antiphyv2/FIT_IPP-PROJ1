import sys
from xml.dom import minidom
import re

RETURN_OK = 0
RETURN_ARG_ERR = 10
RETURN_MISSING_HEADER = 21
RETURN_BAD_OPCODE = 22
RETURN_ERROR_OTHER = 23

def Remove_comments(line):
    line = line.split("#")[0].rstrip("\n")
    if line.isspace() or line == "":
        return line, True
    else:
        return line, False

def print_help():
    print("Tento skript nacita ze standardniho vstupu zdrojovy kod v IPPcode24,")
    print("zkontroluje spravnost kodu a vypise na standardni vystup XML reprezentaci programu.")

def header_check(line):
    line = line.rstrip(" \n")
    if(line != ".IPPcode24"):
        return False
    else:
        return True
    
def add_xml_instruction(line, op_order, xml_output, header):
    instruction = xml_output.createElement('instruction') 
    instruction.setAttribute('order', str(op_order)) 
    instruction.setAttribute('opcode', line) 
    header.appendChild(instruction)
    return instruction

def add_xml_argument(line, arg_number, xml_output, instruction, arg_type):
    #print("ARGTYPE:", arg_type, "TYPE")
    var_array = ['GF', 'LF', 'TF']
    
    if arg_type in var_array:
        arg_type = 'var'
    elif arg_type == 'bool':
        arg_type == 'bool'
    elif arg_type == 'int':
        arg_type == 'int'
    elif arg_type == 'string':
        arg_type == 'string'
    elif arg_type == 'nil':
        arg_type == 'nil'
    else:
        pass
    arg_w_number = f'arg{arg_number}'
    arg = xml_output.createElement(arg_w_number)
    arg.setAttribute('type', arg_type)
    arg_text = xml_output.createTextNode(line)
    arg.appendChild(arg_text)
    instruction.appendChild(arg)

def validate_regex(regex, argument, xml_output, inst_to_add_args, arg_number, inst):
    correct = re.match(regex, argument)
    if correct:
        line = correct.group(0).split('@')
        print("\n",line,"\n")
        arg_type = 'TYPE'
        add_xml_argument(argument, arg_number, xml_output, inst_to_add_args, arg_type)
    else:
        raise Other_exception(f'Nespravna syntaxe argumentu {arg_number} u instrukce {inst.show_opcode()}.')   

def handle_one_arg(inst, inst_to_add_args, argument, xml_output):
    
    list_one_arg_var = ['DEFVAR', 'POPS']
    list_one_arg_label = ['CALL', 'LABEL', 'JUMP']
    list_one_arg_symb = ['PUSHS', 'EXIT', 'DPRINT']

    if inst.show_opcode() in list_one_arg_var:
        regex = "(GF|LF|TF)@[_a-zA-Z][_a-zA-Z0-9$&%*!?-]*$"
        validate_regex(regex, argument, xml_output, inst_to_add_args, 1, inst)
        
    elif inst.show_opcode() in list_one_arg_label:
        regex = "[_a-zA-Z][_a-zA-Z0-9$&%*!?-]*$"
        validate_regex(regex, argument, xml_output, inst_to_add_args, 1, inst)  
        
    elif inst.show_opcode() in list_one_arg_symb:
        regex = "(bool@(true|false)$|int@-?(0o[0-7]+|0x[0-9a-fA-F]+|[0-9]+)$|nil@nil$|string@(.*))"
        validate_regex(regex, argument, xml_output, inst_to_add_args, 1, inst)
    #Opcode is write   
    else:
        regex = "(GF|LF|TF)@[A-Za-z_]+$|(bool@(true|false)$|int@-?(0o[0-7]+|0x[0-9a-fA-F]+|[0-9]+)$|nil@nil$|string@(.*))"
        validate_regex(regex, argument, xml_output, inst_to_add_args, 1, inst)
    
def handle_two_arg(inst, inst_to_add_args, argument1, argument2, xml_output):
    var_symb = ['MOVE', 'INT2CHAR', 'STRLEN', 'TYPE', 'NOT']
    arg1_regex = "(GF|LF|TF)@[_a-zA-Z][_a-zA-Z0-9$&%*!?-]*$"
    if inst.show_opcode() in var_symb:
        arg2_regex = "(bool@(true|false)$|int@-?(0o[0-7]+|0x[0-9a-fA-F]+|[0-9]+)$|nil@nil$|string@(.*))"
        validate_regex(arg1_regex, argument1, xml_output, inst_to_add_args, 1, inst)
        validate_regex(arg2_regex, argument2, xml_output, inst_to_add_args, 2, inst)
    #Opcode is Read <var,type>
    else:
        arg2_regex = "int$|bool$|string$"
        validate_regex(arg1_regex, argument1, xml_output, inst_to_add_args, 1, inst)
        validate_regex(arg2_regex, argument2, xml_output, inst_to_add_args, 2, inst)
    
def handle_three_arg(inst, inst_to_add_args, argument1, argument2, argument3, xml_output):
    var_regex = "(GF|LF|TF)@[_a-zA-Z][_a-zA-Z0-9$&%*!?-]*$"
    symb_regex = "(bool@(true|false)$|int@-?(0o[0-7]+|0x[0-9a-fA-F]+|[0-9]+)$|nil@nil$|string@(.*))"
    validate_regex(var_regex, argument1, xml_output, inst_to_add_args, 1, inst)
    validate_regex(symb_regex, argument2, xml_output, inst_to_add_args, 2, inst)
    validate_regex(symb_regex, argument3, xml_output, inst_to_add_args, 3, inst)


class Arg_exception(Exception):
    err_code = RETURN_ARG_ERR
    def __init__(self, err_message):
        self.err_message = err_message

class Header_exception(Exception):
    err_code = RETURN_MISSING_HEADER
    def __init__(self, err_message):
        self.err_message = err_message

class Opcode_exception(Exception):
    err_code = RETURN_BAD_OPCODE
    def __init__(self, err_message):
        self.err_message = err_message

class Other_exception(Exception):
    err_code = RETURN_ERROR_OTHER
    def __init__(self, err_message):
        self.err_message = err_message
    

class Instruction:

    def __init__(self, order, opcode, arg_count):
        self.order = order
        self.opcode = opcode
        self.arg_count = arg_count

    def show_opcode(self):
        return self.opcode

    def show_order(self):
        return self.order
    
    def show_arg_count(self):
        return self.arg_count

def main_func():
    arg_count = len(sys.argv)
    op_order = 0
    xml_output = minidom.Document()
    input_exists = False


    if arg_count > 2:
        print("Spatna kombinace argumentu")
        sys.exit(RETURN_ARG_ERR)

    if arg_count == 2:
        if sys.argv[1] == '--help':
            print_help()
            sys.exit(RETURN_OK)
        else:
            raise Arg_exception("Spatna kombinace argumentu.")

    for line in sys.stdin:
        input_exists = True

        line, Is_Comment = Remove_comments(line)

        #Skip empty line or comment line
        if(Is_Comment):
            continue

        if op_order == 0:
            header_valid = header_check(line)
            if not header_valid:
                raise Header_exception("Spatny format nebo chybejici hlavicka.")
            else:
                header = xml_output.createElement('program')
                header.setAttribute('language', 'IPPcode24') 
                xml_output.appendChild(header)
                op_order += 1
                continue
        
        #Delete empty strings after splitting by whitespace
        line = line.split(" ")
        support_line = []
        for part in line:
            if part.strip():
                support_line.append(part)
        line = support_line
        num_of_args = len(line) - 1
        line[0] = line[0].upper()

        if line[0] in inst_list_no_arg:
            inst = Instruction(op_order, line[0], 0)
            add_xml_instruction(line[0].upper(), op_order, xml_output, header)
                    
            if num_of_args != inst.show_arg_count():
                raise Other_exception(f'{inst.show_opcode()} nema zadne argumenty.')
            
        elif line[0] in inst_list_one_arg:
            inst = Instruction(op_order, line[0], 1)
            inst_to_add_args = add_xml_instruction(line[0], op_order, xml_output, header)

            if num_of_args != inst.show_arg_count():
                raise Other_exception(f'{inst.show_opcode()} ma pouze 1 argument.')
            
            handle_one_arg(inst, inst_to_add_args, line[1], xml_output)
            
        elif line[0] in inst_list_two_arg:    
            inst = Instruction(op_order, line[0], 2)
            inst_to_add_args = add_xml_instruction(line[0], op_order, xml_output, header)

            if num_of_args != inst.show_arg_count():
                raise Other_exception(f'{inst.show_opcode()} ma 2 argumenty.')
            
            handle_two_arg(inst, inst_to_add_args, line[1], line[2], xml_output)

        elif line[0] in inst_list_three_arg:    
            inst = Instruction(op_order, line[0], 3)
            inst_to_add_args = add_xml_instruction(line[0], op_order, xml_output, header)

            if num_of_args != inst.show_arg_count():
                raise Other_exception(f'{inst.show_opcode()} ma 3 argumenty.')
            
            handle_three_arg(inst, inst_to_add_args, line[1], line[2], line[3], xml_output)

        else:
            raise Opcode_exception("Spatny format nebo neexistujici instrukce.")

        print("Op counter:", op_order, "Line:", line)
        print(inst.show_opcode(), inst.show_order(), inst.show_arg_count())
        op_order += 1

    if not input_exists:
        raise Header_exception("Chybejici hlavicka")
    print(xml_output.toprettyxml(encoding="UTF-8").decode())

inst_list_no_arg = ['CREATEFRAME', 'PUSHFRAME', 'POPFRAME', 'RETURN', 'BREAK']
inst_list_one_arg = ['DEFVAR', 'CALL', 'PUSHS', 'POPS', 'WRITE', 'LABEL', 'JUMP', 'EXIT', 'DPRINT']
inst_list_two_arg = ['MOVE', 'READ', 'INT2CHAR', 'STRLEN', 'TYPE', 'NOT']
inst_list_three_arg = ['ADD', 'SUB', 'MUL', 'IDIV', 'LT', 'GT', 'EQ', 'AND', 'OR', 'STRI2INT', 'CONCAT', 'GETCHAR', 'SETCHAR', 'JUMPIFEQ', 'JUMPIFNEQ']

regex_backup = "(bool@(true|false)$|int@-?(0o[0-7]+|0x[0-9a-fA-F]+|[1-9][0-9]*|0)$|nil@nil$|string@(?:[^\\\x00-\x1F]|\\[0-9]{3})+$)"

if __name__ == "__main__":
    try:
        main_func()
    except Header_exception as he:
        print(he.err_message, file=sys.stderr)
        sys.exit(he.err_code)
    except Opcode_exception as ope:
        print(ope.err_message, file=sys.stderr)
        sys.exit(ope.err_code)
    except Other_exception as oe:
        print(oe.err_message, file=sys.stderr)
        sys.exit(oe.err_code)

    sys.exit(RETURN_OK)

