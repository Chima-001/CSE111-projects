''' I added an extra extra feature: generate_password function (lines 78-96) to enable the user generate 
random but strong passwords, print and automatically test the strength of the generated password (lines 104-107).
Also, I used the built in list() funtion to get the all alphabets (lowercase and uppercase), digits and
special characters instead of manually typing/pasting in the characters.'''

import random
import string

def word_in_file(word, filename= 'wordlist.txt', case_sensitive= False):
    with open(filename, 'r', encoding= 'utf-8') as file:
        
        for line in file:
            line =  line.strip()

            if not case_sensitive:
                if word.casefold() == line.casefold():
                    return True
            if word == line:
                return True
        return False

LOWER = list(string.ascii_lowercase)
UPPER = list(string.ascii_uppercase)
DIGITS = list(string.digits)
SPECIAL = list(string.punctuation)

def word_has_character(word, character_list):

    for char in word:
        if char in character_list:
            return True
    return False

def word_complexity(word):
    complexity_points = 0
    if word_has_character(word, LOWER):
        complexity_points += 1
    if word_has_character(word, UPPER):
        complexity_points += 1
    if word_has_character(word, DIGITS):
        complexity_points += 1
    if word_has_character(word, SPECIAL):
        complexity_points += 1
    return complexity_points

def password_strength(password, min_length= 10, strong_length= 16):
    strength = 0

    with open('wordlist.txt', 'r', encoding= 'utf-8') as file:
        for line in file:
            line =  line.strip()
            if password == line:
                print('Password is a dictionary word and is not secure.')
                return 0
            
    with open('toppasswords.txt', 'r', encoding= 'utf-8') as file:
        for line in file:
            line =  line.strip()
            if password == line:
                print('Password is a commonly used password and is not secure.')
                return 0
            
    if len(password) < min_length:
        print('Password is too short and is not secure.')
        strength = 1
    elif len(password) >= min_length and word_complexity(password) == 2:
        strength = 3
    elif len(password) >= min_length and word_complexity(password) == 3:
        strength = 4
    elif len(password) >= min_length and word_complexity(password) == 4:
        strength = 5
    elif len(password) >= min_length and len(password) < strong_length:
        strength = 2
    elif len(password) >= strong_length:
        print('Password is long, length trumps complexity. This is a good password.')
        strength = 5
    return strength

def generate_password(length):

    all_chars = []
    all_chars += UPPER
    all_chars += LOWER
    all_chars += DIGITS
    all_chars += SPECIAL

    password = []
    password.append(random.choice(UPPER))
    password.append(random.choice(LOWER))
    password.append(random.choice(DIGITS))
    password.append(random.choice(SPECIAL))
    
    for i  in range(length - len(password)):
        password.append(random.choice(all_chars))

    random.shuffle(password)
    return ''.join(password)

def main():
    while True:
        password = input('Enter password, \'g\' to generate and test or \'q\' to quit: ')

        if password.lower() == 'q':
            break
        elif password.lower() == 'g':
            password = generate_password(16)
            print(password)
            print(password_strength(password))
        else:
            print(password_strength(password))
            
if __name__ == '__main__':
    main()