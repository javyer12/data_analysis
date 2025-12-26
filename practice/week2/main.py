from processor.tools import to_lowercase_strip
from processor.tools import to_lowercase_add_space


print(to_lowercase("Hello World"))  # Output: hello/world
data = input("Enter some text with or without spaces: ")
try:
    if " " in data: 
        with open("data.pdf", "a") as file:
            file.write("\n" + to_lowercase_strip(data))
            file.write("\n Bye, File closed.")
            print("File written successfully -> ", data, " on ", file.name)
    else:
        with open("data.pdf", "a") as file:
            file.write("\n" + to_lowercase_add_space(data))
            file.write("\n Bye, File closed.")
        print("File written successfully -> ", data, " on ", file.name)
except FileNotFoundError as e: print("Error: File not found", e)
finally: print("Execution completed.")

