def solve_quadratic_equation(a,b,c):

    
    delta = b**2-4*a*c

    if delta < 0:
        return "the equation has no true answer"
    elif delta == 0:
        x = -b / (2*a)
        return f"the equation has an iterative solution:x={x}"
    else:
        x1 = (-b +(delta**0.5)) /(2*a)
        x2 = (-b -(delta**0.5)) /(2*a)
        return f"the equation has two roots:x1 = {x1},x2={x2}"