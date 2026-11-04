import random

def bot():
    bot_choice = random.choice(["Rock","Paper","Scissor"])
    return bot_choice

def user_input():
    user_choice = str(input("Whats your choice"))
    user_choice = user_choice.title
    return user_choice

def who_wins():
    if bot() == "Scissor" and user_input() =="Paper" or "P":
        print ("The bot chose Scissor and you chose Paper, You lose ☹️")
    if bot() == "Paper" and user_input() == "Scissor" or "Scisor" or "Sccisor" or "Sciisor" or "S":
        print("The Bot chose Paper and you chose Scissors, You win 🙂") 
    if bot() == "Scissor" and user_input() == "Rock" or "Orck" or "Rokc" or "R":
        print("The Bot Chose Scissor and you chose rock, You win 🙂")
    if bot() == "Rock" and user_input() == "Paper" or "P":
        print("The Bot chose Rock and you chose Paper, You win 🙂")
    if bot() == "Paper" and user_input() == "Rock" or "Rokc" or "Orck" or "R":
        print("The Bot chose Paper and you chose Rock, You lose ☹️")
    if bot() == "Rock" and user_input() == "Scissor" or "Scisor" or "Sccisor" or "Sciisor" or "S":
        print("The Bot chose Rock and you chose Scissors, You lose ☹️")

bot()
user_input()
who_wins()
    
    