#!/usr/bin/python

import sys, json
from pprint import pprint
import re


def search(str, line):
    str = "\.".join(str.rsplit("."))
    str = "[^~]*".join(str.rsplit("*"))
    str = str + '$'
    pattern = re.compile(str)
    if pattern.match(line):
        return line

def formatJson(dicti):
    a = json.dumps(dicti, sort_keys=True,
               indent=4, separators=(',', ': '))
    return a
##Walks
def walk(inKey):
    ##Helps walk 1 with all cases of recursion
    def walkHelper(inKey, line, searchdb):
        for item in inKey.keys():
            tempLine = line + "~" + str(item)
            if not isinstance(inKey[item], dict):
                tempLine = tempLine + "~" + str(inKey[item])
                #print tempLine
                searchdb.append(tempLine)
            else:
                #print tempLine
                searchdb.append(tempLine)
                searchdb = walk2(inKey[item], tempLine, searchdb)
        return searchdb
    
    line = ""
    searchdb = []
    for item in inKey.keys():
        line = str(item)
        #print line
        if not isinstance(inKey[item], dict):
            line = line + "~" +str(inKey[item])
            #print line
            searchdb.append(line)
        else:
            searchdb.append(line)
            searchdb = walkHelper(inKey[item], line, searchdb)
    return searchdb



def descend(dictionary, loc):
    prev = dictionary
    newItem = prev[loc.pop(0)]
    try:
        descend(prev, dict)
    except:
        print newItem
if len(sys.argv) == 1:
    print "Usage: \n\t./JSONeditor [File]\n\t./JSONeditor [File] [FileStructurePath]\n\t./JSONeditor [File] [FileStructurePath] [Value]\n\t./JSONeditor [File] [FileStructurePath] [New Name]"
##Case1 -- print all possible paths
elif len(sys.argv) == 2:
    with open(sys.argv[1], 'r') as fp:
        inputFile = json.load(fp)
        line = ""
        searchdb = []
        searchdb = walk(inputFile)
        for res in searchdb:
            line = res
            if line != "None":
                print line
##WORK ON BETTER DISPLAY... NESTED??
##Case 2 -- print values matching search term
elif len(sys.argv) == 3:
    with open(sys.argv[1], 'r') as fp:
        inputFile = json.load(fp)
        line = ""
        searchdb = []
        searchdb = walk(inputFile)
        for res in searchdb:
            line = str(search(sys.argv[2], res))
            if line != "None":
                print line
##Case 3 -- edit values
elif len(sys.argv) == 4:
    with open(sys.argv[1], 'r') as fp:
        inputFile = json.load(fp)
        line = ""
        searchdb = []
        searchdb = walk(inputFile)
        print "\n\nTargets:\n\n"
        for res in searchdb:
            line = str(search(sys.argv[2], res))
            new = sys.argv[3]
            if line != "None":
                print line
                loc = line.split('~')
                for item in loc:
                    try:
                        item = float(item)
                    except ValueError:
                        item = item
                try:
                    new = float(sys.argv[3])
                except ValueError:
                    new = sys.argv[3]
#print loc
#descend(inputFile[loc.pop(0)], loc)
                if len(loc) == 2:
                    inputFile[loc[0]] = new
                elif len(loc) == 3:
                    inputFile[loc[0]][loc[1]] = new
                elif len(loc) == 4:
                    #print inputFile[loc[0]][loc[1]][loc[2]]
                    inputFile[loc[0]][loc[1]][loc[2]] = new
                #print inputFile[loc[0]][loc[1]][loc[2]]
                elif len(loc) == 5:
                    inputFile[loc[0]][loc[1]][loc[2]][loc[3]] = new
                elif len(loc) == 6:
                    inputFile[loc[0]][loc[1]][loc[2]][loc[3]][loc[4]] = new
                elif len(loc) == 7:
                    inputFile[loc[0]][loc[1]][loc[2]][loc[3]][loc[4]][loc[5]] = new
                elif len(loc) == 8:
                    inputFile[loc[0]][loc[1]][loc[2]][loc[3]][loc[4]][loc[5]][loc[6]] = new
                elif len(loc) == 9:
                    inputFile[loc[0]][loc[1]][loc[2]][loc[3]][loc[4]][loc[5]][loc[6]][loc[7]] = new
                elif len(loc) == 10:
                    inputFile[loc[0]][loc[1]][loc[2]][loc[3]][loc[4]][loc[5]][loc[6]][loc[7]][loc[8]] = new
fp.close()
fp = open((sys.argv[1]), 'w')
line = ""
a = formatJson(inputFile)
fp.write(a)
fp.close()
#        for res in searchdb:
#            newLoc = sys.argv[2]
#            newLoc = newLoc.split("~")
#            newLoc[-1] = str(new)
#            ns = '~'.join(newLoc)
#            #print ns
#            line = str(search(ns, res))
#            if line != "None":
#                print line
#                try:
#                    newer = float(new)
#                    if len(loc) == 2:
#                        inputFile[loc[0]] = newer
#                    elif len(loc) == 3:
#                        inputFile[loc[0]][loc[1]] = newer
#                    elif len(loc) == 4:
#                        inputFile[loc[0]][loc[1]][loc[2]] = newer
#                    elif len(loc) == 5:
#                        inputFile[loc[0]][loc[1]][loc[2]][loc[3]] = newer
#                    elif len(loc) == 6:
#                        inputFile[loc[0]][loc[1]][loc[2]][loc[3]][loc[4]] = newer
#                    elif len(loc) == 7:
#                        inputFile[loc[0]][loc[1]][loc[2]][loc[3]][loc[4]][loc[5]] = newer
#                    elif len(loc) == 8:
#                        inputFile[loc[0]][loc[1]][loc[2]][loc[3]][loc[4]][loc[5]][loc[6]] = newer
#                    elif len(loc) == 9:
#                        inputFile[loc[0]][loc[1]][loc[2]][loc[3]][loc[4]][loc[5]][loc[6]][loc[7]] = newer
#                    elif len(loc) == 10:
#                        inputFile[loc[0]][loc[1]][loc[2]][loc[3]][loc[4]][loc[5]][loc[6]][loc[7]][loc[8]] = newer
#                except Exception:
#                    pass


#                while len(loc) > 0:
#                    itemloc.pop(0)
                    #Change name
                    #check if thelast item passed in argument has a child, or is a child
#if hasChild(loc, inputFile):

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