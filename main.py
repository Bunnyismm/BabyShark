"""----------------------------------------------------------------
Name:       Ethan Replogle
Assignment: Lab - Baby Shark
Course:     CS 1430, Section X, Fall 2026
Purpose:    This program is designed to be practice for Python
            functions

Input: None

Output: The sound Baby Shark, with three verses:
        Baby Shark,
        doo-doo-doo-do-do-do-do *3
        Baby Shark!
        Mommy Shark,
        doo-doo-doo-do-do-do-do *3
        Mommy Shark!
        Daddy Shark,
        doo-doo-doo-do-do-do-do *3
        Daddy Shark!
----------------------------------------------------------------"""

##############
# CONSTANTS
##############
REPEAT = 3

def sharkCall(sharkType):
    for _ in range(REPEAT):
        print(str(sharkType)+",")
        print("doo-doo-doo-do-do-do-do")
    print(str(sharkType)+"!")

def main():
    sharkCall("Baby Shark")
    sharkCall("Mommy Shark")
    sharkCall("Daddy Shark")
    

if __name__ == "__main__":
    main()
