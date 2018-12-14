import re

COMMENT = "(//.*)|(/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/)"
EMPTY_TEXT_PATTERN = re.compile("\s*")
KEY_WORD_PATTERN = re.compile("^\s*("
                              "class|constructor|function|method|static|field"
                              "|var|int|char|booolean|void|true|false|null|this|"
                              "let|do|if|else|while|return)\s*")
SYMBOL_PATTERN = re.compile("^\s*({|}|\(|\)|\[|\]|\.|,"
                            "|;|\+|-|\*|/|&|\||<|>|=|~)\s*")
DIGIT_PATTERN = re.compile("^\s*(\d+)\s*")
STRING_PATTERN = re.compile("^\s*\"(.*)\"\s*")
IDENTIFIER_PATTERN = re.compile("^\s*([a-zA-Z_][a-zA-Z1-9_]*)\s*")


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
        if DEBUGGING:
            print(self.text)
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
        if re.fullmatch(EMPTY_TEXT_PATTERN, self.text):
            return False
        else:
            return True

    def advance(self):
        if self.hasMoreTokens():
            pass


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
    print(a.hasMoreTokens())
