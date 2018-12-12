##############################################################################
# FILE : VMtranslator.py
# WRITER : Aviad Dudkewitz, Elkana Tovey
# DESCRIPTION: This program translate VM code to Hack assembly language.
##############################################################################
import sys
import re
from os import listdir
from os.path import isfile, isdir
from JackTokenizer import JackTokenizer

INVALID_ARGS = "The file given as input is invalid..."
NUMBER_OF_ARGS = 2
VM_SUFFIX = "\.vm$"
JACK_SUFFIX = ".jack"
VALID_INPUT_SUFFIX = ".*\.jack$"
JACK_SUFFIX_PATTERN = re.compile(VALID_INPUT_SUFFIX)
COMMENT = "//.*$"


def file_to_xml_lines(file_path):
    """
    Takes a jack file and translates all lines to XML markup language.
    :param file_path:  a string representing a the file path.
    :return: a list with all the translated lines.
    """
    result = []
    # function_name = DEFAULT_FUNCTION_NAME
    # return_address_index = 0
    with open(file_path, "r") as input_file:
        tokenObject = JackTokenizer(input_file)




        for line in input_file:
            line = re.sub(COMMENT, "", line)
            line_as_list = line.split()
            if len(line_as_list) > 0:
                if line_as_list[0] in ARITHMETIC_COMMAND:
                    temp_result = get_arithmetic_command_lines(line_as_list[0])
                    result += temp_result
                elif line_as_list[0] in MEMORY_ACCESS_COMMAND:
                    result += get_memory_command_lines(line_as_list[0],
                                                       line_as_list[1],
                                                       line_as_list[2],
                                                       file_path)
                elif line_as_list[0] in PROGRAM_FLOW_COMMAND:
                    result += get_program_flow_command_lines(line_as_list[0],
                                                             line_as_list[1],
                                                             function_name)
                elif line_as_list[0] in FUNCTION_CALLING_COMMAND:
                    if line_as_list[0] == "function":
                        function_name = line_as_list[1]
                        return_address_index = 0
                        result += get_function_declaration_lines(
                            function_name, int(line_as_list[2]))
                    elif line_as_list[0] == "call":
                        result += get_function_calling_lines(function_name,
                                                             return_address_index,
                                                             line_as_list[1],
                                                             int(line_as_list[2]))
                        return_address_index += 1
                    elif line_as_list[0] == "return":
                        result += get_function_return_lines()
    return result

def get_files(args):
    """
    :param args: the arguments given to the program.
    :return: the list of paths to .jack files
    """
    list_of_files_path = []
    if len(args) == NUMBER_OF_ARGS:
        if isfile(args[1]) and JACK_SUFFIX_PATTERN.match(args[1]):
            list_of_files_path.append(args[1])
        elif isdir(args[1]):
            for file in listdir(args[1]):
                if JACK_SUFFIX_PATTERN.match(file):
                    list_of_files_path.append(args[1] + "/" + file)
        return list_of_files_path
    else:
        print(INVALID_ARGS)
        exit()


def file_output_path(file_path):
    """
    :param file_path: The original file path
    :return: the path to the output file (.vm).
    """
    if isfile(file_path):
        return re.sub(JACK_SUFFIX, VM_SUFFIX, file_path)
    else:
        temp_path = re.sub("/$", "", file_path)
        temp_list = temp_path.split("/")
        return file_path + "/" + temp_list[len(temp_list) - 1] + VM_SUFFIX


def lines_list_to_file(file_path, lines_list):
    """
    :param file_path: path to the output file
    :param lines_list: a list of lines to save to the output file
    :return: None
    """
    with open(file_path, "w+") as output_file:
        for line in lines_list:
            output_file.write(line + "\n")


# The main program:
if __name__ == "__main__":
    comparison_counter = 0
    list_of_files_path = get_files(sys.argv)
    xml_lines_list = []
    for file_path in list_of_files_path:
        xml_lines_list = file_to_xml_lines(file_path)
        lines_list_to_file(file_output_path(sys.argv[1]), xml_lines_list)
