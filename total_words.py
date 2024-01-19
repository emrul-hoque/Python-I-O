import os

os.system("cls")

file_path = "F:\Emrul\Python\Python IO\Python IO.txt"

try:
    with open(file_path, 'r') as file:
        content = file.read()
        word_count = len(content.split())
        print("Total number of words in the sentence is:\t", word_count)
        #print("\n",content)
except FileNotFoundError:
    print(f"The file {file_path} was not found.")
except Exception as e:
    print(f"An error occurred:\n {e}")

print()

