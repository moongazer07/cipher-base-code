#User inputs text and rick astley cipher is returned.
#rick astley chipher encoder
#moongazer07

def encodeUserMsg(userInput):
    msg = ""
    CIPHERbet = {
                'A' : " ",
                'B' : " ",
                'C' : " ",
                'D' : " ",
                'E' : " ",
                'F' : " ",
                'G' : " ",
                'H' : " ",
                'I' : " ",
                'J' : " ",
                'K' : " ",
                'L' : " ",
                'M' : " ",
                'N' : " ",
                'O' : " ",
                'P' : " ",
                'Q' : " ",
                'R' : " ",
                'S' : " ",
                'T' : " ",
                'U' : " ",
                'V' : " ",
                'W' : " ",
                'X' : " ",
                'Y' : " ",
                'Z' : " ",
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
