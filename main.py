"""
doc1
doc2
"""
import sys
from parsers import DataParser
from utils import  DBHelper
import gettext
global g;

def main(*arg):
    g = 10;
    print(globals())
    """
    :param arg:
    :return:
    """
    #DataParser.AirportParser().parseFile(sys.argv[1])
    #DBHelper.DBHelper().getConnection()
    #print(arg)

if __name__ == '__main__':
   main(sys.argv);