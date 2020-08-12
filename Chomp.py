
import turtle


class ChompGame:

    def __init__(self,width,height):
        
        self.window = turtle.Screen()
        self.window.title('CHOMP')

        self.gamewidth = width
        self.gameheight = height

        self.cookies = {}
        
        for i in range(width):
            for j in range(height):
                self.cookies[(i,j)] = Cookie(40*i, 40*j, i==0 and j==0)

        # turtle messenger

        self.messenger = turtle.Turtle()
        self.messenger.hideturtle()
        self.messenger.penup()
        self.messenger.goto(0,-100)

        self.player = 1
        self.print_player()

        # start the game
        self.window.onclick(self.chomp)
        self.window.listen()
        self.window.mainloop()

    def print_player(self):

        self.messenger.clear()
        self.messenger.write('Player ' + str(self.player) + "'s turn", font=('Arial',36,'normal'))

    def chomp(self,x,y):

        xpos = round(x/40)
        ypos = round(y/40)

        if (0 <= xpos < self.gamewidth) and (0 <= ypos < self.gameheight) \
           and self.cookies[(xpos,ypos)].isvisible():

            for i in range(xpos, self.gamewidth):
                for j in range(ypos, self.gameheight):
                    self.cookies[(i,j)].hideturtle()

            if xpos + ypos == 0:
                print("Player " + str(self.player) + ' loses!')
                self.window.bye()
                return

            self.player = 3 - self.player
            self.print_player()

        
class Cookie(turtle.Turtle):

    def __init__(self, x, y , poison):

        turtle.Turtle.__init__(self)

        self.shape('circle')
        self.width(20)
        
        self.speed(0)
        self.penup()
        self.goto(x,y)

        if not poison:
            self.color('brown')

'''       
        
for i in range(7):
    for j in range(5):
        Cookie(40*i, 40*j, i == 0 and j == 0)

'''

c = ChompGame(7,5)
