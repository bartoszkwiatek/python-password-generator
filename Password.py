import random
import string


class Password:
    number_of_characters = 8

    def __init__(self):
        self.password = ''
        self.number_of_characters = None


    def char_pool(self, big_letters, special_signs, numbers):      #pula znaków używanych do generowania hasła
        pool = string.ascii_lowercase

        if big_letters == True:
            pool += string.ascii_uppercase

        if special_signs == True:
            pool += string.punctuation

        if numbers == True:
            pool += string.digits
        return pool


    def generate_random(self, number_of_characters=8, big_letters=True, special_signs=False, numbers=True):
        pool = self.char_pool(big_letters, special_signs, numbers)
        temp_password = str()
        for each_char in range(number_of_characters):
            temp_password += random.choice(pool)
        self.password = temp_password
        print(pool)


  #  def first_big(self):                    #
 #       temp_password=generate_random()


#    def numbers_last(self):
#        temp_password = self.password



kupa = Password()                   # kupa jest obiektem klasy Password
kupa.generate_random()  # używamy na kupie metody "generate_random" z klasy Password, podając jako argument własny atrybut - number_of_characters
print(kupa.password)
#kupa.first_big()
print(kupa.password)
