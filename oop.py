import random
print("Welcome to the guess number game :D \nyou need to guess the correct number")
class Guess_number:
        def __init__(self, random_num=0):
            self.r = random_num
        def generate_random_num(self):
            self.r = random.randrange(11)
            return self.r
        def check(self, user_guess):
            if user_guess == Guess_number.generate_random_num(self):
                print("The random number is: ", self.r, "\nBravo you guessed the correct number")
            else:
                print("The random number is: ", self.r, "Unfortunately, you guessed the wrong number")
class Play(Guess_number):
    def __init__(self, random_num, score):
        self.s = score
        super().__init__(random_num)
    def go(self):
        curr = self.s

        while curr != 0:
            curr = curr - 1
            while Guess_number.check(self, user_guess= int(input("Enter your guess number:"))):
                print("Your score is: ", curr - 1)
                if curr == 0:
                    break
            else:
                print(curr)
        else:
            print("Game over")
y = Play(0, 5)
y.go()