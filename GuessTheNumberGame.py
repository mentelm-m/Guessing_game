"""This is one of the simple python projects yet an exciting one. You can even call it a mini-game.
Make a program in which the computer randomly chooses a number between 1 to 10, 1 to 100, or any range.
Then give users a hint to guess the number.
Every time the user guesses wrong, he gets another clue, and his score gets reduced.
The clue can be multiples, divisible, greater or smaller, or a combination of all."""
import Game


def main():

    # initialize the game object
    game = Game.Game()
    
    # Print out the welcome messages, set the player name, start the game
    game.welcome()
    game._id_name = input()
    game.start_game()

    # Test print of Game id
    # print(game._id)

    while True:
        player = input()
        try:
            player = int(player)
        except ValueError:
            if type(player) != int:
                print('You have to input a number. Try again: ', end='')
                continue

        guessed_number = game.guess(player)

        if not guessed_number and game.moves != 0:
            print(f'You won, {game.id_name}. Good job!')
            print(f'Final score: {game.score}/1000!')
            break

        if game.moves == 0:
            print(f'Number was {game.number}')  # later, when DONE, uncomment the first part of this line
            print(f'Final score: {game.score}/1000!')
            break

        if player > game.number:
            # print(f'Score: {game.score}')
            print('Try smaller number.')
        elif player < game.number:
            # print(f'Score: {game.score}')
            print("Try bigger number.")


if __name__ == '__main__':
    main()
