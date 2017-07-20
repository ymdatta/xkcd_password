#!/usr/bin/python3

filenames = ["6.txt", "7.txt", "8.txt"]
fw = open("final.txt", "w")
wlist = []
for fname in filenames:
    fo = open(fname, "r")
    while True:
        line = fo.readline()
        if len(line) == 0:
            # end of file is reached.
            break
        else:
            linelist = line.split()
            if int(linelist[1]) >= 1500:
                fw.write(str(linelist[0]) + '\n')
