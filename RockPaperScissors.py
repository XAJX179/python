import random

def _game_func(x,y):
    if x == 1 and  y==3:
        return a
    elif x==2 and y==1:
        return a
    elif x==3 and y==2:
        return a
    elif x==y:
        return None
    else:
        return b

listy = ["Rock","Paper","Scissors"]
a = random.randint(1,3)
b = int(input("Enter Rock(1) , Paper(2), Scissors(3)  ᕦ( ͡° ͜ʖ ͡°)ᕤ  :"))

winner = _game_func(a,b)
if a==b:
        print("Tie! ( ͡° ͜ʖ ͡°)")
if winner==b:
    print(f'''Computer:{listy[a-1]}
You:{listy[b-1]}
You Won!!!''')
elif winner==a:
    print(f'''Computer:{listy[a-1]}
You:{listy[b-1]}
You Lost!!!  ᕦ( ͡° ͜ʖ ͡°)ᕤ Hehe''')