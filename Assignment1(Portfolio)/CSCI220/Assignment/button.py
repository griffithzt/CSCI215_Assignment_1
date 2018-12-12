#button.py
#Zachary Griffith

from graphics import *

#Purpose: Create a button class with the functions described in the instructions.

#Authenticity: I certify this is my own homework, but I had help from Professor Xu's
#instructions, example class code, an in class example she showed us, and her responses through email to help me along.

#add your Button class defination  here:
class Button:
    
    def __init__(self, shape, label):
        # Initialize text, label, shape
        #self.text = text
        self.label = label
        self.shape = shape
        
        #Getting point for the rectangle
        rectPointOne = shape.getP1()
        rectPointTwo = shape.getP2()
        
        #Getting X and Y coords for the two points used to make the rectangle.
        #make self.point... so they can be used in isClick further down
        self.pointOneX = rectPointOne.getX()
        self.pointOneY = rectPointOne.getY()
        self.pointTwoX = rectPointTwo.getX()
        self.pointTwoY = rectPointTwo.getY()
        
    
        
        #Set self.shape to a button that is a rectangle, pass in pointOne and pointTwo
        self.shape = Rectangle(Point(self.pointOneX, self.pointOneY), Point(self.pointTwoX, self.pointTwoY))

        #Getting the center of the rectangle. Used the math from the example
        #code provided to the class from Pofessor Xu.
        TwoxMinusOneXIntDivTwo = (self.pointTwoX - self.pointOneX) // 2
        TwoyMinusOneYIntDivTwo = (self.pointTwoY - self.pointOneY) // 2
        rectCenterX = self.pointOneX + TwoxMinusOneXIntDivTwo
        rectCenterY = self.pointOneY + TwoyMinusOneYIntDivTwo
        self.text = Text(Point(rectCenterX,rectCenterY),"")

  
        #Set text using the string label as the text

    def getLabel(self):
        #Getter to return label
        return self.label
    

    def draw(self, win):
        #set draw to draw shape to the window
        self.shape.draw(win)
        #Draw the text inside the shape using the positioning given in __init__
        self.text.setText(self.label)
        self.text.draw(win)

    def undraw(self, win):
        #set undraw to undraw the shape and the label
        self.shape.undraw()
        self.label.undraw()

    def isClick(self, point):
        #Set is clicked to determine if the click is in the box.
        
        #While conditional returning a boolean using the isClick range from the example in buttonClass.py.
        #Not sure what else to use here to make the code any different besides
        #making a series of useless checks but need it to do the rest.
        
        while point.getX() <= max(self.pointOneX, self.pointTwoX) and point.getX() >= min(self.pointOneX, self.pointTwoX) and point.getY() <= max(self.pointOneY, self.pointTwoY) and point.getY() >= min(self.pointOneY, self.pointTwoY):
               return True
        else:
            return False

    def colorButton(self, color):
        #set the color of shape(button)
        self.shape.setFill(color)

    def setLabel(self, win, label):
        #set label
        #remove old label
        self.text.undraw()
        #draw new label
        self.text.draw(win)
        #redraw new button
        #self.shape.draw(win)
        
        

#Main function given as test code.
    # DO NOT EDIT.
def main():
    win = GraphWin()
    rb = Button(Rectangle(Point(100,100), Point(65, 130)), 'yes')
    rb.draw(win)
    pt = win.getMouse()
    if rb.isClick(pt) :
        rb.colorButton('red')
        rb.setLabel(win,'red')
    else:
        rb.colorButton('blue')
        rb.setLabel(win,'blue')

    win.getMouse()

if __name__ == '__main__':
    main()
