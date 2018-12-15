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
        self.compileClassVarDec()
        self.compileSubroutine()

        self._tokenizer.advance()
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
        if self._tokenizer.keyWord() == "static" or\
            self._tokenizer.keyWord() == "field":
            self._output.write("\t" * self._indentation + "<classVarDec>")
            self._indentation += 1
            self._write_keyword()


            ## code prints class vars recursively

            self._indentation -= 1
            self._output.write("\t" * self._indentation + "<\classVarDec>")


    def compileSubroutine(self):
        if self._tokenizer.keyWord() == "constructor" or \
                self._tokenizer.keyWord() == "function" \
                or self._tokenizer == "method":
            self._indentation += 1
            ## some magic here

            self._indentation -= 1

    def compileParameterList(self):
        pass

    def compileVarDec(self):
        pass

    def compileStatements(self):
        pass

    def compileDo(self):
        pass

    def compileLet(self):
        pass

    def compileWhile(self):
        pass

    def compileReturn(self):
        pass

    def compileIf(self):
        pass

    def CompileExpression(self):
        pass

    def CompileTerm(self):
        pass

    def CompileExpressionList(self):
        pass

    def _write_identifier(self):
        self._output.write("\t" * self._indentation + "<identifier> " +
                           self._tokenizer.identifier() + " <\identifier>\n")

    def _write_keyword(self):
        self._output.write("\t" * self._indentation + "<keyword> " +
                           self._tokenizer.keyWord() + " <\keyword>\n")

    def _write_symbol(self):
        self._output.write("\t" * self._indentation + "<symbol> " +
                           self._tokenizer.symbol() + " <\symbol>\n")