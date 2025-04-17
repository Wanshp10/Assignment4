#TASK1 

📄 File Reader Script in Python
This Python script reads and prints the contents of a text file line by line, while also handling the case where the file does not exist.

🧾 Description
Tries to open a file named sample.txt in read mode.

Reads the file line by line using a while loop.

Prints each line with its corresponding line number.

If the file is not found, it gracefully handles the error using a try-except block.

💡 Example Output
plaintext
Copy
Edit
Reading file content:
Line 1 :  It is a sample text file.
Line 2 :  It contains multiple lines.
If the file is missing:

plaintext
Copy
Edit
Error: The file sample.txt was not found.
🚀 How to Run
Ensure Python 3 is installed on your system.

Place a file named sample.txt in the same directory as TASK1.py.

Run the script using:

bash
Copy
Edit
python TASK1.py
🧠 Concepts Used
File handling (open, readline, close)

Exception handling (try-except)

Looping and conditional logic

📄 License
This project is open-source and free to use.

#TASK2

📝 File Writer, Appender & Reader in Python
This Python script allows users to write, append, and read content from a text file named output.txt.

📄 Description
The script performs the following steps in sequence:

Prompts the user to enter text and writes it to output.txt.

Prompts for additional input and appends it to the same file.

Reads and prints the entire content of the file line by line.

💡 Example Interaction
pgsql
Copy
Edit
Enter text to write to your file: Hello, Python!
Data successfully written to output.txt
Enter additional text to append: Learning file handling.
Data successfully appended.
Final content of output.txt :
Hello, Python!
Learning file handling.
🚀 How to Run
Make sure Python 3 is installed on your system.

Save the script as TASK2.py.

Open a terminal and run the script using:

bash
Copy
Edit
python TASK2.py
Follow the prompts to input and view text in the file.

🧠 Key Concepts Used
File operations: write ("w"), append ("a"), read ("r")

User input handling

Loops and conditional checks

⚠️ Note
Running this script multiple times will overwrite the file content initially, but appends afterward.

Make sure you have write permission in the directory.

📄 License
This project is open-source and free to use.

