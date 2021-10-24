import random


data = {
    "r": "Rock",
    "p": "Paper",
    "s": "Scissor"
}


def main():
    print("Game Started\n\n")
    while True:
        # keys
        keys = []
        for key in data:
            keys.append(key)
        
        # key of user 
        user_input = "Enter your key." + "\n" + "Some Keys -"
        for key in keys:
            user_input += " " + key + "for " + data[key]
        user_input += "\n:- "
        
        # key of computer/opponent
        computer = random.choice(keys)
        
        # text for print result
        text = "You: " + data[user] + "\n" + "Computer: " + data[computer]+"\n"
        
        # same keys
        if user == computer:
            print(text+"Same")
        
        # win keys
        elif (user == "r" and computer == "s") or (user == "s" and computer == "p") or (user == "p" and computer == "r"):
            print(text+"You won")
        
        # lose keys
        else:
            print(text+"You lose")
        
        # next game 
        next = input("Do you need this game again? 'y' for yes and 'n' for no.\n:- ")
        if next == "y" or next == "yes":
            print("\n\nNext Game")
        else:
            print("Game Finished")
            break


main()
