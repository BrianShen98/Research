#!/usr/bin/python

import sys,locale,string

#replace old mapping with new one
def replace(prop):
    for i in range(469):
        with open("./progRefined/{}.instenv".format(i),"w") as outFile:
            with open("./tellmedave_data_alignmentrefined/{}.instenv".format(i),"r") as inFile:
                for line in inFile:
                    buffer = line;
                    for old,new in prop.items():
                        if old in line:
                            buffer=buffer.replace(old,new);
                    outFile.write(buffer);
                    
    


#create old->new prop mapping dict
def propDict():
    dict = {};
    with open("./newMapping","r") as input:
        while True:
            line1 = input.readline().rstrip("\n");
            line2 = input.readline().rstrip("\n");
            if not line2:
                break;
            dict[line1] = line2;

        return dict;


def main():
    prop = propDict();
    replace(prop);
if __name__ == "__main__":
    main();
