from display import *
from matrix import *
from draw import *

def parse_file( fname, points, transform, screen, color ):
    print "ok"
    f = open(fname , 'r')
    cmds = f.split("\n")
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
            m = new_matrix()
            transform = ident(m)
            
        elif cmds[i] == "scale":
            factors = cmds[i+1].split(" ")
            scale_m = make_scale(factors[0], factors[1], factors[2])
            transform = matrix_mult(scale_m , transform)
            
        elif cmds[i] == "move":
            factors = cmds[i+1].split(" ")
            move = make_translate(factors[0],factors[1],factors[2])
            transform = matrix_mult(move, transform)
            
        elif cmds[i] == "rotate":
            args = cmds[i+1].split(" ")
            if args[0] == "x":
                rot = makerotX(args[1])
            elif args[0] == "y":
                rot = makerotY(args[1])
            else:
                rot = makerotZ(args[1])
            transform = matrix_mult(rot, transform)
        
        elif cmds[i] == "apply":
            points = matrix_mult(transform , points)
        
        #elif cmds[i] == "display":
            #pass
        
        elif cmds[i] == "save":
            arg = cmds[i+1]
            save_ppm(screen, arg)
        
        elif cmds[i] == "quit":
            break 
        

