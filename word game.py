from random import randint

firstLetter = True
invalid = False
score = 0
randLetter = randint(0, 27)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',' k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
words = []
answers = []

with open("w.txt") as f:
    for line in f:
        a = line.rstrip()
        words.append(a)

print(f"Score: {score}")

msg = input(f"Enter a word beginning with {letters[randLetter]}: ").lower()
answers.append(msg)


if msg[0] != letters[randLetter]:
    firstLetter = False
elif msg not in words or msg.isalpha() is False:
    invalid = True
else:
    score += len(msg)
    print(score)
    pass


while True:

    if firstLetter is False:
        print("Game over! You didn't enter a word that begins with the starting letter.")
        break
    elif invalid is True:
        print(f"Game over! Your word is not in the dictionary file, and/or it has an invalid character. Score: {score}")
        break
    else:
        pass

    
    last_character = msg[-1]


    msg = input(f"Enter a word beginning with {last_character}: ").lower()
    
    if msg in answers:
        print(f"Game over! You repeated yourself. Score: {score}")
        break
    else:
        answers.append(msg)
        pass
    
    if msg not in words or msg.isalpha() is False:
        print(f"Game over! Your word isn't in the dictionary file, and/or your word has an invalid character. Score: {score}")
        break
    else:
        pass
        
    first_character = msg[0]
    
    
    if last_character == first_character:
        score += len(msg)
        print(f"length: {len(msg)}")
        print(f"score: {score}")
        
    else:
        print(f"Game over! You didn't match the last letter of the last word and the first letter of the current word. Score: {score}")
        break
