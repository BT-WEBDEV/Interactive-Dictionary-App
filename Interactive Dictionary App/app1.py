####### Interactive Dictionary #######
# user inputs a word and the program provides the definition of the word
# input & output is displayed within the commandline - no graphical interface. 
# Takeaways from project: importing libraries, getting data from the JSON file, conditionals, variables, and debugging. 
# Possible extensions to this program: web or desktop application with a graphical interface. 


import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data: 
        return data [w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Y for yes, N for no: " % get_close_matches(w, data.keys()) [0])
        if yn == "Y": 
            return data[get_close_matches(w, data.keys()) [0]]
        elif yn == "N":
            return "The word doesn't exist, please try again."
        else: 
            return "We didn't understand your entry, please try again."
    else:
        return "This word does not exist, please try again."

word = input("Enter word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else: 
    print(output)