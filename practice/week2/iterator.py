from processor.__init__ import min_wordFilter 
from processor.__init__ import max_wordFilter 



min_or_max = input("Filter by minimum or maximum length? (min/max): ").strip().lower()
text = input("Enter some text: ")

if (min_or_max == "max"):
    
    max_length = int(input("Enter maximum word length to filter: "))
    for word in max_wordFilter(text, max_length):
        print("Filtered word:", word)
elif (min_or_max == "min"):
    min_length = int(input("Enter minimum word length to filter: "))
    for word in min_wordFilter(text, min_length):
        print("Filtered word:", word)
else:
    print("Invalid option selected. Please choose 'min' or 'max'.")