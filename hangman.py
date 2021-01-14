import random

word_bank = ['rainbow', 'computer', 'science', 'programming',
             'python', 'mathematics', 'player', 'condition',
             'reverse', 'water', 'board', 'geeks']


def hangman_game(attempts):
    word = random.choice(word_bank)

    print('🎮 START ... 🎉🎉')

    guesses = ''
    wrong_guesses = 0
    correct_guesses = 0
    turns = attempts

    while turns > 0:
        guess = str(input("Enter guess:"))
        guesses += guess
        print(word)
        # print([c for c in guesses if c in word])
        # print('wrong', [c for c in guesses if c not in word])
        correct = [c if c in guesses else '-' for c in word]
        print()
        print('👉', ''.join(correct))
        print()

        print(len(word), correct_guesses)

        if guess in word:
            print('✔. # turns left: ', turns)
            # correct_guesses = len([[c for c in guesses if c in word]])
            correct_guesses += 1

        if guess not in word:
            turns -= 1
            print('❌. # turns left: ', turns)
            # wrong_guesses = len([c for c in guesses if c not in word])
            wrong_guesses += 1

        if len(word) == len([c for c in guesses if c in word]):

            print('win')

    return "💀💀💀"


print('HANGMAN')

attempts = int(input("# Wrong guesses you want:"))

print(hangman_game(attempts))