import string
import random 

characters = list(string.ascii_letters + string.digits + string.punctuation)

generate_answer = input("Do you want to generate a pass? (y/n)")

if generate_answer.lower() == 'y':
    pass_len = input("How long would you like your pass to be?")
    if pass_len.isdigit():
        pass_len = int(pass_len)
        random.shuffle(characters)

        password = [random.choice(characters) for _ in range(pass_len)]

        random.shuffle(password)
        password = "".join(password)
        print(password)

    else:
        print("The password lenght is a number")
else:
    print("Nothing to do")
    quit()
