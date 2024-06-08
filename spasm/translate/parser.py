import re

variables = {
}

labels = {
}

labels_dyn=[]

dynamic_names = {}

machine_code = []

def zero_arguments(arguments : []) -> []:
    return [(0), (0)]

def jmp_arguments(arguments : []) -> []:
    if (labels.get(arguments[0]) is None):
        return [arguments[0], (0)]
    return [labels[arguments[0]], (0)]

def one_argument(arguments : []) -> []:
    return [(int(arguments[0])), (0)]

def var_or_int_argument(arguments : []) -> []:
    if (re.match(r"\d+", arguments[0])):
        return [(int(arguments[0])), (0)]
    return [variables[arguments[0]], (1)]

def set_var_argument(arguments : [], memory_pointer: int) -> []:
    variables[arguments[0]] = (memory_pointer)
    i=0
    tmp=[]
    if (not re.match(r"\d+", " ".join(arguments[1:]))):
        for c in str(" ".join(arguments[1:])):
            i+=1
            tmp.append(["INIT", (int(variables[arguments[0]])+i), (ord(c))])
            memory_pointer+=1
        machine_code.append(["INIT", (int(variables[arguments[0]])), (i)])
        memory_pointer+=1
        for comm in tmp:
            machine_code.append(comm)
        return memory_pointer
    machine_code.append( ["INIT",(int(variables[arguments[0]])), (int(arguments[1]))])
    memory_pointer+=1
    return memory_pointer

def var_argument(arguments : []) -> []:
    return [variables.get(arguments[0]), (0)]

def print_argument(arguments : []) -> []:
    if (variables.get(arguments[0]) is not None):
        return [variables.get(arguments[0]), (0)]
    return [(0), (0)]

commands = {
        "add": {"code" : "ADD" , "processor": zero_arguments},
        "pop": {"code" : "POP" , "processor": zero_arguments},
        "push": {"code" : "PUSH" , "processor": var_or_int_argument},
        "load": {"code" : "LOAD" , "processor": var_argument},
        "incr": {"code" : "INCR" , "processor": zero_arguments},
        "decr": {"code" : "DECR" , "processor": zero_arguments},
        "hlt": {"code" : "HLT" , "processor": zero_arguments},
        "jmp": {"code" : "JMP" , "processor": jmp_arguments},
        "jeq": {"code" : "JEQ" , "processor": jmp_arguments},
        "jne": {"code" : "JNE" , "processor": jmp_arguments},
        "jla": {"code" : "JLA" , "processor": jmp_arguments},
        "jle": {"code" : "JLE" , "processor": jmp_arguments},
        "print": {"code" : "PRINT" , "processor": zero_arguments},
        "read": {"code" : "READ" , "processor": zero_arguments},
        "sub": {"code" : "SUB" , "processor": zero_arguments},
        "div": {"code" : "DIV" , "processor": zero_arguments},
        "mul": {"code" : "MUL" , "processor": zero_arguments},
        "adr": {"code" : "ADR" , "processor": var_argument},
        "push_by_adr": {"code" : "PADR" , "processor": zero_arguments},
        "load_by_adr": {"code" : "LADR" , "processor": zero_arguments},
        "mod": {"code" : "MOD" , "processor": var_or_int_argument},
        }


def remove_all_comments(string_with_comments: str) -> str:
    return str(re.sub(r"\$\$[\s\S]*\$\$","",string_with_comments.strip()))

def remove_all_newline(string_with_newline: str) -> str:
    return str(re.sub(r"\n","",string_with_newline.strip()))

def validate_label(string_without_newline_comments: str, machine_code: []) -> None:
    patterns = [".", "@", " "]
    labels_dyn.append((string_without_newline_comments.replace(":", "")).replace("@ ", "").strip())
    assert all(substring not in labels_dyn[-1] for substring in patterns) and not labels_dyn[-1].isnumeric(), "Плохой лейбл"
    if labels.get(labels_dyn[-1]) is None:
        labels[labels_dyn[-1]]=(len(machine_code)+1)
    for command in machine_code:
        if (command[1]==labels_dyn[-1]):
            command[1] = labels[labels_dyn[-1]]

def run(file: str) -> str:
    data_flag = False
    with open(file) as f:
        memory_pointer=0
        prgrm = f.readlines()
        for line in prgrm:
            string_without_newline_comments = remove_all_newline(remove_all_comments(line))
            if (string_without_newline_comments.strip()=="_data"):
                data_flag=True
            if (string_without_newline_comments.strip()=="_programme"):
                data_flag=False
                if (labels.get("start") is None):
                    machine_code.append(["JMP", "start", 0])
                else:
                    machine_code.append(["JMP", labels["start"], 0])
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
            processor_result[1]])
    
def reset_globals() -> None:
    global variables, labels, labels_dyn, dynamic_names, machine_code
    variables = {}
    labels = {}
    labels_dyn = []
    dynamic_names = {}
    machine_code = []
