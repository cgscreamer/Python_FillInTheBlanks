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

Game_One_Level = ["Easy", "easy"]

Game_Two_Level = ["Medium", "medium"]

Game_Three_Level = ["Hard", "hard"]

tests = [First_Test, Second_Test, Third_Test]
answers = [First_Test_Answers, Second_Test_Answers, Third_Test_Answers]

LEVELS = ["easy", "medium", "hard"]

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
    index = 0
    choose_level = None
    for level in LEVELS:
        if difficulty == level.lower():
            choose_level = index
        index += 1

    if choose_level == None:
        print "Wrong level."
        exit()
    chosen_test = tests[chose_level]
    chosen_answers = answers[chose_level]
    game(chosen_test, chosen_answers)

def Game_Restart():
    #For after the game has completed, if the player wants to play again
    restart = raw_input('Would you like to play again? (yes/no): ')
    if restart in Affirmative:
        return Get_Started()
    else:
        print "Ok, See you later, Alligator!"

def game(test, answers):
    def play_game(level):
#Example function with PEP 484 type annotations.
#    Input:
#        level (test): Test filled with blanks
#    Behavior:
#        For a given level it launches the main game logic.
#        It checks the user input.
#        If the user guesses right the current blanks is replaced
#        with the right answer then the quiz is print.
#        This process happens until all blanks are found
#    Return:
#        None.
#    """
        index = 0
    for answer in answers:
        print test
        check_answer(answer, index)
        test = test.replace(blanks[index], answer)
        index += 1
    print test

def check_answer(answer, index):
    index = 0
    user_input = raw_input("What goes into slot" + blanks[blanks_index] + ": ")
    attempts = 5
    while user_input != answer:
         attempts -=1
         print "\nYour answer was wrong. Try again.\n" + "Remaining attempts" + attempts
         user_input = raw_input("Type it here again: ")
         if attempts ==0:
             print "You have no gueeses left! Sorry!!! "
             Game_Restart()
#       # for you to implement
#       # print "try again" message
#       # decrement attempts
#       # ask user input again
#       # if attempts == 5 use print a message and use exit() to quit

###########################################
# Hopefully the fruit of all this labour

def Get_Started():
    #Starts the game and greets the player
    greeting()
    begin = raw_input("Would you like to begin? [Type: yes/no]: ")
    if begin in Affirmative:
        print "Fantastic! Let's begin:"
        print " "
        return get_setup()
    elif begin == "no":
        print "Thanks for stopping by! Now...RUN!!"


Get_Started()
