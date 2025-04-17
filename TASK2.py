file = "output.txt"
f = open(file,"w")
Input = input("Enter text to write to your file: ")
Input = Input + "\n"
f.write(Input)    
print("Data successfully written to",file)
f.close()

f = open("output.txt","a")
Input = input("Enter additional text to append: ")
f.write(Input)
print("Data successfully appended.")
f.close()

f = open("output.txt","r")
print("Final content of",file,":")
read = 0
while read != "":
    read = f.readline()
    print(read)
f.close()

# Enter text to write to your file: Hello, Python!
# Data successfully written to output.txt
# Enter additional text to append: Learning file handling.
# Data successfully appended.
# Final content of output.txt :
# Hello, Python!

# Learning file handling.