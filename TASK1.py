try:
    file = "sample.txt"
    f = open(file,"r")
    i=1
    read = 0
    print("Reading file content: ")
    while read != "":
        read = f.readline()
        if read!="":
            print("Line",i,": ",read)
        else:
            break
        i+=1
    f.close()
except FileNotFoundError:
    print("Error: The file",file,"was not found.")
# Reading file content:
# Line 1 :  It is a sample text file.
#
# Line 2 :  It contains multiple lines.