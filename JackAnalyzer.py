##############################################################################
# FILE : VMtranslator.py
# WRITER : Aviad Dudkewitz, Elkana Tovey
# DESCRIPTION: This program translate VM code to Hack assembly language.
##############################################################################
import sys
import re
from os import listdir
from os.path import isfile, isdir
from CompilationEngine import CompilationEngine

INVALID_ARGS = "The file given as input is invalid..."
NUMBER_OF_ARGS = 2
VM_SUFFIX = ".vm$"
JACK_SUFFIX = ".jack"
VALID_INPUT_SUFFIX = ".*\.jack$"
JACK_SUFFIX_PATTERN = re.compile(VALID_INPUT_SUFFIX)
COMMENT = "//.*$"

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

# The main program:
if __name__ == "__main__":
    """
    The program create a new instance of CompilationEngine for every given 
    .jack file. The instance will create the desired .vm file.
    """
    list_of_files_path = get_files(sys.argv)
    for file_path in list_of_files_path:
        current_code = CompilationEngine(file_path, file_output_path(file_path))
        current_code.compileClass()

