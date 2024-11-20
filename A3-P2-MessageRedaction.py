#Program 2 – Message Redaction
#Description:   Design and write a program that counts and removes all desired letters from 
#               any user-entered sentence or phrase.

#Student #:     W0402993
#Student Name:  Andrew Beaver

def openingMessage():
    return "Message Redaction"

def redactionFunction():
    redactCount = 0

    #Create infinite loop, quit ends program
    while True:

        #Get phrase from user
        program = input("\nType a phrase (or quit to exit program): ").lower()
        if program == "quit":
            print("End of program")
            break

        #Get the characters to redact from user. use split() to get the characters in the same input
        lettersToRedact = input("Type a comma-seperated list of letters to redact: ").lower()
        redaction = lettersToRedact.split(',')

        #replace characters with _
        for letter in redaction:
            redactedProgram = program.replace(letter, "_")
            redactCount += program.count(letter)
            program = redactedProgram
        print("Numbers of letters redacted: {0}".format(redactCount))
        print("Redacted Phrase: {0}".format(redactedProgram))

def main():

    message = openingMessage()
    print(message)

    redactionFunction()

main()