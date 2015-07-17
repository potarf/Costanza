#!/usr/bin/python

import sys, json
from pprint import pprint
import re

##Return line if line matches str (re)
###Else return "None"
def search(str, line):
    str = "\.".join(str.rsplit("."))
    str = "[^~]*".join(str.rsplit("*"))
    str = str + '$'
    pattern = re.compile(str)
    if pattern.match(line):
        return line
##Format dictionary to pretty JSON, for human/machine readable pickling
def formatJson(dicti):
    a = json.dumps(dicti, sort_keys=True,
               indent=4, separators=(',', ': '))
    return a

##walk: recursively walk dictionary
def walk(inKey):
    ##Helps walk 1 with all cases of recursion
    def walkHelper(inKey, line, searchdb):
        for item in inKey.keys():
            tempLine = line + "~" + str(item)
            searchdb.append(tempLine)
            if not isinstance(inKey[item], dict):
                tempLine = tempLine + "~" + str(inKey[item])
                #print tempLine
                searchdb.append(tempLine)
            else:
                #print tempLine
                searchdb = walkHelper(inKey[item], tempLine, searchdb)
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


#Still working on a better version of descend, for now uses many cases --  BAD
#def descend(dictionary, loc):
#    prev = dictionary
#    newItem = prev[loc.pop(0)]
#    try:
#        descend(prev, dict)
#    except:
#        print newItem

##Case0 -- print usage
if len(sys.argv) == 1:
    print "Usage: \n\tTo Print:\n\t\t./JSONeditor [File]\n\tTo Print Matching Paths:\n\t\t./JSONeditor [File] [FileStructurePath]\n\tTo Change Value\n\t\t./JSONeditor [File] [FileStructurePath] [Value]\n\tTo Change Item Name:\n\t\t./JSONeditor [File] [FileStructurePath] [New Name] -rn"
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
                ##Try to convers what can be converted to floats
                for item in loc:
                    try:
                        item = float(item)
                    except ValueError:
                        item = item
                try:
                    new = float(sys.argv[3])
                except ValueError:
                    new = sys.argv[3]
#uncomment descend and delete case based when descend works recursively
#descend(inputFile[loc.pop(0)], loc)
##BAD -- case based
                if len(loc) == 1:
                    inputFile[loc[0]] = new
                elif len(loc) == 3:
                    inputFile[loc[0]][loc[1]] = new
                elif len(loc) == 4:
                    inputFile[loc[0]][loc[1]][loc[2]] = new
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
    ##Close input file
        fp.close()
    ##Open output file
        fp = open((sys.argv[1] + "OUT"), 'w')
        line = ""
        ##Get string formatted as JSON file
        a = formatJson(inputFile)
        ##Write to output file
        fp.write(a)
        ##Close output file
        fp.close()


##Case 4 -- edit values
elif len(sys.argv) == 5:
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
                ##Try to convers what can be converted to floats
                for item in loc:
                    try:
                        item = float(item)
                    except ValueError:
                        item = item
                try:
                    new = float(sys.argv[3])
                except ValueError:
                    new = sys.argv[3]
                
                

                if len(loc) == 1:
                    if str(type(inputFile[loc[0]])) == "<type 'dict'>":
                        inputFile[new] = inputFile.pop(loc[0])
                elif len(loc) == 2:
                    if str(type(inputFile[loc[0]][loc[1]])) == "<type 'dict'>":
                        inputFile[loc[0]][new] = inputFile[loc[0]].pop(loc[1])
                    else:
                        inputFile[new] = inputFile[loc[0]]
                        del inputFile[loc[0]]
                elif len(loc) == 3:
                    if str(type(inputFile[loc[0]][loc[1]][loc[2]])) == "<type 'dict'>":
                        inputFile[loc[0]][loc[1]][new] = inputFile[loc[0]][loc[1]].pop(loc[2])
                    else:
                        inputFile[loc[0]][new] = inputFile[loc[0]][loc[1]]
                        del inputFile[loc[0]][loc[1]]
                elif len(loc) == 4:
                    if str(type(inputFile[loc[0]][loc[1]][loc[2]][loc[3]])) == "<type 'dict'>":
                        inputFile[loc[0]][loc[1]][loc[2]][new] = inputFile[loc[0]][loc[1]][loc[2]].pop(loc[3])
                    else:
                        inputFile[loc[0]][loc[1]][new] = inputFile[loc[0]][loc[1]][loc[2]]
                        del inputFile[loc[0]][loc[1]][loc[2]]
                elif len(loc) == 5:
                    if str(type(inputFile[loc[0]][loc[1]][loc[2]][loc[3]][loc[4]])) == "<type 'dict'>":
                        inputFile[loc[0]][loc[1]][loc[2]][loc[3]][new] = inputFile[loc[0]][loc[1]][loc[2]][loc[3]].pop(loc[4])
                    else:
                        inputFile[loc[0]][loc[1]][loc[2]][new] = inputFile[loc[0]][loc[1]][loc[2]][loc[3]]
                        del inputFile[loc[0]][loc[1]][loc[2]][loc[3]]
                elif len(loc) == 6:
                    if str(type(inputFile[loc[0]][loc[1]][loc[2]][loc[3]][loc[4]][loc[5]])) == "<type 'dict'>":
                        inputFile[loc[0]][loc[1]][loc[2]][loc[3]][loc[4]][new] = inputFile[loc[0]][loc[1]][loc[2]][loc[3]][loc[4]].pop(loc[5])
                    else:
                        inputFile[loc[0]][loc[1]][loc[2]][loc[3]][new] = inputFile[loc[0]][loc[1]][loc[2]][loc[3]][loc[4]]
                        del inputFile[loc[0]][loc[1]][loc[2]][loc[3]][loc[4]]
                else:
                    print "Add another case at line 204"
                #uncomment descend and delete case based when descend works recursively
                #descend(inputFile[loc.pop(0)], loc)
                ##BAD -- case based
#                if len(loc) == 2:
#                    print loc[0]
#                    inputFile[new] = inputFile.pop(loc[0])
#                elif len(loc) == 3:
#                    inputFile[loc[0]][new] = inputFile[loc[0]].pop([loc[1]])
#                elif len(loc) == 4:
#                    inputFile[loc[0]][loc[1]][new] = inputFile[loc[0]][loc[1]].pop([loc[2]])
#                elif len(loc) == 5:
#                    inputFile[loc[0]][loc[1]][loc[2]][new] = inputFile[loc[0]][loc[1]][loc[2]].pop([loc[3]])
#                elif len(loc) == 6:
#                    inputFile[loc[0]][loc[1]][loc[2]][loc[3]][new] = inputFile[loc[0]][loc[1]][loc[2]][loc[3]].pop([loc[4]])
#                elif len(loc) == 7:
#                    inputFile[loc[0]][loc[1]][loc[2]][loc[3]][loc[4]][new] = inputFile[loc[0]][loc[1]][loc[2]][loc[3]][loc[4]].pop([loc[5]])
#                elif len(loc) == 8:
#                    inputFile[loc[0]][loc[1]][loc[2]][loc[3]][loc[4]][loc[5]][new] = inputFile[loc[0]][loc[1]][loc[2]][loc[3]][loc[4]][loc[5]].pop([loc[6]])
#                elif len(loc) == 9:
#                    inputFile[loc[0]][loc[1]][loc[2]][loc[3]][loc[4]][loc[5]][loc[6]][new] = inputFile[loc[0]][loc[1]][loc[2]][loc[3]][loc[4]][loc[5]][loc[6]].pop([loc[7]])
#                elif len(loc) == 10:
#                    inputFile[loc[0]][loc[1]][loc[2]][loc[3]][loc[4]][loc[5]][loc[6]][loc[7]][new] = inputFile[loc[0]][loc[1]][loc[2]][loc[3]][loc[4]][loc[5]][loc[6]][loc[7]].pop([loc[8]])
#                if len(loc) == 1:
#                    inputFile[new] = inputFile.pop(loc[0])
#                if len(loc) == 2:
#                    print "HIIIIII"
#                    inputFile[loc[0]][new] = inputFile[loc[0]].pop(loc[1])
#                elif len(loc) == 3:
#                    inputFile[loc[0]][new] = inputFile[loc[0]].pop(loc[-1])
#                for i in inputFile:
#                    print str(i)
        ##Close input file
        fp.close()
        ##Open output file
        fp = open((sys.argv[1] + "OUT"), 'w')
        line = ""
        ##Get string formatted as JSON file
        a = formatJson(inputFile)
        ##Write to output file
        fp.write(a)
        ##Close output file
        fp.close()
