#!/usr/bin/python
import sys,string,re

def formatRel():
    for i in range(469):
        with open("./{}.clauses".format(i)) as inFile:
            for line in inFile:
                    if "clause dscr:" in line:
                        clause = {}
                        #delete "clause dscr" and ']'
                        str0 = re.sub(r"clause dscr:\s*",'',line).strip(']\n')
                        #extract verb
                        strList = str0.split('[')
                        clause["verb"] = strList[0].strip()
                        
                        objNrel = strList[1].split('|');
                        length = len(objNrel)

                        #if obj and rel are all null
                        if length == 1:
                            clause["obj1"]= "Null"
                            clause["rel12"]="Null"
                            
                        else:
                            #extract all the obj
                            for j in range(length-1):
                                clause["obj{}".format(j+1)] = objNrel[j].strip()
            
                            #extract all relation
                            rel = objNrel[length -1].strip()
                            rel = re.sub(r"relation:\s*(\(.*\))*",'',rel)
                            rel = re.findall(r"({[^}]*})",rel)

                            #if relation is Null
                            if not rel:
                                clause["rel12"] = "Null"
                                
                            #if relation not Null(one obj)
                            else:
                                objLength = length -1
                                index = 0
                                for k in range(1, objLength):
                                    for l in range (k,objLength):
                                        clause["rel{}{}".format(k,l+1)] = re.match(r"^{.*->(.*)}$",rel[index]).group(1).strip()
                                        index +=1

                                    
                        
                                    
                        print("File{}\n{}".format(i,clause))
                        
                        
                    
                


def main():
    formatRel()

if __name__ == "__main__":
    main()
