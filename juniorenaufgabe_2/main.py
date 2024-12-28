class Main:
    def __init__(self) -> None:
        self.input = self.input()
        self.shit_str = self.check()
        if len(self.shit_str) > 1:
            print(self.shit_str)
            exit()
        self.result = self.calc()
    def input(self) -> str:
        used_input = str(input('Do u want to use a stored input?(yes or NO):'))

        if used_input.lower().strip() == 'yes':
            print(Json.call_strings())
            use_input = input(f'which given number from {Json.call_string_number()} do u want to use?:')
            return Json.give_complete_string(use_input)

        new_input = str(input('give new input(str):'))
        return new_input
    
    def check(self) -> str:
        if len(self.input) < 2:
            return f'{self.input} is to short'
        return ''
    
    def calc(self) -> str:
        input = self.input
        input_length = len(input)

        

    def __str__(self) -> str:
        f'the winner is the {self.result} person.'
    
class Json:
    def __init__(self):
        ...
    def store_string(self):
        ...
    def call_strings(self):
        ...
    def call_string_number(self):
        ...
    def give_complete_string(self):
        ...

if __name__ == '__main__':
    print(Main())
