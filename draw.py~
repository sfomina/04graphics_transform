from display import *
from matrix import *


def draw_lines( matrix, screen, color ):
    num_points = len(matrix)

    x1 = 0
    x2= 0

    y1= 0
    y2 = 0

    for i in range(0,num_points , 2):
        x1 = matrix[i][0]
        y1 = matrix[i][1]
        x2 = matrix[i+1][0]
        y2 = matrix[i+1][1]
        
        draw_line(x1,y1,x2,y2, screen, color)

def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point(matrix,x0, y0 , z0)
    add_point(matrix,x1, y1 , z1)    
    

def add_point( matrix, x, y, z=0 ):
    point = [x,y,z,1]
    matrix.append(point)
    return matrix
    


def draw_line( x0, y0, x1, y1, screen, color ):
    x = x0
    y = y0
    B = x0 - x1
    A = y1 - y0
    if (x1 - x0 == 0):
        m = 0
        if (y0 <= y1):
            while (y <= y1):
                plot(screen, color, x, y)
                y += 1
        else:
            while (y >= y1):
                plot(screen, color, x, y)
                y -= 1
                
        
    else:
        m  =(1.0 * (y1- y0))/(x1 - x0)

        if (m <= 1 and m >= 0):
            d = 2*A + B
            while (x <= x1):
                plot(screen, color,x , y)
                if (d > 0):
                    y += 1
                    d += 2*B
                x += 1
                d += 2*A

        #octant II
        elif (m > 1):
            d = A + B*2
            while (y <= y1):
                plot(screen, color, x, y)
                if(d < 0):
                    x += 1
                    d += 2*A
                y += 1
                d+= 2*B

        #octant VIII
        elif (m >= -1 and m < 0):
            d = 2*A - B
            while (x <= x1):
                plot(screen, color, x, y)
                if (d < 0):
                    y -= 1
                    d -= 2*B
                x += 1
                d += 2*A
         #print screen

        #octant VII
        elif (m < -1):
            d = A - 2*B
            while (y >= y1):
                plot(screen, color, x ,y)
                if (d >0):
                    x += 1
                    d += 2*A
                y -= 1
                d -= 2*B





