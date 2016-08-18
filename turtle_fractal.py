import turtle

t = turtle.Turtle()
t.speed(2)
t.color('black')
t.fillcolor('black')
window = turtle.Screen()
window.bgcolor('white')

def orient_turtle(factor=1):
    t.up()
    t.left(180)
    t.forward(factor*200)
    t.left(90)
    t.forward(factor*100)
    t.left(90)
    t.down()

def draw_triangle(length, *args):
    t.begin_fill()
    for i in range(3):
        t.forward(length)
        t.left(120)
    t.end_fill()

def ext_draw(fn, length, dim):
    for i in range(3):
        fn(length, fn, dim)
        t.forward(length * (2 ** dim))
        t.left(120)
    return ext_draw

def gen_fract_exp(length, dim):
    exp = 'ext_draw(%s, draw_triangle, %s)' % (str(length), '1')
    for i in range(dim-1):
        exp = 'ext_draw(%s, lambda x,y,z: %s, %s)' % (str(length), exp, str(i+2))
    return exp

#orient_turtle()
#eval(gen_fract_exp(30, 3))
#window.exitonclick()


def func_comp(f, t):
    return ext_draw(lambda x, y, z: f, *t)

def f(length):
    return ext_draw(draw_triangle, length, 1)

func_comp(f, (30,2))

def draw_fractal(length):
    orient_turtle()
    t.right(120)
    t.speed(10)
    for _ in range(3):
        for x in range(3):
            for y in range(3):
                for z in range(3):
                    draw_triangle(length)
                    extend(length, 1)
                extend(length, 2)
            extend(length, 3)
        extend(length, 4)

    window = turtle.Screen()
    window.exitonclick()
def draw_repeated(length, dim):
    orient_turtle()
    eval(gen_fract_exp(length, dim))
    #ext_draw(length, lambda x,y,z: ext_draw(length, lambda x,y,z: ext_draw(length, draw_triangle, dim - 2), dim - 1), dim)
    window = turtle.Screen()
    window.exitonclick()
def extend(length, dim):
    t.forward(length * (2 ** dim))
    t.left(120)
def build_exp(string, dim, length):
    string = 'ext_draw(%s, lambda x,y,z: %s, %s)' % (str(length), string, str(dim))
    return string