import turtle

def apply_rule(ch, rules):
    return rules.get(ch, ch)

def generate_l_system(axiom, rules, iterations):
    result = axiom
    for _ in range(iterations):
        result = ''.join(apply_rule(ch, rules) for ch in result)
    return result

def draw_l_system(turtle, instructions, angle, distance):
    stack = []
    for cmd in instructions:
        if cmd == 'F':
            turtle.forward(distance)
        elif cmd == '+':
            turtle.left(angle)
        elif cmd == '-':
            turtle.right(angle)
        elif cmd == '[':
            stack.append((turtle.heading(), turtle.pos()))
        elif cmd == ']':
            heading, position = stack.pop()
            turtle.penup()
            turtle.goto(position)
            turtle.setheading(heading)
            turtle.pendown()

def main():
    #дерево 1
#    axiom = 'F'
#    rules = {'F': 'F[+F]F[-F]F'}
#    angle = 25.7

    #дерево 2
    axiom = 'X'
    rules = {'F': 'FF', 'X': 'F[+X][-X]FX'}
    angle = 25.7

    #кривая Гильберта
#    axiom = 'X'
#    rules = {'F': 'F', 'X': '-YF+XFX+FY-', 'Y': '+XF-YFY-FX+'}
#    angle = 90

    #Снежинка Коха
#    axiom = 'F++F++F'
#    rules = {'F': 'F-F++F-F'}
#    angle = 60

    #Дракон Хартера-Хатвея
#    axiom = 'FX'
#    rules = {'F': 'F', 'X': 'X+YF+', 'Y': '-FX-Y'}
#    angle = 90

    #Треугольник Серпинского
#    axiom = 'FXF--FF--FF'
#    rules = {'F': 'FF', 'X': '--FXF++FXF++FXF--'}
#    angle = 60

    
    # Количество итерация влияет на детализацию
    iterations = 3

    l_system = generate_l_system(axiom, rules, iterations)

    # Окно
    window = turtle.Screen()
    window.bgcolor("white")

    # Черепашка
    fractal_turtle = turtle.Turtle()
    fractal_turtle.speed(100)

    # Начальное положение и направление (смотрит наверх)
    fractal_turtle.penup()
    fractal_turtle.goto(0, -150)
 #   fractal_turtle.setheading(90)  # Поворот на 90 градусов
    fractal_turtle.pendown()

    # Рисование L-системы
    draw_l_system(fractal_turtle, l_system, angle, 5)

    # Закрываем окно при нажатии
    window.exitonclick()

if __name__ == "__main__":
    main()
