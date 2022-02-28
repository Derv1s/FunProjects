letters = {"A": ".-",
           "B": "-...",
           "C": "-.-.",
           "Ç":	"-.-..",
           "D": "-..",
           "E": ".",
           "F": "..-.",
           "G": "--.",
           "Ğ": "--.-.",
           "H": "....",
           "I": "..",
           "İ": ".-..-",
           "J": ".---",
           "K": "-.-",
           "L": ".-..",
           "M": "--",
           "N": "-.",
           "O": "---",
           "Ö": "---.",
           "P": ".--.",
           "R": ".-.",
           "S": "...",
           "Ş": "",
           "T": "-",
           "U": "..-",
           "Ü": "..--",
           "V": "...-",
           "W": ".--",
           "X": "-..-",
           "Y": "-.--",
           "Z": "--..",
           " ": "/",
           ".": ".-.-.-",
           ",": "--..--",
           "?": "..--..",
           "0":	"-----",	
           "1":	".----",	
           "2":	"..---",	
           "3":	"...--",	
           "4":	"....-",	
           "5":	".....",
           "6":	"-....",	
           "7":	"--...",	
           "8":	"---..",	
           "9":	"----."}

def morse(string):
    if "." in string[:4] or "-" in string[:4]:
        
        coded_text = string.split()
        
        key_lists = list(letters.keys())
        value_lists = list(letters.values())

        normal_text = ""

        for word in coded_text:
            word = word.split()
            for element in word:
                position = value_lists.index(element)
                normal_text += key_lists[position]

        return print(normal_text)

    else:
        mors_text = ""

        for letter in string:
            mors_text += letters[letter] + " "

        return print(mors_text)

text = input("Enter the message you want to convert to morse or enter the morse code that you receive:\n").upper()

morse(text)