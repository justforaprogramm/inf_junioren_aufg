class Main:
    def __init__(self) -> None:
        self.input = self.input()
        self.result = self.calc()
    def input(self) -> str:
        used_input = input('Do u want to use a stored input?(yes or NO):')

        if used_input.strip.lower is 'yes':
            print(Json.call_strings())
            use_input = input(f'which given number from {Json.call_string_number()} do u want to use?:')
            return Json.give_complete_string(use_input)

        else:
           new_input = input('give new input:')
           return new_input
        
    def calc(self):
        ...
    def __str__(self):
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
