#!/usr/bin/python
import sys,string,re

clause = {"verb":None,
        "obj1":None,
        "obj2":None,
        "rel12":None}

def formatRel2():
    for i in range(469):
        with open("./{}.clauses".format(i)) as inFile:
            for line in inFile:
                if  "sent:" in line:
                    dscr = next(inFile)
                    if "clause dscr:" in dscr:
                    #delete "clause dscr" and ']'
                        str0 = re.sub(r"clause dscr:\s*",'',dscr).strip(']\n')
                        #extract verb
                        strList = str0.split('[')
                        clause["verb"] = strList[0].strip()
                        
                        objNrel = strList[1].split('|');
                        
                        #extract obj
                        clause["obj1"] = objNrel[0].strip()
                        clause["obj2"] = objNrel[1].strip()

                    
                


def main():
    formatRel2()

if __name__ == "__main__":
    main()
