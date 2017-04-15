import random
import string
import re

number_of_characters = 20

def char_pool(big_letters, special_signs, numbers):  # pula znaków używanych do generowania hasła
    pool = string.ascii_lowercase

    if big_letters == True:
        pool += string.ascii_uppercase

    if special_signs == True:
        pool += string.punctuation

    if numbers == True:
        pool += string.digits
    return pool


def generate_random(number_of_characters=8, big_letters=True, special_signs=True, numbers=True):
    temp_password = str()
    for each_char in range(number_of_characters):
        temp_password += random.choice(char_pool(big_letters, special_signs, numbers))
    password = temp_password
    return password


def first_big_numbers_last(number_of_characters=11, number_of_numbers=3):
    temp_password_first = str(random.choice(string.ascii_uppercase))
    temp_password_middle = str(generate_random(number_of_characters-1-number_of_numbers, False, False, False))
    temp_password_end = str()
    for each_char in range(number_of_numbers):
        temp_password_end += random.choice(string.digits)
    password = temp_password_first+temp_password_middle+temp_password_end
    return password


def mixed(number_of_characters=20):
    vowels=['a','e','u','i','o']
    others=list(string.ascii_lowercase)
    password= ''

    for vowel in range(len(vowels)):
        others.remove(vowels[vowel])

    for sign in range(number_of_characters):
        if sign%2==0:
            password+=random.choice(others)
        else:
            password+=random.choice(vowels)
    return password


def words_list_cleaning():
    words_list = open('words','r')
    content_of_document = list(words_list.readlines())
    words_list.close()

    for each_line in range(len(content_of_document)):       #modyfikacja ponieważ lista słow ma entery
        word=re.sub('\n','',content_of_document[each_line])
        content_of_document[each_line]=word

    return content_of_document


def words_pass(number_of_characters=20):
    password = str()
    words = words_list_cleaning()

    while len(password) != number_of_characters:

        if len(password) < number_of_characters:
            rest = number_of_characters-len(password)

            if rest > 6:
                temp_password = random.choice(words)
                password += temp_password.capitalize()

            else:
                random_word = random.choice(words)

                if len(random_word) == rest:
                    password += random_word.capitalize()

                else:
                    continue

        elif len(password)>= number_of_characters:
            password=str('')

    return password

print(generate_random(number_of_characters))
print(first_big_numbers_last(number_of_characters))
print(mixed(number_of_characters))
print(words_pass(number_of_characters))

file = open('/home/bartek/Documents/program/pass.txt','w')
file.write(generate_random(number_of_characters)+'\n'+
first_big_numbers_last(number_of_characters)+'\n'+
mixed(number_of_characters)+'\n'+
words_pass(number_of_characters))
file.close()
