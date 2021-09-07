from random import randint
words = ("mouse","television","monitor","door","keyboad")
is_over = False
flag = True
word = []
str = ""
missing_str = ""
missing_words = []
missing_counter = 0
ran = randint(0, 4)
fail = 0
while not is_over:
    word_length = len(words[ran])
    for i in range(word_length):
        word.append("_")
        str += word[i]
    print (str)
    flag = False
    while flag == False:
        print("guess a letter")
        guess = input(">")
        if guess in word:
            print("already exists in the secret word")
        if guess in words[ran]:
            for i in range(word_length):
                if guess in words[ran][i]:
                    word[i] = guess
        else:
            if guess not in missing_words:
                missing_words.append(guess)
                missing_counter += 1
                fail += 1
            else:
                print("you already typed this letter")
        str = ""
        missing_str = ""
        for i in range(word_length):
            str += word[i]
        for i in range(missing_counter):
            missing_str+= missing_words[i] + ", "

        print(f"already used: {missing_str}")
        print(str)
        if "_" not in word:
            is_over = True
            print("you won the game!")
            break
        if fail == 10:
            print("you lost the game")



















