import re

COMMENT = "(//.*)|(/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/)"
DEBUGGING = True

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



    def __init__(self, input_file_path):
        """

        :param input_file: the current file
        """
        with open(input_file_path, "r") as file:
            self.text = file.read()
        self.clear_all_comments()
        self.tokenType = "NONE"
        self.currentToken = "NONE"

    def clear_all_comments(self):
        """
        Clear all comments from self.text .
        """
        self.text = re.sub(COMMENT, "", self.text)
        print(self.text)




    def hasMoreTokens(self):
        pass

    def advance(self):
        self.skipWhiteSpace()


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

if __name__ == "__main__" and DEBUGGING:
    a = JackTokenizer("Square\Square.jack")