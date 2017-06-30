#!/usr/bin/python

#find the empty sentences in progREfined
import string,sys,re 
def findEmpty():
    result = re.compile(r"sent:\s*$")
    for i in range(469):
        with open("./{}.clauses".format(i)) as inFile:
            for line in inFile:
                if re.search(result,line):
                    print("File {}\n{}".format(i,line))

def main():
    findEmpty()

if __name__ == "__main__":
    main();
    
