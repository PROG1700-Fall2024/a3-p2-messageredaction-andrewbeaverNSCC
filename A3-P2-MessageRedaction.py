#Program 2 – Message Redaction
#Description:   Design and write a program that counts and removes all desired letters from 
#               any user-entered sentence or phrase.

#Student #:     W0402993
#Student Name:  Andrew Beaver

def x():
    redactCount = 0
    while True:
        program = input("\nType a phrase (or quit to exit program): ").lower()
        if program == "quit":
            print("End of program")
            break
        lettersToRedact = input("Type a comma-seperated list of letters to redact: ").lower()
        redaction = lettersToRedact.split(',')

        for letter in redaction:
            redactedProgram = program.replace(letter, "_")
            redactCount += program.count(letter)
            program = redactedProgram
        print("Numbers of letters redacted: {0}".format(redactCount))
        print("Redacted Phrase: {0}".format(redactedProgram))

def main():


    #redactCount = 0
    print("Message Redaction")

    # while True:
    #     program = input("\nType a phrase (or quit to exit program): ").lower()
    #     if program == "quit":
    #         print("End of program")
    #         break
    #     lettersToRedact = input("Type a comma-seperated list of letters to redact: ").lower()
    #     redaction = lettersToRedact.split(',')

    #     for letter in redaction:
    #         redactedProgram = program.replace(letter, "_")
    #         redactCount += program.count(letter)
    #         program = redactedProgram

        
    #     print("Numbers of letters redacted: {0}".format(redactCount))
    #     print("Redacted Phrase: {0}".format(redactedProgram))
    x()

main()