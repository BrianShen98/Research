#!/usr/bin/python
import sys,string,re

clause = {"verb":None,
        "obj1":None,
        "obj2":None,
        "rel12":None}

def check():
    for i in range(469):
        with open("./{}.clauses".format(i)) as inFile:
            for line in inFile:
                if "clause dscr:" in line and "(2, 2)"in line and "(2, 2){" not in line:
                    print("File{}\n{}".format(i,line))
                


def main():
    check()

if __name__ == "__main__":
    main()
