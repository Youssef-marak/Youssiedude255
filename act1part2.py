"""_summary_
    Group Members: Syed Ali Mustafa Wasti, Youssef Marrak, Bechir Ben Zaeid
    Date: 05/02/2024
    Manifesto: This program is desigined to take user input on the colors of shapes and the pen color to create a pattern of hexagons, circles and squares.
"""

import turtle
 
turta = turtle.Turtle() #Turning the turtle library into an object so that it can be called using turta.

hexa_color = input("Enter the color of the hexagon: ") #Input the color of the hexagon.
circle_color = input("Enter the color of the circle: ") #Input the color of the circle.
square_color = input("Enter the color of the square: ") #Input the color of the square.
border_color = input("Enter the color of shape borders: ") #Input the color of the shape borders.

def setPos(x, y): #Set the position of the shapes.
    turta.up() #Using the .up and .down functions allows us to make it so that the movements between each shape cannot be seen
    turta.goto(x, y) #This is the function that moves the turtle to a specific place in the window using coordinates.
    turta.down()

def hexagon(): #Making the hexagon() function.
    turta.fillcolor(hexa_color) #The color of the shape with the color being user input.
    turta.begin_fill() #When to start filling the shape with color.
    
    turta.forward(50) #This is the function that makes the lines for the hexagon and the value in the () is the length of the line.
    turta.left(60) #This is the function that moves the turtle to the specific angle that is written in the ().
    turta.forward(50)
    turta.left(60)
    turta.forward(50)
    turta.left(60)
    turta.forward(50)
    turta.left(60)
    turta.forward(50)
    turta.left(60)
    turta.forward(50)
    turta.left(60)
    
    turta.end_fill() #When to stop filling the color
    
def square(): #Making the square() function.
    turta.fillcolor(square_color) #The color of the shape with the color being user input.
    turta.begin_fill() #When to start filling the shape with color.
    
    turta.forward(90) #This is the function that makes the lines for the square and the value in the () is the length of the line.
    turta.left(90) #This is the function that moves the turtle to a specific angle that is written in the ()
    turta.forward(90)
    turta.left(90)
    turta.forward(90)
    turta.left(90)
    turta.forward(90)
    
    turta.end_fill() #When to stop filling the color
    
def circle(): #Making the circle() function.
    turta.fillcolor(circle_color) #The color of the shape with the color being user input.
    turta.begin_fill() #When to start filling the shape with color.
    
    turta.circle(45) #This is the function that makes the circle and the value in the () is the radius.
    
    turta.end_fill() #When to stop filling the color
    
def pattern(): #Putting the shapes into a pattern by using the functions hexagon(), square(), circle().
    turta.screen.bgcolor("skyblue") #The function to change the background color of the turtle. We use turta.screen.bgcolor() as in some versions of the library you need to access the screen() library to change some parameters. It is possible to make this user input too.
    
    turta.pencolor(border_color) #The function to change the pen color of the turtle with the color being user input.
    
    turta.pensize(2) #The function to change the size of the pen. It is possible to make this user input too.
    
    hexagon() #Running the hexagon() function.
    
    turta.up() #Using the .up and .down functions allows us to make it so that the movements between each shape cannot be seen
    turta.fd(160) #This is the function that allows us to move the specific shape to a different position.
    turta.down()
    circle() #Running the circle() function.
    
    turta.up() #Using the .up and .down functions allows us to make it so that the movements between each shape cannot be seen
    turta.fd(90) #This is the function that allows us to move the specific shape to a different position.
    turta.down()
    square() #Running the square() function.
    
    
def main(): #Making a main function to run the pattern() function.
    
    setPos(-250, 150) #Sets the position for where the pattern should start.
    pattern() #Running the pattern() function.
    turta.rt(270)
    
    setPos(-150, 0) #Sets the position for where the pattern should start.
    pattern() #Running the pattern() function.
    turta.rt(-90)
    
    setPos(-50, -150) #Sets the position for where the pattern should start.
    pattern() #Running the pattern() function.
    
    input("Press 'Enter' to exit...") #We have used the input() function so that the user can see the drawing even after the code has ended.

main() #Running the main() function.