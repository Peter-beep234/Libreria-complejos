import math

def sum_complex(a,b):
    return(a[0]+b[0],a[1]+b[1])

#def rest_complex(a,b):
    #return ((a[0]*1)-(b[0]*1),(a[1]*1)-(b[1]*1))

def mult_complex(a,b):
    return ((a[0]*b[0])-(a[1]*b[1]),(a[0]*b[1])+(b[0]*a[1]))

def div_complex(a,b):
    return ((a[0]*b[0])+(a[1]*b[1]))/(b[0]**2 + b[1]**2), ((b[0]*a[1])-(a[0]*b[1]))/(b[0]**2 + b[1]**2)

def mod_complex(a):
    return ((a[0]**2)+(a[1]**2))**(1/2)

def conj_complex(a):
    return (a[0],a[1]*-1)

def cartesiano_a_polar_complex(a):
    return (((a[0]**2)+(a[1]**2))**(1/2),math.atan((a[1]/a[0])))

def polar_a_cartesiano_complex(a):
    return (a[0]*math.cos(a[1])),(a[0]*math.sin(a[1]))

def fase_complex(a):
    return math.atan((a[1]/a[0]))

