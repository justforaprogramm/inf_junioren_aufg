from functools import cache
import string
from typing import List

class Main:
    def __init__(self) -> None:
        """initalize step by step all functions to prepare for print
        """
        self.input = self.input()
        self.shit_str = self.check()
        if len(self.shit_str) > 1:
            print(self.shit_str)
            exit()
        #Json.store_string() = self.input
        self.result = self.calc()

    def input(self) -> str:
        """asks which str user wants, give option to give new string

        Returns:
            str: a text who should be checkt
        """
        used_input = str(input('Do u want to use a stored input?(yes or NO):'))

        if used_input.lower().strip() == 'yes':
            print(Json.call_strings())
            use_input = input(f'which given number from {Json.call_string_number()} do u want to use?:')
            return Json.give_complete_string(use_input)

        new_input = str(input('give new input(str):'))
        return new_input
    
    def check(self) -> str:
        """checks if string is long enough

        Returns:
            str: Error description if fail
        """
        if len(self.input) < 2:
            return f'{self.input} is to short'
        return ''
    
    def calc(self) -> str:
        """calculates which starting point gets out of bounds first

        Returns:
            str: winner of texthopsen
        """
        input_length = len(self.input)
        start0 = [0, 0]
        start1 = [0, 1]
        temp_num = 0

        while start0[1] < input_length:
            temp_num = start0[1]
            start0[1] += self.ording(start0[1])
            if temp_num == start0[1]:
                start0[1] += 1 
            else:
                start0[0] += 1

        while start1[1] < input_length:
            temp_num = start1[1]
            start1[1] += self.ording(start1[1])
            if temp_num == start1[1]:
                start1[1] += 1 
            else:
                start1[0] += 1
        
        if start0[0] == start1[0]:
            return 'first and second'
        elif start0[0] < start1[0]:
            return 'first'
        else:
            return 'second'

    @cache
    def ording(self, index) -> int:
        """returns for a letter which it is in the alphabet

        Args:
            index (int): which letter from string should be checkt

        Returns:
            int: the number of the letter in a alphabet
        """
        if self.input[index].lower() in string.ascii_lowercase:
            return ord(self.input[index].lower()) -96
        return index

    def __str__(self) -> str:
        """get the winner and make a sentence out of it

        Returns:
            str: result in printform
        """
        return f'the winner is the {self.result} person.'
    
class Json:
    def __init__(self):
        ...
    def store_string(self) -> None:
        ...
    def call_strings(self) -> List[str]:
        ...
    def call_string_number(self) -> int:
        ...
    def give_complete_string(self) -> str:
        ...

if __name__ == '__main__':
    print(Main())
