#DESCRIPTION:
#the user picks a character from a list,
#and inputs their features using
#provided descriptive words in order for the computer to guess which character they picked. 

#all lists the computer will need to reference to are created in the beginning

girl = ('lee ahin', 'heo yoorim', 'song joohee', 'son minjung', 'choi yewon', 'bae yubin', 'kim jisoo', 'kim jennie', 'yoon bomi', 'kim chaewon')

characters_girls = [
    ["Blood Type A", "Born Wonju SK", "Zodiac Libra"],
    ["Blood Type B", "Born SK", "Zodiac Cancer"],
    ["Blood Type B", "Born Gangwon Prov SK", "Zodiac Aries"],
    ["Blood Type O", "Born Seoul SK", "Zodiac Scorpio"],
    ["Blood Type O", "Born Busan SK", "Zodiac Gemini"],
    ["Blood Type O", "Born ChunCheon SK", "Zodiac Virgo"],
    ["Blood Type A", "Born Gunpo SK", "Zodiac Capricorn"],
    ["Blood Type B", "Born Seoul SK", "Zodiac Capricorn"],
    ["Blood Type O", "Born Suwon SK", "Zodiac Leo"],
    ["Blood Type B", "Born SK", "Zodiac Aquarious"]]

character_traits = []

blood = ['Blood Type A', 'Blood Type B', 'Blood Type O']
born = ['Born Wonju SK', 'Born SK', 'Born Seoul SK', 'Born Gangwon Prov SK', 'Born Busan SK', 'Born ChunCheon SK', 'Born Gunpo SK', 'Born Suwon SK']
zodiac = ['Zodiac Libra', 'Zodiac Cancer', 'Zodiac Aries', 'Zodiac Capricorn', 'Zodiac Scorpio', 'Zodiac Gemini', 'Zodiac Leo', 'Zodiac Virgo', 'Zodiac Aquarious']

lists = None

yon = ['Y', 'N']

def game():

    while True:

#the user is able to recieve the game introduction

        print("""
Hello! Welcome to GUESS MY CHARACTER.

You will recieve a list of k-pop idol characters.

Depending on your choice you will be given their characteristics.

The computer will ask you a series of questions in which you shall respond with your characteristics.

The program is case sensitive. 

In the end, the computer will guess who they think your character is.

Now, let's begin.
""")

#the user is able to recieve the list of characters and input their value
        
        print(girl)
        print("")
        user_character = str(input("Now, please copy//paste//enter the name of the character you would like to play with in order to get their characteristics."))
        print(user_character)

#ig the users input is not a character the user will have to continue putting their character in until a value matching in the list of characters is given

        while user_character not in girl:
            print("""
please re-enter a proper value""")
            print(girl)
            user_character = str(input("Now, please copy//paste//enter the name of the character you would like to play with in order to get their characteristics."))
            
            if user_character in girl:
                break

#once the computer knows the character, the user is able to recieve the correct list of characteristics for that character
                
        if user_character == 'lee ahin':
            print(characters_girls[0])
            lists = characters_girls[0]
            break
        elif user_character == 'heo yoorim':
            print(characters_girls[1])
            lists = characters_girls[1]
            break
        elif user_character == 'song joohee':
             print(characters_girls[2])
             lists = characters_girls[2]
             break
        elif user_character == 'son minjung':
            print(characters_girls[3])
            lists = characters_girls[3]
            break
        elif user_character == 'choi yewon':
            print(characters_girls[4])
            lists = characters_girls[4]
            break
        elif user_character == 'bae yubin':
            print(characters_girls[5])
            lists = characters_girls[5]
            break
        elif user_character == 'kim jisoo':
            print(characters_girls[6])
            lists = characters_girls[6]
            break
        elif user_character == 'kim jennie':
            print(characters_girls[7])
            lists = characters_girls[7]
            break
        elif user_character == 'yoon bomi':
            print(characters_girls[8])
            lists = characters_girls[8]
            break
        elif user_character == 'kim chaewon':
            print(characters_girls[9])
            lists = characters_girls[9]
            break

#the user is then prompted a set of questions to help the computer discover characteristics
#first question
     
    blood_type = input("What is your character's blood type?")
    print("")
    character_traits.append(blood_type)

#if the characteristic entered is not in any of the characteristics options, then the user will have to enter the characteristic until a proper entry has been made
#the proper characteristic is appended to a list which will be compared to find out the character later on

    while blood_type not in blood:
        print("")
        print("please re-enter a proper value. copy and paste the answer from your character's respective list, or type it out exactly as written.")
        print("")
        print(lists)
        print("")
        blood_type = input("What is your character's blood type?")
        if blood_type in blood:
            character_traits.append(blood_type)
            break
#second question
        
    born_in = input("Where was your character born?")
    print("")
    character_traits.append(born_in)
    
    while born_in not in born:
        print("")
        print("please re-enter a proper value. copy and paste the answer from your character's respective list, or type it out exactly as written.")
        print("")
        print(lists)
        print("")
        born_in = input("Where was your character born?")
        if born_in in born:
            character_traits.append(born_in)
            break

#third question

    zodiac_sign = input("What is your character's zodiac?")
    print("")
    character_traits.append(zodiac_sign)
    
    while zodiac_sign not in zodiac:
        print("please re-enter a proper value. copy and paste the answer from your character's respective list, or type it out exactly as written.")
        print("")
        print(lists)
        print("")
        zodiac_sign = input("What is your character's zodiac?")
        if zodiac_sign in zodiac:
            character_traits.append(zodiac_sign)
        
#the computer now compares the list of characteristics based on the user's entries to the options of characters
#the computer is able to figure out which character the user had and print what character it thinks it was

#the computer asks the user to play, and if they say yes, it plays the game and then then guesses which character they had
#once the game/guess ends it asks again, and if they say yes it repeats but if they say no then it ends the program

while True:
    yesorno = input("""
Would you like to play GUESS THIS CHARACTER?

Type 'Y' or 'N' """)

    while yesorno.upper() not in yon:
        yesorno = input("""
Would you like to play GUESS THIS CHARACTER?

Type 'Y' or 'N' """)
            
    if yesorno.upper() == 'Y':
        True
        game()
        
#the computer guesses which character the user chose
        
        if character_traits == characters_girls[0]:
            print("The characteristics you have entered match most with Lee Ahin.")
            print("")
            lee = input("Is this your character?")
            print("")
            print("This was fun! Hope to see you next time!")
            character_traits = []

        elif character_traits == characters_girls[1]:
            print("The characteristics you have entered match most with Heo Yoorim.")
            print("")
            lee = input("Is this your character?")
            print("")
            print("This was fun! Hope to see you next time!")
            character_traits = []

        elif character_traits == characters_girls[2]:
            print("The characteristics you have entered match most with Song Joohee.")
            print("")
            lee = input("Is this your character?")
            print("")
            print("This was fun! Hope to see you next time!")
            character_traits = []

        elif character_traits == characters_girls[3]:
            print("The characteristics you have entered match most with Son Minjung.")
            print("")
            lee = input("Is this your character?")
            print("")
            print("This was fun! Hope to see you next time!")
            character_traits = []

        elif character_traits == characters_girls[4]:
            print("The characteristics you have entered match most with Choi Yewon.")
            print("")
            lee = input("Is this your character?")
            print("")
            print("This was fun! Hope to see you next time!")
            character_traits = []

        elif character_traits == characters_girls[5]:
            print("The characteristics you have entered match most with Bae Yubin.")
            print("")
            lee = input("Is this your character?")
            print("")
            print("This was fun! Hope to see you next time!")
            character_traits = []

        elif character_traits == characters_girls[6]:
            print("The characteristics you have entered match most with Kim Jisoo.")
            print("")
            lee = input("Is this your character?")
            print("")
            print("This was fun! Hope to see you next time!")
            character_traits = []

        elif character_traits == characters_girls[7]:
            print("The characteristics you have entered match most with Kim Jennie.")
            print("")
            lee = input("Is this your character?")
            print("")
            print("This was fun! Hope to see you next time!")
            character_traits = []

        elif character_traits == characters_girls[8]:
            print("The characteristics you have entered match most with Yoon Bomi.")
            print("")
            lee = input("Is this your character?")
            print("")
            print("This was fun! Hope to see you next time!")
            character_traits = []

        elif character_traits == characters_girls[9]:
            print("The characteristics you have entered match most with Kim Chaewon.")
            print("")
            lee = input("Is this your character?")
            print("")
            print("This was fun! Hope to see you next time!")
            character_traits = []
            
    elif yesorno.upper() == 'N':
        False
        quit()

