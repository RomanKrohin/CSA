import re

machine_code = {}

def code_of_label(label: str) -> str:
    if labels.get(label)==None:
        labels[label]=hexcode(len(labels)+1)
        return labels[label]
    return labels[label]

def zero_arguments(arguments : []) -> []:
    return ["0000", "0000", "0000"]

def jmp_arguments(arguments : []) -> []:
    return [code_of_label(arguments[0]), "0000", "0000"]

def one_argument(arguments : []) -> []:
    return [hexcode(int(arguments[0])), "0000", "0000"]

def four_arguments(arguments : []) -> []:
    return [signes.get(arguments[0]), code_of_label(arguments[1]), code_of_label(arguments[2])]

labels = {
    "start": "0001"
}

labels_dyn=[]

signes = {
    ">": "1000",
    "=": "2000",
    "<": "3000",
}

commands = {
                 "add": {"code" : "a300" , "processor": one_argument}, 
                 "pop": {"code" : "b400" , "processor": zero_arguments}, 
                 "push": {"code" : "b500" , "processor": one_argument}, 
                 "jif": {"code" : "c680" , "processor": four_arguments}, 
                 "jmp": {"code" : "c600" , "processor": jmp_arguments},
                 "load": {"code" : "d700" , "processor": one_argument}}

dynamic_names = {}

def hexcode(number : int ) -> dict:
    hexadecimal = "{:04x}".format(number)
    return hexadecimal


def run(file) -> str:
    with open(file, "r") as f:
        prgrm = f.readlines()
        for line in prgrm:
            line_without_comments = str(re.sub(r'\$\$[\s\S]*\$\$','',line.strip()))
            string_without_newline_comments = str(re.sub(r'\n','',line_without_comments.strip()))
            if (string_without_newline_comments.strip()!=""):
                if (re.fullmatch(r"[\s\S]*\:", string_without_newline_comments)):
                    labels_dyn.append(string_without_newline_comments.replace(":", ""))
                    if labels.get(labels_dyn[-1])==None: 
                        labels[labels_dyn[-1]]=hexcode(len(labels)+1)
                    machine_code[labels.get(labels_dyn[-1])]=[]
                else:
                    machine_code.get(labels.get(labels_dyn[-1])).append(split_argument_command(string_without_newline_comments))
    return machine_code
                
                
                            
def split_argument_command(command_argument) -> str:
    command_argument_list = command_argument.split(" ")
    return (commands[command_argument_list[0]]["code"]+ " " + commands[command_argument_list[0]]["processor"](command_argument_list[1:])[0] + " "
            +commands[command_argument_list[0]]["processor"](command_argument_list[1:])[1]  + " "
            + commands[command_argument_list[0]]["processor"](command_argument_list[1:])[2]  )
