from JackTokenizer import JackTokenizer

class CompilationEngine:
    """
    effects the compilation engine
    """

    def __init__(self, input_file, outputLocation):
        """

        :param fileToRead:
        """
        self.file = input_file
        self.output = outputLocation
        self.tokenizer = JackTokenizer(self.file)


    def compileClass(self):
        currentToken = self.tokenizer.advance()

        self.output.write( + "\n")


    def compileClassVarDec(self):
        pass

    def compileSubroutine(self):
        pass

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