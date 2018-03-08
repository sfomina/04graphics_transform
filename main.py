from display import *
from draw import *
#import parser
from matrix import *

#print parser.tired()


screen = new_screen()
color = [ 0, 255, 0 ]
edges = new_matrix()
transform = new_matrix()

#print_matrix([[1,4], [2,5],[3,6]])
#print (matrix_mult([[1,4], [2,5],[3,6]] , [[7,9,11] , [8,10,12]]))

#print_matrix(transform)

def parse_file( fname, points, transform, screen, color ):
    f = open(fname , 'r')
    cmds = f.read().split("\n")
    for i in range(0,len(cmds)):
        if cmds[i] == "line":
            pts = cmds[i+1].split(" ")
            x0 = int(pts[0])
            y0 = int(pts[1])
            z0 = int(pts[2])
            x1 = int(pts[3])
            y1 = int(pts[4])
            z1 = int(pts[5])
            add_edge(points, x0, y0, z0, x1, y1, z1 )
            
        elif cmds[i] == "ident":
            ident(transform)
            
        elif cmds[i] == "scale":
            factors = cmds[i+1].split(" ")
            scale_m = make_scale(int(factors[0]),int( factors[1]), int(factors[2]))
            
            transform = matrix_mult(scale_m , transform)
            
        elif cmds[i] == "move":
            factors = cmds[i+1].split(" ")
            move = make_translate(int(factors[0]),int(factors[1]),int(factors[2]))
            transform = matrix_mult(move, transform)
            
        elif cmds[i] == "rotate":
            args = cmds[i+1].split(" ")
            if args[0] == "x":
                rot = make_rotX(int(args[1]))
            elif args[0] == "y":
                rot = make_rotY(int(args[1]))
            else:
                rot = make_rotZ(int(args[1]))
            transform = matrix_mult(rot, transform)
        
        elif cmds[i] == "apply":
            #print "APPLY"
            points = matrix_mult(transform, points)
            #print_matrix( points)
        
        elif cmds[i] == "display":
            print "DISP"
            print(len(points))
            draw_lines(points, screen, color)
        
        elif cmds[i] == "save":
            arg = cmds[i+1]
            save_ppm(screen, arg)
        
        elif cmds[i] == "quit":
            break 
        


parse_file( 'script', edges, transform, screen, color )
