from math import floor

# One definition program to check if an user-inputted word
# or phrase is a palindrome. Most of the program is fairly self-explanatory.
# First, check if the word/phrase in question only contains alphabetic
# characters. Then, based on if the word has an even or odd number of letters,
# begin comparing each letter near the beginning to the corresponding word
# near the end.
def palindromeChecker():
    word = input("Please enter a word: ")
    if not word.isalpha():
        print("Word is invalid, exiting program.")
    elif len(word) % 2 == 0:
        leftIndex = 0
        rightIndex = len(word) - 1
        while leftIndex != (len(word) / 2):
            if word[leftIndex] == word[rightIndex]:
                leftIndex += 1
                rightIndex -= 1
            else:
                print("\'" + word + "\' is not a palindrome.")
                leftIndex = -1
                break
        if leftIndex != -1:
            print("\'" + word + "\' is a palindrome!")
    else:
        leftIndex = 0
        rightIndex = len(word) - 1
        while leftIndex != floor(len(word) / 2):
            if word[leftIndex] == word[rightIndex]:
                leftIndex += 1
                rightIndex -= 1
            else:
                print("\'" + word + "\' is not a palindrome.")
                leftIndex = -1
                break
        if leftIndex != -1:
            print("\'" + word + "\' is a palindrome!")
    answer = input("Would you like to use this program again? Type in " +\
        "\'Yes\' if you  would or \'No\' if not: ")
    if(answer == 'Yes'):
        palindromeChecker()
    elif(answer == 'No'):
        print("Thank you for using my program. Have a great day!")
    else:
        print("Invalid input. Ending program...")
    return

palindromeChecker()

