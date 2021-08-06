def find_alphabet(words):
    # check if a letter of a word is in the alphabet
    # get a list of all letters in the alphabet both lower and upper case
    present_alphabets = []
    upper_case_alphabet = [chr(i) for i in range(65, 91)]
    lower_case_alphabet = [chr(i) for i in range(97, 123)]
    # merge the above lists
    alphabet = upper_case_alphabet + lower_case_alphabet
    # check if each word contains a letter from the alphabet
    for word in words:
        for letter in word:
            if letter in alphabet:
                present_alphabets.append(letter)
    # return the alphabet with the letters that are present in the words
    return present_alphabets