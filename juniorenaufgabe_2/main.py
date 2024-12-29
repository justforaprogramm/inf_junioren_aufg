from functools import cache
from string import ascii_lowercase

class Main:
    def __init__(self) -> None:
        """initalize step by step all functions to prepare for print
        """
        self.Txt = Data()

        self.input = self.input()
        self.shit_str = self.check()
        if len(self.shit_str) > 1:
            print(self.shit_str)
            exit()
        self.Txt.store_string(self.input)
        self.result = self.calc()

    def input(self) -> str:
        """asks which str user wants, give option to give new string

        Returns:
            str: a text who should be checkt
        """
        used_input = str(input('Do u want to use a stored input?(yes or NO):'))

        if used_input.lower().strip() == 'yes' and self.Txt.call_string_number() < 1:
            print(self.Txt.call_strings())
            use_input
            while use_input > 0 and use_input <= self.Txt.call_string_number():
                try:
                    use_input = int(input(f'which given number from 0 to {self.Txt.call_string_number()} do u want to use?:'))
                except ValueError:
                    print('given input has to be a number')
                    use_input = 1
            return self.Txt.give_complete_string(use_input)

        new_input = str(input('give new input(str):'))
        return new_input
    
    def check(self) -> str:
        """checks if string is long enough

        Returns:
            str: Error description if fail
        """
        if len(self.input) < 5:
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
    def ording(self, index:int) -> int:
        """returns for a letter which it is in the alphabet

        Args:
            index (int): which letter from string should be checkt

        Returns:
            int: the number of the letter in a alphabet
        """
        if self.input[index].lower() in ascii_lowercase:
            return ord(self.input[index].lower()) -96
        return index

    def __str__(self) -> str:
        """get the winner and make a sentence out of it

        Returns:
            str: result in printform
        """
        return f'the winner is the {self.result} person.'
    
class Data:
    def __init__(self):
        """look if file exist in path, if not, create it
           and make some file calls to reduce time later
        """
        self.filename = './juniorenaufgabe_2/data.txt'

        try:
            open(self.filename, 'x').close()
        except FileExistsError:
            ...

        with open(self.filename, 'r') as file:
            self.filecontent = file.readlines()
    
    def store_string(self, contains:str) -> None:
        """store given string in file

        Args:
            contains (str): content of str
        """
        with open(self.filename, 'a') as file:
            file.write('\n' + contains)

    def call_strings(self) -> str:
        """look up the first 5 character of each line

        Returns:
            str: formatet first characters
        """
        res = ''
        line_num = 0
        for lines in self.filecontent:
            line_num += 1 
            res += (f'{line_num}:' + lines[:5] + '...\n')
        return res

    @cache
    def call_string_number(self) -> int:
        """sum up lines in file

        Returns:
            int: number of lines
        """
        return sum(1 for _ in open(self.filename))
    
    def give_complete_string(self, line_number:int) -> str:
        """give filecontent of specific line

        Args:
            line_number (int): the number of the line which content shoud be returnd

        Returns:
            str: content of line
        """
        return self.filecontent[line_number]

if __name__ == '__main__':
    print(Main())
