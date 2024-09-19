import random
moves = ['rock', 'paper', 'scissors']


def intro():
    print("\nWelcome to Rock Paper Scissors!")
    if input == "Exit":
        print("Game Over!")
        quit()
    elif input == "Start":
        game.play_game()


"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return

    def learn(self, my_move, their_move):
        pass


class RockPlayer(Player):
    def move(self):
        return "rock"

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)

    def learn(self, my_move, their_move):
        pass


class HumanPlayer(Player):
    def move(self):
        while True:
            move = input("\nRock, Paper, or Scissors? ").lower()
            if move in ["rock", "paper", "scissors"]:
                return move
            else:
                print("Please try again.")

    def learn(self, my_move, their_move):
        pass


class ReflectPlayer(Player):
    def __init__(self):
        super().__init__()
        self.human_last_move = None

    def learn(self, my_move, their_move):
        self.human_last_move = their_move

    def move(self):
        if self.human_last_move is None:
            return random.choice(moves)
        else:
            return self.human_last_move


class CyclePlayer(Player):
    def __init__(self):
        super().__init__()
        self.last_move = None

    def learn(self, my_move, their_move):
        self.last_move = my_move

    def move(self):
        moves = ['rock', 'paper', 'scissors']
        if self.last_move is None:
            return random.choice(moves)
        else:
            current_index = moves.index(self.last_move)
            return moves[(current_index + 1) % 3]


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2, rounds):
        self.p1 = p1
        self.p2 = p2
        self.rounds = rounds
        self.p1score = 0
        self.p2score = 0
        self.rounds_played = 0

    def play_round(self):

        print(f"Player 1 Score {self.p1score}")
        print(f"Player 2 Score {self.p2score}")
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}\nPlayer 2: {move2}")

        if beats(move1, move2):
            self.p1score += 1
            print("Player 1 Wins the round!")

        elif beats(move2, move1):
            self.p2score += 1
            print("Player 2 Wins the round!")

        else:
            print("Game Tied!")

        self.rounds_played += 1
        print(f"Round {self.rounds_played}:")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        while self.rounds_played < self.rounds:
            self.play_round()
        print(f"\nFinal Score for Player 1:{self.p1score}")
        print(f"Final Score for Player 2:{self.p2score}\n")
        if self.p1score > self.p2score:
            print("Player 1 has Won!\n")
        if self.p1score < self.p2score:
            print("Player 2 has Won!\n")
        print("Game over!\n")


if __name__ == '__main__':
    intro()
# create a game here to set type of player and number of round(s)
    game = Game(HumanPlayer(), RandomPlayer(), 5)
    game.play_game()