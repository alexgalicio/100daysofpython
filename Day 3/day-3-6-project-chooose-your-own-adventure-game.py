print('Welcome to Treasure Island. Your mission is to find the treasure.')
way = input('There is a two way. Choose between left(l) or right(r)')
if way == "r":
    swim = input('Swim(s) or wait(w) ')
    if swim == 'w':
        door = input('There are two door: Red(r) or blue(b) or Pink(p) ')
        if door == 'p':
            print('You win!')
        else:
            print("It's morbin time!")
    else:
        print("It's morbin time!")
else:
    print("It's morbin time!")
