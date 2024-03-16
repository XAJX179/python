import random
score = 0


def _calc_scores():
    global score
    with open('Hi-Score.txt', 'r+') as f:
        x = f.read() or '0'
        high_score = int(x)

        if score <= high_score:
            print(f"Score : {score} , Hi-Score : {high_score}")

        else:
            f.seek(0)
            f.truncate()
            f.write(str(score))
            print(f"New Hi-Score : {score}!!!")


def _game_func(x, y):
    if ((x == 1 and y == 3) or (x == 2 and y == 1) or (x == 3 and y == 2)):
        return 'Computer'
    elif x == y:
        return None
    else:
        return 'Player'


listy = ["Rock", "Paper", "Scissors"]

while True:
    a = random.randint(1, 3)
    b = int(input("Enter Rock(1) , Paper(2), Scissors(3)  ᕦ( ͡° ͜ʖ ͡°)ᕤ  :"))

    winner = _game_func(a, b)

    if winner == None:
        print('''Tie! ( ͡° ͜ʖ ͡°)
        ''')
        _calc_scores()


    elif winner == 'Computer':
        print(f'''Computer:{listy[a-1]}
     You:{listy[b-1]}
    You Lost!!!  ᕦ( ͡° ͜ʖ ͡°)ᕤ Hehe
    ''')
        score = 0
        _calc_scores()


    else:
        score = score + 1
        print(f'''Computer:{listy[a-1]}
     You:{listy[b-1]}
    You Won!!!
    ''')
        _calc_scores()
        
