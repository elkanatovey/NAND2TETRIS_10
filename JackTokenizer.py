import re

COMMENT = "//.*$"

class JackTokenizer:
    """
    JackTokenizer module as described in NAND2Tetris chapter 10
    """

    KEYWORDS = ["CLASS", "METHOD", "FUNCTION", "CONSTRUCTOR", "INT",
                "BOOLEAN", "CHAR", "VOID", "VAR", "STATIC", "FIELD", "LET",
                "DO", "IF", "ELSE", "WHILE", "RETURN", "TRUE", "FALSE",
                "NULL", "THIS"]

    TOKEN_TYPES = ["KEYWORD", "SYMBOL", "IDENTIFIER", "INT_CONST",
                   "STRING_CONST"]



    def __init__(self, input_file):
        """

        :param input_file: the current file
        """
        self.file = input_file
        self.currentLine = input_file.readline().strip()
        self.skipWhiteSpace()
        self.tokenType = "NONE"
        self.currentToken = "NONE"

    def skipWhiteSpace(self):
        """
        skips the whitespace in a file, recursively moves forward on
        this
        """
        self.currentLine = re.sub(COMMENT, "", self.currentLine)  ## case: //
        if self.currentLine == "":  ## empty line
            self.currentLine = self.file.readline().strip()
            self.skipWhiteSpace()
        if self.currentLine.find('/*') == 0:
            while self.currentLine.find('*/') < 2:
                self.currentLine = self.file.readline().strip()
            self.currentLine = self.file.readline().strip()
            self.skipWhiteSpace()





    def hasMoreTokens(self):
        pass

    def advance(self):
        self.skipWhiteSpace()
        if 

    def tokenType(self):
        return self.tokenType

    def keyWord(self):
        pass

    def symbol(self):
        return self.currentToken

    def identifier(self):
        pass

    def intVal(self):
        return int(self.currentToken)

    def stringVal(self):
        return self.currentToken