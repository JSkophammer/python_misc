import turtle

t = turtle.Turtle()
t.speed(100)
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

def draw_shape(sides, length, *args):
    t.begin_fill()
    for i in range(sides):
        t.forward(length)
        t.left(360/sides)
    t.end_fill()

def ext_draw(sides, length, fn, dim):
    for i in range(sides):
        fn(sides, length, fn, dim)
        t.forward(length * ((sides-1) ** dim))
        t.left(360/sides)
    return ext_draw

def gen_fract_exp(sides, length, dim):
    exp = 'ext_draw(%s, %s, draw_shape, %s)' % (str(sides), str(length), '1')
    for i in range(dim-1):
        exp = 'ext_draw(%s, %s, lambda x,y,z,w: %s, %s)' % (str(sides), str(length), exp, str(i+2))
    return exp

orient_turtle(1)
eval(gen_fract_exp(5, 5, 3))
window.exitonclick()


def func_comp(length, f, dim):
    return lambda x, y, z: ext_draw(length, lambda x, y, z: f, dim)
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
    ext_draw(length, lambda x,y,z: ext_draw(length, lambda x,y,z: ext_draw(length, draw_shape, dim - 2), dim - 1), dim)
    window = turtle.Screen()
    window.exitonclick()
def extend(length, dim):
    t.forward(length * (2 ** dim))
    t.left(120)
def build_exp(string, dim, length):
    string = 'ext_draw(%s, lambda x,y,z: %s, %s)' % (str(length), string, str(dim))
    return string