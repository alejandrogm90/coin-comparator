#!/usr/bin/env python3
#
#
#       Copyright 2022 Alejandro Gomez
#
#       This program is free software: you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation, either version 3 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import sqlite3
from calendar import monthrange
from time import gmtime, strftime

import pyfiglet


def getProjetPath():
    """ Return the project absolute path
    :return: path as string
    """
    return os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


def getTime():
    """ Return a complete date as YYYY-MM-dd HH:mm
    :return: all date as string
    """
    return strftime("%Y-%m-%d %H:%M:%S", gmtime())


def getDate():
    """ Return a complete date as YYYY-MM-dd
    :return: all date as string
    """
    return strftime("%Y-%m-%d", gmtime())


def getHeadLine(level):
    return "[" + getTime() + "][" + level + "]"


def isDate(cadena):
    """ Check is the text recived is a rigth date
    :param cadena: datatime text (YYYY-MM-DD)
    :return: True or False
    """
    if len(cadena) != 10:
        return False

    if cadena[4] != "-" or cadena[7] != "-":
        return False

    try:
        anno = int(cadena[0:4])
        mes = int(cadena[5:7])
        dia = int(cadena[8:10])
    except:
        return False

    if mes > 12 or mes < 1:
        return False
    elif anno < mes or anno < dia:
        return False
    elif dia > monthrange(anno, mes)[1] or dia < 1:
        return False
    else:
        return True


def create_sqlitle3_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)

    return conn


def printBanner(character, textList):
    """ Print a simple banner
    :param text: text to print
    """
    line_size = 0
    for line in textList:
        if line_size < len(line):
            line_size = len(line)

    print(character * (line_size + 4))
    for line in textList:
        if len(line) == line_size:
            print(character + " " + line + " " + character)
        else:
            spaces = " " * (line_size - len(line) + 1)
            print(character + " " + line + spaces + character)
    print(character * (line_size + 4))


def printMegaBanner(text):
    """ Print a big banner
    :param text: text to print
    """
    ascii_banner = pyfiglet.figlet_format(text)
    print(ascii_banner)


def printFileEncoded(nombre):
    """ print file with encoded text
    :param nombre: file's URI
    """
    f1 = open(nombre, 'r')
    linea = f1.readline()
    while (len(linea) > 0):
        nueva = ""
        for pos in range(0, len(linea) - 1):
            nueva = nueva + str(chr(ord(linea[pos]) + 1))
        print(nueva)
        linea = f1.readline()


def getFiletName(location, extension=False):
    """ return file name not URI location
    :param location: URI of scritp
    :return: file name
    """
    SPLITER_1 = '/'
    SPLITER_2 = '.'
    name1 = os.path.split(location)[1]
    name2 = ""
    if extension:
        name2 = name1
    else:
        parts = len(name1.split(SPLITER_2))
        if parts <= 2:
            name2 = name1.split(SPLITER_2)[0]
        else:
            for part2 in range(0, (parts - 1)):
                name2 += name1.split(SPLITER_2)[part2]

    return name2


def getFileLog(location):
    """ return file name not URI location
    :param location: URI of scritp
    :return: file log name
    """
    return getFiletName(location) + "_" + getDate() + ".log"


def printLogFile(outputFile, msg):
    """ Print log file
    """
    printLogFile_file = open(outputFile, 'a')
    printLogFile_file.write(msg + os.linesep)
    printLogFile_file.close()


def infoMsg(logger, msg, outputFile=""):
    """ Show a menssage text
    :param msg: info menssage
    :param outputFile: output file
    """
    logger.info(": " + msg)
    if outputFile != "":
        printLogFile(outputFile, getHeadLine("INFO") + ": " + msg)


def warnMsg(logger, msg, outputFile=""):
    """ Show a menssage text
    :param msg: warning menssage
    :param outputFile: output file
    """
    logger.warning(": " + msg)
    if outputFile != "":
        printLogFile(outputFile, getHeadLine("WARNING") + ": " + msg)


def errorMsg(logger, num, msg, outputFile=""):
    """ Show a menssage text and exits with output number
    :param num: output number
    :param msg: error menssage
    :param outputFile: output file
    """
    logger.error("[" + str(num) + "]: " + msg)
    if outputFile != "":
        printLogFile(outputFile, getHeadLine("ERROR") + "[" + str(num) + "]: " + msg)
    exit(num)
