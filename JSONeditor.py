#!/usr/bin/python

import sys, json
from pprint import pprint
import re


def search(str, line):
    str = "[^~]*".join(str.rsplit("*"))
    str = str + '$'
    pattern = re.compile(str)
    if pattern.match(line):
        return line


def walk1(inKey, line, searchdb):
    for item in inKey.keys():
        line = str(item)
        #print line
        if not isinstance(inKey[item], dict):
            line = line + "~" +str(inKey[item])
            #print line
            searchdb.append(line)
        else:
            searchdb = walk2(inKey[item], line, searchdb)
    return searchdb

def walk2(inKey, line, searchdb):
    for item in inKey.keys():
        tempLine = line + "~" + str(item)
        if not isinstance(inKey[item], dict):
            tempLine = tempLine + "~" + str(inKey[item])
            #print tempLine
            searchdb.append(tempLine)
        else:
            tempLine = tempLine + "~" + str(item)
            #print tempLine
            searchdb.append(tempLine)
            searchdb = walk2(inKey[item], tempLine, searchdb)
    return searchdb

def isCollection(things):
    try:
        for thing in things:
            return True
    except TypeError:
        return False


with open(sys.argv[1], 'r') as fp:
    inputFile = json.load(fp)
    loc = sys.argv[2].split(':')
    line = ""
    searchdb = []
    searchdb = walk1(inputFile, line, searchdb)
    for res in searchdb:
        line = str(search(sys.argv[2], res))
        if line != "None":
            print line
#    for item in loc:
#        try:
#            item = float(item)
#        except ValueError:
#            item = item
#    try:
#        new = float(sys.argv[3])
#    except ValueError:
#        new = sys.argv[3]
#    if '-rn' in sys.argv:
#        if len(loc) == 1:
#            inputFile[new] = inputFile.pop(loc[0])
#        elif len(loc) == 2:
#            inputFile[loc[0]][new] = inputFile[loc[0]].pop(loc[1])
#        elif len(loc) == 3:
#            inputFile[loc[0]][loc[1]][new] = inputFile[loc[0]][loc[1]].pop(loc[2])
#        elif len(loc) == 4:
#            inputFile[loc[0]][loc[1]][loc[2]][new] = inputFile[loc[0]][loc[1]][loc[2]].pop(loc[3])
#        elif len(loc) == 5:
#            inputFile[loc[0]][loc[1]][loc[2]][loc[3]][new] = inputFile[loc[0]][loc[1]][loc[2]][loc[3]].pop(loc[4])
#        elif len(loc) == 6:
#            inputFile[loc[0]][loc[1]][loc[2]][loc[3]][loc[4]][new] = inputFile[loc[0]][loc[1]][loc[2]][loc[3]][loc[4]].pop(loc[5])
#        elif len(loc) == 7:
#            inputFile[loc[0]][loc[1]][loc[2]][loc[3]][loc[4]][loc[5]][new] = inputFile[loc[0]][loc[1]][loc[2]][loc[3]][loc[4]][loc[5]].pop(loc[6])
#        elif len(loc) == 8:
#            inputFile[loc[0]][loc[1]][loc[2]][loc[3]][loc[4]][loc[5]][loc[6]][new] = inputFile[loc[0]][loc[1]][loc[2]][loc[3]][loc[4]][loc[5]][loc[6]].pop(loc[7])
#        elif len(loc) == 9:
#            inputFile[loc[0]][loc[1]][loc[2]][loc[3]][loc[4]][loc[5]][loc[6]][loc[7]][new] = inputFile[loc[0]][loc[1]][loc[2]][loc[3]][loc[4]][loc[5]][loc[6]][loc[7]].pop(loc[8])
#        elif len(loc) == 10:
#            inputFile[loc[0]][loc[1]][loc[2]][loc[3]][loc[4]][loc[5]][loc[6]][loc[7]][loc[8]][new] = inputFile[loc[0]][loc[1]][loc[2]][loc[3]][loc[4]][loc[5]][loc[6]][loc[7]][loc[8]].pop(loc[9])
#    else:
#        if len(loc) == 1:
#            inputFile[loc[0]] = new
#        elif len(loc) == 2:
#            inputFile[loc[0]][loc[1]] = new
#        elif len(loc) == 3:
#            inputFile[loc[0]][loc[1]][loc[2]] = new
#        elif len(loc) == 4:
#            inputFile[loc[0]][loc[1]][loc[2]][loc[3]] = new
#        elif len(loc) == 5:
#            inputFile[loc[0]][loc[1]][loc[2]][loc[3]][loc[4]] = new
#        elif len(loc) == 6:
#            inputFile[loc[0]][loc[1]][loc[2]][loc[3]][loc[4]][loc[5]] = new
#        elif len(loc) == 7:
#            inputFile[loc[0]][loc[1]][loc[2]][loc[3]][loc[4]][loc[5]][loc[6]] = new
#        elif len(loc) == 8:
#            inputFile[loc[0]][loc[1]][loc[2]][loc[3]][loc[4]][loc[5]][loc[6]][loc[7]] = new
#        elif len(loc) == 9:
#            inputFile[loc[0]][loc[1]][loc[2]][loc[3]][loc[4]][loc[5]][loc[6]][loc[7]][loc[8]] = new
#        elif len(loc) == 10:
#            inputFile[loc[0]][loc[1]][loc[2]][loc[3]][loc[4]][loc[5]][loc[6]][loc[7]][loc[8]][loc[9]] = new
#    pprint(inputFile)
#    print "Usage: ./JSONeditor.py <file name> <string> -option (-rn)"