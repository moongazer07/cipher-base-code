#User inputs text and example cipher is returned.
#example chipher encoder
#moongazer07

def encodeUserMsg(userInput):
    msg = ""
    CIPHERbet = {
                'A' : "lol ",
                'B' : "l0l ",
                'C' : "LOL ",
                'D' : "troll ",
                'E' : "TROLL ",
                'F' : "TROll ",
                'G' : "potato ",
                'H' : "POTATO ",
                'I' : "DEEZ ",
                'J' : "deez ",
                'K' : "nuts ",
                'L' : "NUTS ",
                'M' : "DEEZ NUTS ",
                'N' : "deez nuts ",
                'O' : "covid ",
                'P' : "COVID ",
                'Q' : "pokemon ",
                'R' : "yo ",
                'S' : "YO ",
                'T' : "TEAM SEAS ",
                'U' : "example ",
                'V' : "DESTENY ",
                'W' : "pest ",
                'X' : "cheese ",
                'Y' : "KOKONUT ",
                'Z' : "NUT ",
                ' ' : "+ "
                }
    for ittr in range(len(userInput)):
        if(userInput[ittr].isalpha() or userInput[ittr] == ' '):
            msg += (CIPHERbet[userInput[ittr]])
    print(msg+"\n=")



print('cipher')
userInput = input("Please enter text to protect: ")
encodeUserMsg(userInput.upper())

while True:
    userInput = input("Would you like to continue? press Enter without typing anything to quit or type text and press enter to continue: ")
    if (userInput == ''):
        break
    encodeUserMsg(userInput.upper())
