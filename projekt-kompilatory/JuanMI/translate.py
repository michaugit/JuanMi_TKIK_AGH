from JuanMI import JuanMILexer, JuanMIParser
from JuanMIListenerImpl import JuanMIListenerImpl
from antlr4 import *
import sys


def translate(input_file, output_file):

    input_stream = FileStream(input_file, encoding='utf-8')

    lexer = JuanMILexer.JuanMILexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = JuanMIParser.JuanMIParser(stream)

    tree = parser.program()

    parse_tree_walker = ParseTreeWalker()
    listener = JuanMIListenerImpl()

    parse_tree_walker.walk(listener, tree)

    file = open(output_file, "w+", encoding='utf-8')
    file.write(listener.code)
    file.close()


path = str(sys.argv[1])
target = str(sys.argv[2])
translate(path, target)





