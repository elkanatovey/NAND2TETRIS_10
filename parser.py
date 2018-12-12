##############################################################################
# FILE : VMtranslator.py
# WRITER : Aviad Dudkewitz, Elkana Tovey
# DESCRIPTION: This program translate VM code to Hack assembly language.
##############################################################################
import sys
import re
from os import listdir
from os.path import isfile, isdir

INVALID_ARGS = "The file given as input is invalid..."
NUMBER_OF_ARGS = 2
VM_SUFFIX = "\.vm$"
JACK_SUFFIX = ".jack"
VALID_INPUT_SUFFIX = ".*\.jack$"
jack_suffix_pattern = re.compile(VALID_INPUT_SUFFIX)



def get_files(args):
    """
    :param args: the arguments given to the program.
    :return: the list of paths to .jack files
    """
    list_of_files_path = []
    if len(args) == NUMBER_OF_ARGS:
        if isfile(args[1]) and jack_suffix_pattern.match(args[1]):
            list_of_files_path.append(args[1])
        elif isdir(args[1]):
            for file in listdir(args[1]):
                if jack_suffix_pattern.match(file):
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
