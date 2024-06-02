import re

variables = {   
}

labels = {
}

labels_dyn=[]

dynamic_names = {}

machine_code = []

def zero_arguments(arguments : []) -> []:
    return [hex(0), hex(0), hex(0)]

def jmp_arguments(arguments : []) -> []:
    if (labels.get(arguments[0])==None):
        return [arguments[0], hex(0), hex(0)]
    return [labels[arguments[0]], hex(0), hex(0)]

def one_argument(arguments : []) -> []:
    return [hex(int(arguments[0])), hex(0), hex(0)]

def var_or_int_argument(arguments : []) -> []:
    if (re.match(r"\d+", arguments[0])):
        return [hex(int(arguments[0])), hex(0), hex(0)]
    return [variables[arguments[0]], hex(1), hex(0)]

def set_var_argument(arguments : [], memory_pointer: int) -> []:
    variables[arguments[0]] = hex(memory_pointer)
    i=0
    tmp=[]
    if (not re.match(r"\d+", " ".join(arguments[1:]))):
        for c in str(" ".join(arguments[1:])):
            i+=1
            tmp.append(['0x420', hex((int(variables[arguments[0]], 16)+memory_pointer)), hex(ord(c)), hex(0)])
            memory_pointer+=1
        machine_code.append(['0x420', hex((int(variables[arguments[0]], 16))), hex(i), hex(0)])
        memory_pointer+=1
        for comm in tmp:
            machine_code.append(comm)
        return memory_pointer
    else:
        machine_code.append( ['0x420',hex(int(variables[arguments[0]], 16)), hex(int(arguments[1])), hex(0)])
        memory_pointer+=1
        return memory_pointer

def var_argument(arguments : []) -> []:
    return [variables.get(arguments[0]), hex(0), hex(0)]

def print_argument(arguments : []) -> []:
    if (variables.get(arguments[0]) != None):
        return [variables.get(arguments[0]), hex(0), hex(3)]

commands = {
        "add": {"code" : '0x64' , "processor": var_or_int_argument}, 
        "pop": {"code" : '0xc8' , "processor": zero_arguments}, 
        "push": {"code" : '0x12c' , "processor": var_or_int_argument}, 
        "load": {"code" : '0x520' , "processor": var_argument},
        "incr": {"code" : '0x630' , "processor": zero_arguments}, 
        "decr": {"code" : '0x530' , "processor": zero_arguments},
        "hlt": {"code" : '0x1' , "processor": zero_arguments}, 
        "jmp": {"code" : '0x2bc' , "processor": jmp_arguments},
        "jeq": {"code" : '0x3bc' , "processor": jmp_arguments},
        "jne": {"code" : '0x4bc' , "processor": jmp_arguments},
        "jla": {"code" : '0x5bc' , "processor": jmp_arguments},
        "jle": {"code" : '0x5bc' , "processor": jmp_arguments},
        "print": {"code" : '0x290' , "processor": print_argument},
        "read": {"code" : '0x390' , "processor": print_argument},
        "sub": {"code" : '0x74' , "processor": var_or_int_argument},
        "div": {"code" : '0x84' , "processor": var_or_int_argument},
        "mul": {"code" : '0x94' , "processor": var_or_int_argument},
        "adr": {"code" : '0x12c' , "processor": var_argument},
        "push_by_adr": {"code" : '0x44' , "processor": zero_arguments},
        "load_by_adr": {"code" : '0x48' , "processor": zero_arguments},
        }


def remove_all_comments(string_with_comments: str) -> str:
    return str(re.sub(r'\$\$[\s\S]*\$\$','',string_with_comments.strip()))

def remove_all_newline(string_with_newline: str) -> str:
    return str(re.sub(r'\n','',string_with_newline.strip()))

def validate_label(string_without_newline_comments: str, machine_code: []) -> None:
    patterns = [".", "@", " "]
    labels_dyn.append((string_without_newline_comments.replace(":", "")).replace("@ ", "").strip())
    assert all(substring not in labels_dyn[-1] for substring in patterns) and not labels_dyn[-1].isnumeric(), "Плохой лейбл"
    if labels.get(labels_dyn[-1])==None: 
        labels[labels_dyn[-1]]=hex(len(machine_code)+1)
    for command in machine_code:
        if (command[1]==labels_dyn[-1]):
            command[1] = labels[labels_dyn[-1]]

def run(file: str) -> str:
    data_flag = False
    with open(file, "r") as f:
        memory_pointer=0
        prgrm = f.readlines()
        for line in prgrm:
            string_without_newline_comments = remove_all_newline(remove_all_comments(line))
            if (string_without_newline_comments.strip()=="_data"):
                data_flag=True
            if (string_without_newline_comments.strip()=="_programme"):
                data_flag=False
                if (labels.get("start")==None):
                    machine_code.append(['0x2bc', "start", '0x0', '0x0'])
                else:
                    machine_code.append(['0x2bc', labels["start"], '0x0', '0x0'])
            if (string_without_newline_comments.strip()!="" and not re.fullmatch(r"_[\s\S]*", string_without_newline_comments)):
                if (not data_flag):    
                    if (re.fullmatch(r"@ [\s\S]*\:", string_without_newline_comments)):
                        validate_label(string_without_newline_comments, machine_code)
                    else:
                        machine_code.append(split_argument_command(string_without_newline_comments))
                else:
                    memory_pointer= set_var_argument(string_without_newline_comments.replace("=","").replace("  "," ").split(" "), memory_pointer)
    return machine_code
                                         
def split_argument_command(command_argument) -> []:
    command_argument_list = command_argument.split(" ")
    processor_result = commands[command_argument_list[0]]["processor"](command_argument_list[1:])
    return ([commands[command_argument_list[0]]["code"], 
            processor_result[0],
            processor_result[1],
            processor_result[2]])
    