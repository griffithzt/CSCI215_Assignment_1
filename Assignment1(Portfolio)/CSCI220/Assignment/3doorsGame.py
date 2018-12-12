#3doorsGame.py
#Zachary Griffith

#Purpose: Create a three door game, where the buttons from button.py are used as doors.
#Put the button objects in a list
#Put the output messages in a list
#When correct flash the door green and white
#When wrong turn the door red

#Authenticity: I certify this is my own homework, but I had help from Professor Xu's
#instructions, example class code, an in class example she showed us, and her responses through email to help me along.


#importing libraries and button from button class.
from graphics import *
from button import Button
from random import *
from math import *
from time import *


def main():

    win = GraphWin("Three Door Game",320,320)

    #Draw 3 doors.
    buttonOneRectangle = Rectangle(Point(80, 170), Point(20, 130))
    buttonOne = Button(buttonOneRectangle, "Door 1")
    buttonOne.draw(win)

    buttonTwoRectangle = Rectangle(Point(120, 130), Point(180, 170))
    buttonTwo = Button(buttonTwoRectangle, "Door 2")
    buttonTwo.draw(win)

    buttonThreeRectangle = Rectangle(Point(220, 130), Point(280, 170))
    buttonThree = Button(buttonThreeRectangle, "Door 3")
    buttonThree.draw(win)

    #Put button objects in a list
    buttonList =[buttonOne, buttonTwo, buttonThree]

    #Self random int in the range 0 to 2.
    randomButtonListNum = randint(0,2)

    #Make the correct door the random generated int in the range 0 to 2
    # in the list of button objects.
    correctDoor = buttonList[randomButtonListNum]

    #Make text that instructs user to click on a door.
    instructionText = Text(Point(150,50), "Please click a door.")
    instructionText.draw(win)

    #Set a play number so you won't be in never ending if else statements
    #and can get to click to close eventually.
    playNumber = 5
    winCount = 0
    for i in range(playNumber):
        #get mouse and click
        point = win.getMouse()

        #List for messages
        messageList = ["You Win!", "This is not the correct door! You Lose!","Click anywhere to close."]
        #Selecting a random door from the list of buttons
        correctDoor = buttonList[randomButtonListNum]

        
        #is button won is clicked
        if buttonOne.isClick(point):
            #check is it matches the list
             if buttonOne == correctDoor:
                #undraw instructions
                instructionText.undraw()
                #draw winning message
                winText = Text(Point(150,50), messageList[0])
                winText.draw(win)

                #Flash green and white if correct
                buttonOne.colorButton("green")
                sleep(1)
                buttonOne.colorButton("white")
                sleep(1)
                buttonOne.colorButton("green")
                #main()
                #After game is over. Set click to close text and draw.
                endTextOutput = Text(Point(150,300), messageList[2])
                endTextOutput.draw(win)

            #If buttonOne doesn't match the list item
             elif buttonOne != correctDoor:
                #undraw the instructions
                instructionText.undraw()
                #Prompt to try again
                loseText = Text(Point(150,50), messageList[1])
                loseText.draw(win)
                #red for wrong
                buttonOne.colorButton("red")
                sleep(1)
                loseText.undraw()
                instructionText.draw(win)
                win.close()
                main()
                

        #If buttonTwo is clicked
        elif buttonTwo.isClick(point):
            #check to see if it matched the list
            if buttonTwo == correctDoor:
                #undraw the instructions
                instructionText.undraw()
                #Draw winner text
                winText = Text(Point(150,50), messageList[0])
                winText.draw(win)

                #Flash green and white if correct
                buttonTwo.colorButton("green")
                sleep(1)
                buttonTwo.colorButton("white")
                sleep(1)
                buttonTwo.colorButton("green")
                #After game is over. Set click to close text and draw.
                endTextOutput = Text(Point(150,280), messageList[2])
                endTextOutput.draw(win)


            #If buttonTwo is incorrect
            elif buttonTwo != correctDoor:
                #undraw instruction text
                instructionText.undraw()
                #Prompt to keep playing
                loseText = Text(Point(150,50), messageList[1])
                loseText.draw(win)
                #red for wrong
                buttonTwo.colorButton("red")
                sleep(1)
                loseText.undraw()
                instructionText.draw(win)
                win.close()
                main()

        #If the click on button three is correct
        elif buttonThree.isClick(point):
            #check to make sure it matches the list item
            if buttonThree == correctDoor:
                #undraw the instructions
                instructionText.undraw()
                
                #Draw win message
                winText = Text(Point(150,50), messageList[0])
                winText.draw(win)

                #Flash green and white if correct
                buttonThree.colorButton("green")
                sleep(1)
                buttonThree.colorButton("white")
                sleep(1)
                buttonThree.colorButton("green")
                #After game is over. Set click to close text and draw.
                endTextOutput = Text(Point(150,280), messageList[2])
                endTextOutput.draw(win)

            #If button three is incorrect
            elif buttonThree != correctDoor:
                #Undraw instructions
                instructionText.undraw()
                #Prompt to keep playing
                loseText = Text(Point(150,50), messageList[1])
                loseText.draw(win)
                #red for wrong
                buttonThree.colorButton("red")
                sleep(2)
                loseText.undraw()
                instructionText.draw(win)
                win.close()
                main()

##            if buttonOne == correctDoor or buttonTwo == correctDoor or buttonThree == correctDoor:
##                win = win + 1
##                strWin = str(win)
##                print(strWin)
##                winText = Text(Point(130, 70), str(strWin))
##                winText.draw(win)
##            elif buttonOne != correctDoor or buttonTwo != correctDoor or buttonThree != correctDoor:
##                loss = loss + 1
##                strLoss = str(loss)
##                lossText = Text(Point(160,70), str(strLoss))
##                lossText.draw(win)

    #close win
    win.getMouse()
    win.close()

main()


                        

