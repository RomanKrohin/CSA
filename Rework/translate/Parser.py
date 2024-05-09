import re


variables = {   
}

labels = {
    "start": '0x1'
}

labels_dyn=[]

signes = {
    ">": '0x3e8',
    "=": '0x7d0',
    "<": '0xbb8',
}

dynamic_names = {}

machine_code = {}

def code_of_label(label: str) -> str:
    if labels.get(label)==None:
        labels[label]=hex(len(labels)+1)
        return labels[label]
    return labels[label]

def zero_arguments(arguments : []) -> []:
    return [hex(0), hex(0), hex(0)]

def jmp_arguments(arguments : []) -> []:
    return [code_of_label(arguments[0]), hex(0), hex(0)]

def one_argument(arguments : []) -> []:
    return [hex(int(arguments[0])), hex(0), hex(0)]

def var_or_int_argument(arguments : []) -> []:
    if (re.match(r"\d+", arguments[0])):
        return [hex(int(arguments[0])), hex(0), hex(0)]
    return [variables[arguments[0]], hex(1), hex(0)]

def set_var_argument(arguments : []) -> []:
    variables[arguments[0]] = hex(len(variables.keys())*40)
    i=0
    
    if (not re.match(r"\d+", " ".join(arguments[1:]))):
        for c in str(" ".join(arguments[1:])):
            machine_code.get(labels.get(labels_dyn[-1])).append(['0x420', hex((len(variables.keys())-1)*40+i), hex(ord(c)), hex(1)])
            i+=1
            
        return [hex((len(variables.keys())-1)*40+i), hex(ord("\0")), hex(2)]
    else:
        return [hex((len(variables.keys())-1)*40), hex(int(arguments[1])), hex(3)]

def var_argument(arguments : []) -> []:
    return [variables.get(arguments[0]), hex(0), hex(0)]

def print_argument(arguments : []) -> []:
    if (variables.get(arguments[0]) == None):
        for c in " ".join(arguments[0:]):
            machine_code.get(labels.get(labels_dyn[-1])).append(['0x290', hex(ord(c)), hex(1), hex(0)])
        return [hex(ord("\0")), hex(2), hex(0)]
    else:
        return [variables.get(arguments[0]), hex(0), hex(3)]


def four_arguments(arguments : []) -> []:
    return [signes.get(arguments[0]), hex(int(arguments[1])), code_of_label(arguments[2])]

commands = {
        "add": {"code" : '0x64' , "processor": one_argument}, 
        "pop": {"code" : '0xc8' , "processor": zero_arguments}, 
        "push": {"code" : '0x12c' , "processor": var_or_int_argument}, 
        "load": {"code" : '0x520' , "processor": var_argument}, 
        "jif": {"code" : '0x190' , "processor": four_arguments}, 
        "jmp": {"code" : '0x2bc' , "processor": jmp_arguments},
        "print": {"code" : '0x290' , "processor": print_argument},
        "set_var": {"code" : '0x420' , "processor": set_var_argument},
        }


def remove_all_comments(string_with_comments: str) -> str:
    return str(re.sub(r'\$\$[\s\S]*\$\$','',string_with_comments.strip()))

def remove_all_newline(string_with_newline: str) -> str:
    return str(re.sub(r'\n','',string_with_newline.strip()))

def validate_label(string_without_newline_comments: str) -> None:
    patterns = [".", "@", " "]
    labels_dyn.append((string_without_newline_comments.replace(":", "")).replace("@ ", "").strip())
    assert all(substring not in labels_dyn[-1] for substring in patterns) and not labels_dyn[-1].isnumeric(), "Плохой лейбл"
    if labels.get(labels_dyn[-1])==None: 
        labels[labels_dyn[-1]]=hex(len(labels)+1)

def run(file: str) -> str:
    with open(file, "r") as f:
        prgrm = f.readlines()
        for line in prgrm:
            string_without_newline_comments = remove_all_newline(remove_all_comments(line))
            if (string_without_newline_comments.strip()!=""):
                if (re.fullmatch(r"@ [\s\S]*\:", string_without_newline_comments)):
                    validate_label(string_without_newline_comments)
                    machine_code[labels.get(labels_dyn[-1])]=[]
                else:
                    machine_code.get(labels.get(labels_dyn[-1])).append(split_argument_command(string_without_newline_comments))
    return machine_code
                                         
def split_argument_command(command_argument) -> []:
    command_argument_list = command_argument.split(" ")
    processor_result = commands[command_argument_list[0]]["processor"](command_argument_list[1:])
    return ([commands[command_argument_list[0]]["code"], 
            processor_result[0],
            processor_result[1],
            processor_result[2]])
    