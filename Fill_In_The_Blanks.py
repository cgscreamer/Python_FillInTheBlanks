# IPND Stage 2 Final Project

####################
# Variable or getting the basics down, at least

blanks = ["___1___", "___2___", "___3___", "___4___"]

First_Test = "[Options: market, grandmother, wolf, basket] Little Red Riding Hood went to the ___1___ to buy her ___2___ some apples.On her way through the forest, she saw a scary ___3___ that she ran away from but dropped her ___4___ . She was awfully sad!"
Second_Test = "[Options: pie, affectionate, cry, play,] Georgie Porgie Pudding and ___1___. Kissed the girls and made them ___2___. When the boys came out to ___3___. He kissed them to cause he was very ___4___ that way."
Third_Test = "[Options: bread, dead, lamb, school] Mary had a little ___1___, her father shot it ___2___. Now it follows her to ___3___ between two bits of ___4___."

First_Test_Answers = ["market", "grandmother", "wolf", "basket"]
Second_Test_Answers = ["pie", "cry", "play", "affectionate"]
Third_Test_Answers = ["lamb", "dead", "school", "bread"]

Affirmative = ["yes", "Yes", "Y", "y"]

tests = [First_Test, Second_Test, Third_Test]
answers = [First_Test_Answers, Second_Test_Answers, Third_Test_Answers]

LEVELS = ["Easy", "Medium", "Hard"]
EASY = 0
MEDIUM = 1
HARD = 2

Game_One_Level = ["Easy", "easy"]

Game_Two_Level = ["Medium", "medium"]

Game_Three_Level = ["Hard", "hard"]

answer_limit = 3
attempts_limit = 0


####################
# Helper Functions and probably a lot of stuff I broke

def greeting():
    # Say Hello, and give the player a name.
    player_name = raw_input("Hi! What's your name, stranger?  ")
    if player_name == " ":
        print "That's not a name!"
        return greeting()
    elif player_name == "":
        print "That's not a name!"
        return greeting()
    else:
        print "\nGreat! Welcome, " + player_name + ". Let's play a Game! "

def get_setup():
    # Getting the difficulty levels set up correctly
    # lower() transforms the string in all lowercase so you have to specify: `easy, Easy, EAsy, EASy`
        print 'What Level would you like to try? Easy/Medium/Hard?'
        difficulty = raw_input("Choose a Level: ")

        if difficulty in Game_One_Level:
            print "\nYou chose: Easy.\n"
            return tests[EASY], answers[EASY]

        elif difficulty in Game_Two_Level:
            print "\nYou chose: Medium \n"
            return tests[MEDIUM], answers[MEDIUM]

        elif  difficulty in Game_Three_Level:
            print "\nYou chose: Hard \n"
            return tests[HARD], answers[HARD]

        else:
            print "Wrong level."
            Game_Restart()
        chosen_test = tests(difficulty)
        chosen_answers = answers(difficulty)



def Game_Restart():
    #For after the game has completed, if the player wants to play again
    restart = raw_input('Would you like to play again? (yes/no): ')
    if restart in Affirmative:
        return Get_Started()
    else:
        print "Ok, See you later, Alligator!"
        exit()


def check_answer(chosen_test, chosen_answers, index, attempts):
    user_input = raw_input("What goes into slot" + blanks[index] + ": ")
    while user_input == chosen_answers[index]:
        correct_answer(chosen_test, chosen_answers, index)
    if user_input != chosen_answers[index]:
        wrong_answer(chosen_test, chosen_answers, index, attempts)


def correct_answer(chosen_test, chosen_answers, index):
    index = 0
    while index < answer_limit:
        chosen_test = chosen_test.replace(blanks[index], chosen_answers[index])
        print "That's Right!! Well done!"
        print chosen_test
        index += 1
        user_input = raw_input("What goes into slot" + blanks[index] + ": ")
        if index == answer_limit:
            print "You've Won the Game!! Congratulations"
            Game_Restart()

def wrong_answer(chosen_test, chosen_answers, index, attempts):
    if attempts == attempts_limit:
        print "You have no gueeses left! Sorry!!! "
        Game_Restart()
    else:
        attempts -=1
        print "\nYour answer was wrong. Try again. Remaining attempts: " + str(attempts)
        check_answer(chosen_test, chosen_answers, index, attempts)


def game(chosen_test, chosen_answers):
    print chosen_test
    index = 0
    attempts = 5
    for answer in chosen_answers:
        check_answer(chosen_test, chosen_answers, index, attempts)



###########################################
# Hopefully the fruit of all this labour

def Get_Started():
    #Starts the game and greets the player
    greeting()
    begin = raw_input("Would you like to begin? [Type: yes/no]: ")
    if begin in Affirmative:
        print "Fantastic! Let's begin:"
        print " "
        chosen_test, chosen_answers =  get_setup()
        game(chosen_test, chosen_answers)

    elif begin == "no":
        print "Thanks for stopping by! Now...RUN!!"


Get_Started()
