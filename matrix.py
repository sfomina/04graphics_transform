import math

def make_translate( x, y, z ):
    translation = [[1,0,0,0], [0,1,0,0] , [0,0,1,0] , [x,y,z,1]]
    return translation

def make_scale( x, y, z ):
    scale = [ [x,0,0,0] , [0,y,0,0,] , [0,0,z,0] , [0,0,0,1]]
    return scale

def make_rotX( theta ):    
    rotx = [[1,0,0,0] , [0,math.cos(theta) , math.sin(theta) ,0] , [0, -1* math.sin(theta) , math.cos(theta), 0] , [0,0,0,1]]
    return rotx

def make_rotY( theta ):
    roty = [[math.cos(theta) ,0 , -1* math.sin(theta), 0],[0, 1, 0, 0],[math.sin(theta), 0, math.cos(theta), 0] , [0 , 0, 0, 1]]
    return roty

def make_rotZ( theta ):
    rotz = [[math.cos(theta), -1* math.sin(theta), 0,0],[math.sin(theta), math.cos(theta), 0 , 0], [0,0,1,0] , [0,0,0,1]]
    return rotz

def print_matrix( matrix ):
    s = ''
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            s+= str(matrix[c][r]) + ' '
        s+= '\n'
    print s

def ident( matrix ):
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            if r == c:
                matrix[c][r] = 1
            else:
                matrix[c][r] = 0

#m1 * m2 -> m3
def matrix_mult( m1, m2 ):
    m3 = []
    for i in range(len(m2)):
        m3.append([])
        for x in range(len(m2[0])):
            m3[i][x] = 0
    for i in range(len(m1[0])):
        for y in range(len(m2)):
            sum = 0
            x = 0
            for l in m1:
                sum += l[i] * m2[y][x]
                x+=1
            m3[y][i] = sum 
            #print sum
    return m3


def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
