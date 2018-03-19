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

####################
# Games

def Game_One():
    print First_Test
    First_Test_Q1 = raw_input('What goes into slot ___1___?: ')
    while First_Test_Q1 != First_Test_Answers[0]:
        print "\nYour answer was wrong. Try again.\n"
        First_Test_Q1 = raw_input("Type it here again: ")

    print "\nWell done! That's correct!\n"

    First_Test_1 = (First_Test.replace(blanks[0], First_Test_Answers[0]))
    print First_Test_1
    First_Test_Q2 = raw_input("What goes into slot ___2___?: ")
    while First_Test_Q2 != First_Test_Answers[1]:
        print "\nYour answer was wrong. Try again.\n"
        First_Test_Q2 = raw_input("Type it here again: ")
    print "\nWell done! That's correct!\n"

    First_Test_2 = (First_Test_1.replace(blanks[1], First_Test_Answers[1]))
    print First_Test_2
    First_Test_Q3 = raw_input("What goes into slot ___3___?: ")
    while First_Test_Q3 != First_Test_Answers[2]:
        print "\nYour answer was wrong. Trry again.\n"
        First_Test_Q3 = raw_input("Type it here again: ")
    print "\nWell done! That's correct!\n"

    First_Test_3 = (First_Test_2.replace(blanks[2], First_Test_Answers[2]))
    print First_Test_3
    First_Test_Q4 = raw_input("What goes into slot ___4___?: ")
    while First_Test_Q4 != First_Test_Answers[3]:
        print "\nYour answer was wrong. Trry again.\n"
        First_Test_Q4 = raw_input("Type it here again: ")
        print "\nWell done! That's correct!\n"
    First_Test_4 = (First_Test_3.replace(blanks[3], First_Test_Answers[3]))
    print " "
    print First_Test_4
    print " "
    print "You got everything correct! You Genius!!"
    print " "
    Game_Restart()

def Game_Two():
    print Second_Test
    Second_Test_Q1 = raw_input('What goes into slot ___1___?: ')
    while Second_Test_Q1 != Second_Test_Answers[0]:
        print "\nYour answer was wrong. Try again.\n"
        Second_Test_Q1 = raw_input("Type it here again: ")

    print "\nWell done! That's correct!\n"

    Second_Test_1 = (Second_Test.replace(blanks[0], Second_Test_Answers[0]))
    print Second_Test_1
    Second_Test_Q2 = raw_input("What goes into slot ___2___?: ")
    while Second_Test_Q2 != Second_Test_Answers[1]:
        print "\nYour answer was wrong. Trry again.\n"
        Second_Test_Q2 = raw_input("Type it here again: ")
    print "\nWell done! That's correct!\n"

    Second_Test_2 = (Second_Test_1.replace(blanks[1], Second_Test_Answers[1]))
    print Second_Test_2
    Second_Test_Q3 = raw_input("What goes into slot ___3___?: ")
    while Second_Test_Q3 != Second_Test_Answers[2]:
        print "\nYour answer was wrong. Trry again.\n"
        Second_Test_Q3 = raw_input("Type it here again: ")
    print "\nWell done! That's correct!\n"
    Second_Test_3 = (Second_Test_2.replace(blanks[2], Second_Test_Answers[2]))
    print Second_Test_3
    Second_Test_Q4 = raw_input("What goes into slot ___4___?: ")
    while Second_Test_Q4 != Second_Test_Answers[3]:
        print "\nYour answer was wrong. Trry again.\n"
        Second_Test_Q4 = raw_input("Type it here again: ")
        print "\nWell done! That's correct!\n"
        print " "
    Second_Test_4 = (Second_Test_3.replace(blanks[3], Second_Test_Answers[3]))
    print Second_Test_4
    print " "
    print "You got everything correct! You Genius!!"
    print " "
    Game_Restart()

def Game_Three():
    print Third_Test
    Third_Test_Q1 = raw_input('What goes into slot ___1___?: ')
    while Third_Test_Q1 != Third_Test_Answers[0]:
        print "\nYour answer was wrong. Try again.\n"
        Third_Test_Q1 = raw_input("Type it here again: ")

    print "\nWell done! That's correct!\n"

    Third_Test_1 = (Third_Test.replace(blanks[0], Third_Test_Answers[0]))
    print Third_Test_1
    Third_Test_Q2 = raw_input("What goes into slot ___2___?: ")
    while Third_Test_Q2 != Third_Test_Answers[1]:
        print "\nYour answer was wrong. Trry again.\n"
        Third_Test_Q2 = raw_input("Type it here again: ")
    print "\nWell done! That's correct!\n"

    Third_Test_2 = (Third_Test_1.replace(blanks[1], Third_Test_Answers[1]))
    print Third_Test_2
    Third_Test_Q3 = raw_input("What goes into slot ___3___?: ")
    while Third_Test_Q3 != Third_Test_Answers[2]:
        print "\nYour answer was wrong. Trry again.\n"
        Third_Test_Q3 = raw_input("Type it here again: ")
    print "\nWell done! That's correct!\n"

    Third_Test_3 = (Third_Test_2.replace(blanks[2], Third_Test_Answers[2]))
    print Third_Test_3
    Third_Test_Q4 = raw_input("What goes into slot ___4___?: ")
    while Third_Test_Q4 != Third_Test_Answers[3]:
        print "\nYour answer was wrong. Trry again.\n"
        Third_Test_Q4 = raw_input("Type it here again: ")
        print "\nWell done! That's correct!\n"
        print " "
    Third_Test_4 = (Third_Test_3.replace(blanks[3], Third_Test_Answers[3]))
    print Third_Test_4
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