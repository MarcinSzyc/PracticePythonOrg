while True:
    print('This is rock, paper, scisors game. Google the rules.')
    print(' Use R for Rock \n P for Paper \n S for scissors')
    test = ''
    player1 = input("Player 1: Please provide your choice here: ").lower()
    player2 = input("Player 2: Please provide your choice here: ").lower()
    test = player1 + player2

    if player1 == player2:
        l = input('Duce, do you want to try again? (Y/N)')
        if l.lower() == 'n':
            break
        else:
            continue
    else:
        if test == 'rs' or test == 'pr' or test == 'sp':
            print('Player 1 wins')
            if input('Do you want to play again? (Y/N) ') == 'n'.lower():
                break
            else:
                continue
        if test == 'sr' or test == 'rp' or test == 'ps':
            print('Player 2 wins!')
            if input('Do you want to play again? (Y/N ') == 'n'.lower():
                break
            else:
                continue
