"""Template Game class"""

import random


class Game:

    _id = 0
    _id_name = ''
    rand_max = 200

    def __init__(self, number=random.randint(0, rand_max), score=1000):
        self.number = number
        self.score = score
        self.moves = 10
        self._id += 1

    def score_multiplier(self, player_guess):
        # Adjustment of score deduction based on difference between player input and the number
        return abs((self.number - player_guess))

    def guess(self, player_guess):
        player_guess = int(player_guess)
        if self.moves == 0:
            self.score = 0
            print("You are out of moves. YOU LOSE!")
            return False                                                        # Returns False for the main while loop to break
        self.moves -= 1

        if player_guess == self.number and type(player_guess) == int:
            return False                                                        # Returns False for the main while loop to break
        elif player_guess != self.number and type(player_guess) == int:
            if self.moves == 0:
                print("You are out of moves. YOU LOSE!")
                self.score = 0
                return False
            if self.score > 0:
                self.score -= self.score_multiplier(player_guess)
            return True                                                         # Returns True for the main while loop to continue

    def welcome(self):
        print('Welcome to Guess the Number - GAME!\n')
        print(f'You have {self.moves} guesses to find the number.')
        print('First, please choose your name: ', end='')

    def start_game(self):
        print('\nPlease input a number between 1 and 200 to start: ', end='')

    @property
    def id_name(self):
        return self._id_name

    @id_name.setter
    def id_name(self, new_id, new_id_name):
        self._id_name = new_id_name

    @id_name.deleter
    def id_name(self):
        del self._id_name

    def __repr__(self):
        return f"Number is {self.number}."


