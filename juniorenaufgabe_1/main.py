from pprint import pprint

class Main():
    def __init__(self, debugmode = False):
        """call functions

        Args:
            debugmode (bool, optional): make a print more if result want to be checked. Defaults to False.
        """
        self.input = self.input()
        self.calc()
        self.debug() if debugmode else ...

    def input(self):
        numberofareas = input('number of intrestet persons:')
        bottom, side = input('which size is the area?(x;y):').split(';')

        return [int(numberofareas), int(bottom), int(side)]

    def calc(self):
        """calculates area squerest
        """
        # difines for calculation
        area = self.input[1] / self.input[2]
        square_num = self.input[0]
        num_dict = {}
        search = []

        # calculation
        for x in range(square_num, int(square_num*1.1)+1):
            for num in range(1, x+1):
                num_dict.setdefault(x, []).append([num, ((num**2)/x) * area]) if (x % num) == 0 else ...

        for squares in num_dict:
            search.append([item[1] for item in num_dict[squares]])
        search = [value for sub in search for value in sub]

        perf_num = min(search, key=lambda x:abs(x-1))
        for squares in num_dict:
            for btmside in num_dict[squares]:
                if btmside[1] == perf_num:
                    # return
                    self.square = squares
                    self.btmside = btmside[0]
                    break;
    

    def __str__(self):
        """get the winner and make a sentence out of it

        Returns:
            str: result in printform
        """
        return f'there are {self.square} squares with {self.btmside} by {int(self.square/self.btmside)} reqtangles in the square the size of {self.input[1] }:{ self.input[2]}.'
    def debug(self) -> None:
        """make additional prints
        """
        print('\nDEBUG PRINT:', end='')
        pprint(self.input)

if __name__ == '__main__':
    print(Main())