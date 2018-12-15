import re
from JackTokenizer import JackTokenizer


class CompilationEngine:
    """
    effects the compilation engine
    """

    def __init__(self, input_file_path, output_path):
        """

        :param fileToRead:
        """
        self._indentation = 0
        self._tokenizer = JackTokenizer(input_file_path)
        self._output = open(output_path, "w+")
        if self._tokenizer.hasMoreTokens():
            self._tokenizer.advance()
            self.compileClass()

    def compileClass(self):
        self._output.write("<class>\n")
        self._indentation += 1

        self._tokenizer.advance()
        self._write_keyword()

        self._tokenizer.advance()
        self._write_identifier()

        self._tokenizer.advance()
        self._write_symbol()

        self._tokenizer.advance()
        while self._tokenizer.keyWord() == "static" or \
                self._tokenizer.keyWord() == "field":
            self.compileClassVarDec()
        while self._tokenizer.keyWord() == "constructor" or \
                self._tokenizer.keyWord() == "function" \
                or self._tokenizer == "method":
            self.compileSubroutine()

        self._write_symbol()

        self._indentation -= 1
        self._output.write("<\class>")
        self._output.close()

    def compileClassVarDec(self):
        """
        this should only print if there actually are class var decs,
        should run on the recursively
        :return:
        """
        self._output.write("\t" * self._indentation + "<classVarDec>")
        self._indentation += 1
        self._write_keyword()

        self._tokenizer.advance()
        self._compile_type_and_varName()

        self._indentation -= 1
        self._output.write("\t" * self._indentation + "<\classVarDec>")

    def compileSubroutine(self):
        self._output.write("\t" * self._indentation + "<subroutineDec>")
        self._indentation += 1
        self._write_keyword()

        self._tokenizer.advance()
        if self._tokenizer.tokenType() == self._tokenizer.KEYWORD:
            self._write_keyword()
        elif self._tokenizer.tokenType() == self._tokenizer.IDENTIFIER:
            self._write_identifier()

        self._tokenizer.advance()
        self._write_identifier()

        self._tokenizer.advance()
        self._write_symbol()

        self._tokenizer.advance()
        self.compileParameterList()

        self._write_symbol()

        self._tokenizer.advance()
        # compile subroutineBody:
        self._output.write("\t" * self._indentation + "<subroutineBody>")
        self._indentation += 1
        self._write_symbol()

        self._tokenizer.advance()
        while self._tokenizer.keyWord() == "var":
            self.compileVarDec()

        self.compileStatements()

        self._write_symbol()
        self._indentation -= 1
        self._output.write("\t" * self._indentation + "<\subroutineBody>")
        self._indentation -= 1
        self._output.write("\t" * self._indentation + "<\subroutineDec>")
        self._tokenizer.advance()

    def compileParameterList(self):
        self._output.write("\t" * self._indentation + "<parameterList>")
        self._indentation += 1
        while self._tokenizer.tokenType() != self._tokenizer.SYMBOL:
            if self._tokenizer.tokenType() == self._tokenizer.KEYWORD:
                self._write_keyword()
            elif self._tokenizer.tokenType() == self._tokenizer.IDENTIFIER:
                self._write_identifier()
            self._tokenizer.advance()
            self._write_identifier()
            self._tokenizer.advance()
            if self._tokenizer.symbol() == ",":
                self._write_symbol()
                self._tokenizer.advance()

        self._indentation -= 1
        self._output.write("\t" * self._indentation + "<\parameterList>")
        self._tokenizer.advance()

    def compileVarDec(self):
        self._output.write("\t" * self._indentation + "<varDec>")
        self._indentation += 1

        self._write_keyword()
        self._tokenizer.advance()
        self._compile_type_and_varName()

        self._indentation -= 1
        self._output.write("\t" * self._indentation + "<\\varDec>")

    def compileStatements(self):
        self._output.write("\t" * self._indentation + "<statements>")
        self._indentation += 1
        while self._tokenizer.tokenType() == self._tokenizer.keyWord():
            if self._tokenizer.keyWord() == "let":
                self.compileLet()
            elif self._tokenizer.keyWord() == "if":
                self.compileIf()
            elif self._tokenizer.keyWord() == "while":
                self.compileWhile()
            elif self._tokenizer.keyWord() == "do":
                self.compileDo()
            elif self._tokenizer.keyWord() == "return":
                self.compileReturn()
        self._indentation -= 1
        self._output.write("\t" * self._indentation + "<\statements>")

    def compileDo(self):
        pass

    def compileLet(self):
        self._output.write("\t" * self._indentation + "<letStatement>")
        self._indentation += 1
        self._write_keyword()

        self._tokenizer.advance()
        self._write_identifier()

        self._tokenizer.advance()
        if self._tokenizer.symbol() == "[":
            self._write_symbol()
            self._tokenizer.advance()
            self.compileExpression()
            self._write_symbol()
            self._tokenizer.advance()

        self._write_symbol()

        self._tokenizer.advance()
        self.compileExpression()
        self._write_symbol()

        self._indentation -= 1
        self._output.write("\t" * self._indentation + "<\letStatement>")
        self._tokenizer.advance()

    def compileWhile(self):
        pass

    def compileReturn(self):
        pass

    def compileIf(self):
        pass

    def compileExpression(self):
        pass

    def compileTerm(self):
        pass

    def compileExpressionList(self):
        pass

    def _compile_type_and_varName(self):
        if self._tokenizer.tokenType() == self._tokenizer.KEYWORD:
            self._write_keyword()
        elif self._tokenizer.tokenType() == self._tokenizer.IDENTIFIER:
            self._write_identifier()
        self._tokenizer.advance()
        self._write_identifier()
        self._tokenizer.advance()
        while self._tokenizer.symbol() == ",":
            self._write_symbol()
            self._tokenizer.advance()
            self._write_identifier()
            self._tokenizer.advance()
        self._write_symbol()
        self._tokenizer.advance()

    def _write_identifier(self):
        self._output.write("\t" * self._indentation + "<identifier> " +
                           self._tokenizer.identifier() + " <\identifier>\n")

    def _write_keyword(self):
        self._output.write("\t" * self._indentation + "<keyword> " +
                           self._tokenizer.keyWord() + " <\keyword>\n")

    def _write_symbol(self):
        self._output.write("\t" * self._indentation + "<symbol> " +
                           self._tokenizer.symbol() + " <\symbol>\n")
