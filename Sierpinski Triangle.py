
import turtle

def sierpinski_triangle(t,size,depth):
    '''
    (turtle, int, int) --> None
    Input: (t, size, depth) --> None
    t is turtle
    size is side length
    depth is depth of recursion
    Process: draws triangle
    Output: draws triangle
    '''

    if depth == 0:
        for i in range(3):
            t.forward(size)
            t.left(120)

    else:
        sierpinski_triangle(t, size/2, depth -1)
        t.forward(size/2)
        sierpinski_triangle(t, size/2, depth -1)
        t.left(120)
        t.forward(size/2)
        t.right(120)
        sierpinski_triangle(t, size/2, depth -1)
        t.left(60)
        t.back(size/2)
        t.right(60)
        



window = turtle.Screen()
t = turtle.Turtle()
sierpinski_triangle(t,100,3)
window.mainloop() # infinte loop that blocks execution of code
# use .mainloop() at the end of programs
