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




# The main program:
if __name__ == "__main__":
    comparison_counter = 0
    list_of_files_path = get_files(sys.argv)
    # assembly_lines_list = ["@256",
    #                        "D = A",
    #                        "@SP",
    #                        "M = D // set stack pointer to 0x0100",
    #                        "@Sys.init",
    #                        "0;JMP // invoke Sys.init"]
    for file_path in list_of_files_path:
        assembly_lines_list += file_to_assembly_lines(file_path)
    lines_list_to_file(file_output_path(sys.argv[1]), assembly_lines_list)
