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
    print 'What Level would you like to try? Easy/Medium/Hard?'
    difficulty = raw_input("Choose a Level: ")

    if difficulty in Game_One_Level:
        print "\nYou chose: Easy.\n"
        return Game_One()

    elif difficulty in Game_Two_Level:
        print "\nYou chose: Medium \n"
        return Game_Two()

    elif  difficulty in Game_Three_Level:
        print "\nYou chose: Hard \n"
        return Game_Three()

    else:
        return Game_Restart()

def Game_Restart():
    restart = raw_input('Would you like to play again? (yes/no): ')
    if restart in Affirmative:
        return Get_Started()
    else:
        print "Ok, See you later, Alligator!"

def check_answer_First_Test(user_input, First_Test_Answers, blanks_index):
    '''
    This is used to validate user answers with our correct answers list.
    '''

    if user_input == First_Test_Answers[blanks_index]:
        return "Correct"
    else:
        return "Wrong"
    pass

def check_answer_Second_Test(user_input, Second_Test_Answers, blanks_index):
    '''
    This is used to validate user answers with our correct answers list.
    '''

    if user_input == Second_Test_Answers[blanks_index]:
        return "Correct"
    else:
        return "Wrong"
    pass

def check_answer_Third_Test(user_input, Third_Test_Answers, blanks_index):
    '''
    This is used to validate user answers with our correct answers list.
    '''

    if user_input == Third_Test_Answers[blanks_index]:
        return "Correct"
    else:
        return "Wrong"
    pass

###########################################
# Games

def Game_One():
    First_Test = "[Options: market, grandmother, wolf, basket] Little Red Riding Hood went to the ___1___ to buy her ___2___ some apples.On her way through the forest, she saw a scary ___3___ that she ran away from but dropped her ___4___ . She was awfully sad!"
    print First_Test
    blanks_index = 0
    while blanks_index < len(blanks):
        user_input= raw_input("What goes into slot" + blanks[blanks_index] + ": ")
        while user_input != First_Test_Answers[blanks_index]:
            print "\nYour answer was wrong. Try again.\n"
            user_input = raw_input("Type it here again: ")
        else:
            print "nice job! that is the right answer!\n"
            if check_answer_First_Test(user_input, First_Test_Answers, blanks_index) == "Correct":
                First_Test = First_Test.replace(blanks[blanks_index],user_input)
                blanks_index += 1
                print First_Test
                if blanks_index == len(blanks):
                    print " "
                    print "You got everything correct! You Genius!!"
                    print " "
                    Game_Restart()

def Game_Two():
    Second_Test = "[Options: pie, affectionate, cry, play,] Georgie Porgie Pudding and ___1___. Kissed the girls and made them ___2___. When the boys came out to ___3___. He kissed them to cause he was very ___4___ that way."
    print Second_Test
    blanks_index = 0
    while blanks_index < len(blanks):
        user_input= raw_input("What goes into slot" + blanks[blanks_index] + ": ")
        while user_input != Second_Test_Answers[blanks_index]:
            print "\nYour answer was wrong. Try again.\n"
            user_input = raw_input("Type it here again: ")
        else:
            print "nice job! that is the right answer!\n"
            if check_answer_Second_Test(user_input, Second_Test_Answers, blanks_index) == "Correct":
                Second_Test = Second_Test.replace(blanks[blanks_index],user_input)
                blanks_index += 1
                print Second_Test
                if blanks_index == len(blanks):
                    print " "
                    print "You got everything correct! You Genius!!"
                    print " "
                    Game_Restart()

def Game_Three():
    Third_Test = "[Options: bread, dead, lamb, school] Mary had a little ___1___, her father shot it ___2___. Now it follows her to ___3___ between two bits of ___4___."
    print Third_Test
    blanks_index = 0
    while blanks_index < len(blanks):
        user_input= raw_input("What goes into slot" + blanks[blanks_index] + ": ")
        while user_input != Third_Test_Answers[blanks_index]:
            print "\nYour answer was wrong. Try again.\n"
            user_input = raw_input("Type it here again: ")
        else:
            print "nice job! that is the right answer!\n"
            if check_answer_Third_Test(user_input, Third_Test_Answers, blanks_index) == "Correct":
                Second_Test = Third_Test.replace(blanks[blanks_index],user_input)
                blanks_index += 1
                print Third_Test
                if blanks_index == len(blanks):
                    print " "
                    print "You got everything correct! You Genius!!"
                    print " "
                    Game_Restart()

###########################################
# Hopefully the fruit of all this labour

def Get_Started():
    greeting()
    begin = raw_input("Would you like to begin? [Type: yes/no]: ")
    if begin in Affirmative:
        print "Fantastic! Let's begin:"
        print " "
        return get_setup()
    elif begin == "no":
        print "Thanks for stopping by! Now...RUN!!"


Get_Started()
