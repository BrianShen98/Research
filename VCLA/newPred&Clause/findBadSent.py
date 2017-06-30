#! /usr/bin/python

import string, sys,re

def find_Bad_Multi_Line():
    for i in range(469):
        with open("./progRefined/{}.clauses".format(i),"r") as inFile:
            for line in inFile:            
                if "sent:" in line and "clause dscr:" not in next(inFile):
                    print("File {}\n{}".format(i,line))


def find_Bad_Single_Line():
    for i in range(469):
        with open("./progRefined/{}.clauses".format(i),"r") as inFile:
            for line in inFile:            
                if "sent:" in line and "clause dscr:" in next(inFile):
                    noSent = re.sub(r"sent:\s*",'',line)
                    regAnd = re.compile(r".+and.+")
                    regDot = re.compile(r".+\..+")
                    if re.search(regDot,noSent) or re.search(regAnd,noSent):
                        print("File {}\n{}".format(i,line))

                    
                    

def main():
    if len(sys.argv) != 2:
        print("wrong number of arguments!")
        exit(1);
    if sys.argv[1] == "single":
        find_Bad_Single_Line()
    elif sys.argv[1] == "multi":
        find_Bad_Multi_Line()
    else:
        print("cannot recognize the option!")
        exit(1)
    
if __name__ == "__main__":
    main();
