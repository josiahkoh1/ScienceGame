position = 0
name = input('What is your name: ')
print(' any key to roll \n q to quit \n you move backwards if you answer questions wrong\n answer the water cycle questions like it starts from the ocean \n answer multiple choice questions like a, b, c, or d')
import random
def roll(position):
    inp=str(input('->'))
    correct=0
    wrong=0
    while inp!='q':
        x= random.randint(1,6)
        if x ==1:
            position+=1
        if x ==2:
            position+=2
        if x ==3:
            position+=3
        if x ==4:
            position+=4
        if x ==5:
            position+=5
        if x ==6:
            position+=6
        print('You rolled the number',x)
        if position == 1:
            questionone = input("What stage is condensation in the water cycle? \n a) 1st \n b) 2nd \n c) 3rd \n d) 4th \n Answer: ")
            if questionone == "b":
                print('Correct!')
                correct = correct + 1
                position = 7
            else:
                wrong = wrong + 1
                print('The correct answer is 2nd')

        if position == 5:
            questiontwo = input("What stage is surface runoff or groundwater flow in the water cycle? \n a) 1st \n b) 2nd \n c) 3rd \n d) 4th \n Answer: ")
            if questiontwo == "d":
                print('Correct!')
                correct = correct + 1
                position = 13
            else:
                print('Wrong.')
                wrong = wrong + 1
                position = 3
                print('The correct answer is 4th')

        if position == 8:
            questionthree = input("What stage is evaporation in the water cycle? \n a) 1st \n b) 2nd \n c) 3rd \n d) 4th \n Answer: ")
            if questionthree == "a":
                print('Correct!')
                correct = correct + 1
                position = 25
            else:
                print('Wrong.')
                wrong = wrong + 1
                position = 6
                print('The correct answer is 1st')

        if position == 15:
            questionfour = input("What stage is precipitation in the water cycle? \n a) 1st \n b) 2nd \n c) 3rd \n d) 4th \n Answer: ")
            if questionfour == "c":
                print('Correct!')
                correct = correct + 1
                position = 42
            else:
                print('Wrong.')
                wrong = wrong + 1
                position = 13
                print('The correct answer is 3rd')

        if position == 22:
            questionfive = input("How does the sun effect the water cycle? \n a) It evaporates water \n b) it makes the clouds start to rain \n c) It help make the clouds \n Answer: ")
            if questionfive == "a":
                print('Correct!')
                correct = correct + 1
                posision = 36
            else:
                print('Wrong.')
                wrong = wrong + 1
                position = 12
                print('The correct answer is it evaporates water')

        if position == 33:
            questionsix = input("True or False, Precipitation can be rain, snow, sleet, and hail. \n Answer: ")
            if questionsix == "True" or questionsix == "true":
                print('Correct!')
                correct = correct + 1
                position = 46
            else:
                print('Wrong.')
                wrong = wrong + 1
                position = 31
                print('The correct answer is true')

        if position == 35:
            questionseven = input("True or False, Evaporation is water becoming a gas. \n Answer: ")
            if questionseven == "True" or questionseven == "true":
                print('Correct!   ')
                correct = correct + 1
                position = 41
            else:
                print('Wrong.')
                wrong = wrong + 1
                position = 24
                print('The correct answer is true')

        if position == 46:
            questioneight = input("What is the first state of matter affected in sublimation? \n a) Solid \n b) Liquid \n c)Gas \n Answer: ")
            if questioneight == "a":
                print('Correct!')
                correct = correct + 1
                position = 58
            else:
                print('Wrong.')
                wrong = wrong + 1
                position = 32
                print('The correct answer is a, solid')
                

        if position == 56:
            questionnine = input("What is the first state of matter affected in deposition? \n a) Solid \n b) Liquid \n c)Gas \n Answer: ")
            if questioninine == "c":
                print('Correct!')
                correct = correct + 1
                position = 62
            else:
                print('Wrong.')
                wrong = wrong + 1
                position = 41
                print('The correct answer is c, Gas')

        if position == 69:
            questionten = input("Is kinetic energy being added or removed in evaporation? \n a) Added \n b) Removed \n Answer: ")
            if questionten == "a":
                print('Correct!')
                correct = correct + 1
                position = 82
            else:
                print('Wrong.')
                wrong = wrong + 1
                position = 61
                print('The correct answer is a, added')


        if position == 75:
            questioneleven = input("Is kinetic energy being added or removed in freezing? \n a) Added \n b) Removed \n Answer: ")
            if questioneleven == "b":
                print('Correct!')
                correct = correct + 1
                position = 87
            else:
                print('Wrong.')
                wrong = wrong + 1
                position = 68
                print('The correct answer is removed')

        if position == 89:
            questiontwelve = input("Is kinetic energy being added or removed in melting? \n a) Added \n b) Removed \n Answer: ")
            if questiontwelve == "a":
                print('Correct!')
                correct = correct + 1
                position = 104
            else:
                print('Wrong.')
                wrong = wrong + 1
                position = 84
                print('The correct answer is added')

        if position == 114:
            questionthirteen = input("Is kinetic energy being added or removed in condensation? \n a) Added \n b) Removed \n Answer: ")
            if questionthirteen == "b":
                print('Correct!')
                correct = correct + 1
                position = 124
            else:
                print('Wrong.')
                wrong = wrong + 1
                position = 86
                print('The correct answer is removed')

        if position == 127:
            questionfourteen = input("Is kinetic energy being added or removed in deposition? \n a) Added \n b) Removed \n Answer: ")
            if questionfourteen == "b":
                print('Correct!')
                correct = correct + 1
                position = 138
            else:
                print('Wrong.')
                wrong = wrong + 1
                position = 102
                print('The correct answer is removed')
        print('You are at square',position)

        if position == 142:
            questionfifteen = input("Is thermal energy being absorbed or released in deposition? \n a) Absorbed \n b) Released \n Answer: ")
            if questionfifteen == "b":
                print('Correct!')
                correct = correct + 1
                position = 138
            else:
                print('Wrong.')
                wrong += 1
                position = 102
                print('The correct answer is released')
                print('You are at square',position)
        if position >= 175:
            win = correct > wrong
            if win == True:
                print("Game over.",name,"has won!")
            else:
                print('Game over.',name,'answered more questions wrong than right.')
            print(name, 'Has answered' ,correct, 'questions correct and answered' ,wrong, 'questions wrong.')
            restart = input('[Enter] to restart: ')
            if restart == '':
                position=0
                correct=0
                wrong=0
        inp=str(input('->'))
roll(position)
