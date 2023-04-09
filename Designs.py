import colorsys
import turtle

from math import cos, sin, radians


t = turtle.Turtle()
s = turtle.Screen()


def design_1():
    s.bgcolor('black')
    t.speed(0)

    n = 36
    h = 0

    for i in range(460):
        c = colorsys.hsv_to_rgb(h, 1, 0.8)
        h += 1/n
        t.color(c)
        t.left(145)

        for j in range(5):
            t.forward(300)
            t.left(150)


def design_2():
    n = 70
    h = 0
    for i in range(360):
        c = colorsys.hsv_to_rgb(h, 1, 0.8)
        h += 1 / n
        t.color(c)
        t.left(1)
        t.fd(1)
        for j in range(2):
            t.left(2)
            t.circle(100)


def design_3():
    c = 0
    x = 0

    colors = [
        # reddish colors
        (1.00, 0.00, 0.00), (1.00, 0.03, 0.00), (1.00, 0.05, 0.00), (1.00, 0.07, 0.00), (1.00, 0.10, 0.00),
        (1.00, 0.12, 0.00), (1.00, 0.15, 0.00), (1.00, 0.17, 0.00), (1.00, 0.20, 0.00), (1.00, 0.23, 0.00),
        (1.00, 0.25, 0.00), (1.00, 0.28, 0.00), (1.00, 0.30, 0.00), (1.00, 0.33, 0.00), (1.00, 0.35, 0.00),
        (1.00, 0.38, 0.00), (1.00, 0.40, 0.00), (1.00, 0.42, 0.00), (1.00, 0.45, 0.00), (1.00, 0.47, 0.00),
        # orangey colors
        (1.00, 0.50, 0.00), (1.00, 0.53, 0.00), (1.00, 0.55, 0.00), (1.00, 0.57, 0.00), (1.00, 0.60, 0.00),
        (1.00, 0.62, 0.00), (1.00, 0.65, 0.00), (1.00, 0.68, 0.00), (1.00, 0.70, 0.00), (1.00, 0.72, 0.00),
        (1.00, 0.75, 0.00), (1.00, 0.78, 0.00), (1.00, 0.80, 0.00), (1.00, 0.82, 0.00), (1.00, 0.85, 0.00),
        (1.00, 0.88, 0.00), (1.00, 0.90, 0.00), (1.00, 0.93, 0.00), (1.00, 0.95, 0.00), (1.00, 0.97, 0.00),
        # yellowy colors
        (1.00, 1.00, 0.00), (0.95, 1.00, 0.00), (0.90, 1.00, 0.00), (0.85, 1.00, 0.00), (0.80, 1.00, 0.00),
        (0.75, 1.00, 0.00), (0.70, 1.00, 0.00), (0.65, 1.00, 0.00), (0.60, 1.00, 0.00), (0.55, 1.00, 0.00),
        (0.50, 1.00, 0.00), (0.45, 1.00, 0.00), (0.40, 1.00, 0.00), (0.35, 1.00, 0.00), (0.30, 1.00, 0.00),
        (0.25, 1.00, 0.00), (0.20, 1.00, 0.00), (0.15, 1.00, 0.00), (0.10, 1.00, 0.00), (0.05, 1.00, 0.00),
        # greenish colors
        (0.00, 1.00, 0.00), (0.00, 0.95, 0.05), (0.00, 0.90, 0.10), (0.00, 0.85, 0.15), (0.00, 0.80, 0.20),
        (0.00, 0.75, 0.25), (0.00, 0.70, 0.30), (0.00, 0.65, 0.35), (0.00, 0.60, 0.40), (0.00, 0.55, 0.45),
        (0.00, 0.50, 0.50), (0.00, 0.45, 0.55), (0.00, 0.40, 0.60), (0.00, 0.35, 0.65), (0.00, 0.30, 0.70),
        (0.00, 0.25, 0.75), (0.00, 0.20, 0.80), (0.00, 0.15, 0.85), (0.00, 0.10, 0.90), (0.00, 0.05, 0.95),
        # blueish colors
        (0.00, 0.00, 1.00), (0.05, 0.00, 1.00), (0.10, 0.00, 1.00), (0.15, 0.00, 1.00), (0.20, 0.00, 1.00),
        (0.25, 0.00, 1.00), (0.30, 0.00, 1.00), (0.35, 0.00, 1.00), (0.40, 0.00, 1.00), (0.45, 0.00, 1.00),
        (0.50, 0.00, 1.00), (0.55, 0.00, 1.00), (0.60, 0.00, 1.00), (0.65, 0.00, 1.00), (0.70, 0.00, 1.00),
        (0.75, 0.00, 1.00), (0.80, 0.00, 1.00), (0.85, 0.00, 1.00), (0.90, 0.00, 1.00), (0.95, 0.00, 1.00)
    ]

    while x < 1000:
        idx = int(c)
        color = colors[idx]
        turtle.color(color)
        turtle.forward(x)
        turtle.right(98)
        x = x + 1
        c = c + 0.1

    turtle.exitonclick()


class ThreeDragonCurve:
    def __init__(self, iterations, axiom, rules, angle, length=None, size=None, correction_angle=0, y_offset=None, x_offset=None, offset_angle=None, inverted=False, flip_h=False, flip_v=False, width=None, height=None, margin=None, aspect_ratio=None):
        self.iterations = iterations
        self.axiom = axiom
        self.rules = rules
        self.angle = angle
        self.length = length
        self.size = size
        self.correction_angle = correction_angle
        self.y_offset = y_offset
        self.x_offset = x_offset
        self.offset_angle = offset_angle
        self.inverted = inverted
        self.flip_h = flip_h
        self.flip_v = flip_v
        self.width = width
        self.height = height
        self.margin = margin
        self.aspect_ratio = aspect_ratio

    def draw(self):
        inst = self.create_l_system(self.iterations, self.axiom, self.rules)

        width_, height_, min_x, min_y = self.calc_length_height(inst, self.angle, self.correction_angle)

        if width_ == 0 and height_ == 0:
            return

        if self.aspect_ratio is None:
            if 0 in [width_, height_]:
                self.aspect_ratio = 1
            else:
                self.aspect_ratio = width_ / height_

        if self.width is None and self.height:
            self.width = self.height / self.aspect_ratio

        if self.height is None and self.width:
            self.height = self.width / self.aspect_ratio

        if self.margin is None:
            self.margin = 35

        if self.offset_angle is None:
            self.offset_angle = -90

        if self.length is None:
            if width_ > height_:
                self.length = (self.width - 2 * self.margin) / width_
            else:
                self.length = (self.height - 2 * self.margin) / height_

        if width_ * self.length > self.width:
            self.length = (self.width - 2 * self.margin) / width_
        elif height_ * self.length > self.height:
            self.length = (self.height - 2 * self.margin) / height_

        if self.x_offset is None:
            if width_ >= height_ and (self.width - width_) <= width_ - 2 * self.margin:
                self.x_offset = -(self.width / 2 - self.margin) + min_x * self.length
            else:
                self.x_offset = -(self.width / 2) + (self.width - width_ * self.length) / 2 + min_x * self.length

        if self.y_offset is None:
            if height_ >= width_ and (self.height - height_) <= height_ - 2 * self.margin:
                self.y_offset = -(self.height / 2 - self.margin) + min_y * self.length
            else:
                self.y_offset = -(self.height / 2) + (self.height - height_ * self.length) / 2 + min_y * self.length

        if self.inverted:
            inst = inst.replace('+', '$')
            inst = inst.replace('-', '+')
            inst = inst.replace('$', '-')
            inst = inst.replace('F', '$')
            inst = inst.replace('B', 'F')
            inst = inst.replace('$', 'B')

        if self.flip_h:
            inst = inst.replace('F', '$')
            inst = inst.replace('B', 'F')
            inst = inst.replace('$', 'B')
            self.y_offset *= -1

        if self.flip_v:
            inst = inst.replace('+', '$')
            inst = inst.replace('-', '+')
            inst = inst.replace('$', '-')
            self.y_offset *= -1

        if self.size is None:
            if self.length < 3:
                self.size = 1
            elif self.length < 12:
                self.size = 2
            elif self.length < 25:
                self.size = 3
            else:
                self.size = 5

        t = turtle.Turtle()
        wn = turtle.Screen()
        wn.setup(self.width, self.height)

        t.up()
        t.backward(-self.x_offset)
        t.left(90)
        t.backward(-self.y_offset)
        t.left(self.offset_angle)
        t.down()
        t.speed(0)
        t.pensize(self.size)
        self.draw_l_system(t, inst, self.angle, self.length)
        t.hideturtle()

        wn.exitonclick()

    def create_l_system(self, iters, axiom, rules):
        start_string = axiom
        if iters == 0:
            return axiom
        end_string = ""
        for _ in range(iters):
            end_string = "".join(rules[i] if i in rules else i for i in start_string)
            start_string = end_string

        return end_string

    def draw_l_system(self, t, instructions, angle, distance):
        steps = len([i for i in instructions if i in "FB"])
        step = 1 / steps
        i = 0
        for cmd in instructions:
            if cmd == 'F':
                t.forward(distance)
            elif cmd == 'B':
                t.backward(distance)
            elif cmd == '+':
                t.right(angle)
            elif cmd == '-':
                t.left(angle)

    def calc_length_height(self, instructions, angle, correction_angle):
        current_angle = correction_angle
        x_offset = 0
        y_offset = 0
        min_x = 0
        min_y = 0
        max_x = 0
        max_y = 0
        for inst in instructions:
            if inst == "F":
                x_offset += cos(radians(current_angle))
                y_offset += sin(radians(current_angle))
            elif inst == "B":
                x_offset -= cos(radians(current_angle))
                y_offset -= sin(radians(current_angle))
            elif inst == "+":
                current_angle -= angle
            elif inst == "-":
                current_angle += angle
            max_x = max(max_x, x_offset)
            min_x = min(min_x, x_offset)
            max_y = max(max_y, y_offset)
            min_y = min(min_y, y_offset)

        width = abs(max_x) + abs(min_x)
        height = abs(max_y) + abs(min_y)

        return width, height, abs(min_x), abs(min_y)
