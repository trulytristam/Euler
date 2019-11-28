import time
import math
from subprocess import call

screenwidth = 30
screenheight = 30
emptypixel = ' '

camera_angle = 1.0
screen_ratio = screenwidth / screenheight

screen = [emptypixel for i in range(screenwidth * screenheight)]


def clearmat(m):
    for i in range(screenwidth * screenheight):
        m[i] = emptypixel


def printmat(m):
    print()
    for i in range(screenwidth * screenheight):
        print(m[i], end=' ')
        if (i + 1) % screenwidth == 0:
            print()


class vec3:
    def __init__(self, X, Y, Z):
        self.x = X
        self.y = Y
        self.z = Z

    def __sub__(self, other):
        return vec3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __add__(self, other):
        return vec3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __mul__(self, num):
        return vec3(self.x * num, self.y * num, self.z * num)

    def __mod__(self, num):
        return vec3(self.x / num, self.y / num, self.z / num)

    def mag(self):
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    def normalize(self):
        return vec3(self.x, self.y, self.z) % self.mag()


class tri:
    def __init__(self, p1, p2, p3):
        self.p = [p1, p2, p3]

    def copy(self):
        return tri(self.p[0], self.p[1], self.p[2])


class mesh:
    def __init__(self, t):
        self.tris = t


def RotX(p, t):
    temp = vec3(0, 0, 0)
    temp.x = p.x
    temp.y = p.y * math.cos(t) + p.z * math.sin(t)
    temp.z = p.y * -math.sin(t) + p.z * math.cos(t)
    return temp


def RotY(p, t):
    temp = vec3(0, 0, 0)
    temp.y = p.y
    temp.x = p.x * math.cos(t) + p.z * -math.sin(t)
    temp.z = p.x * math.sin(t) + p.z * math.cos(t)
    return temp


def RotZ(p, t):
    temp = vec3(0, 0, 0)
    temp.z = p.z
    temp.x = p.x * math.cos(t) + p.y * math.sin(t)
    temp.y = p.x * -math.sin(t) + p.y * math.cos(t)
    return temp


def CrossProd(v1, v2):
    temp = vec3(0, 0, 0)

    temp.x = v1.y * v2.z - v1.z * v2.y
    temp.y = v1.z * v2.x - v1.x * v2.z
    temp.z = v1.x * v2.y - v1.y * v2.x

    return temp


def DotProd(v1, v2):
    return v1.x * v2.x + v1.y * v2.y + v1.z * v2.z


def drawline(one, two, m, cha):
    vecline = two - one
    dirx = -1 if vecline.x < 0 else 1
    diry = -1 if vecline.y < 0 else 1

    if one.x == two.x:
        for y in range(one.y, one.y + int(vecline.y)):
            if 0 <= one.x < screenwidth and 0 <= y < screenheight:
                m[y * screenwidth + one.x] = cha

    elif one.y == two.y:
        for x in range(one.x, one.x + int(vecline.x)):
            if 0 <= one.y < screenheight and 0 <= x < screenwidth:
                m[one.y * screenwidth + x] = cha



    else:
        xratio = vecline.x / vecline.y
        yratio = vecline.y / vecline.x

        if abs(vecline.x) > abs(vecline.y):

            for i in range(abs(vecline.x)):

                p = one + (vecline % (abs(vecline.x))) * i
                p.x = int(p.x)
                p.y = int(p.y)

                if 0 <= p.x < screenwidth and 0 <= p.y < screenheight:
                    m[p.y * screenwidth + p.x] = cha

        else:
            for i in range(abs(vecline.y)):

                p = one + (vecline % (abs(vecline.y))) * i
                p.x = int(p.x)
                p.y = int(p.y)

                if 0 <= p.x < screenwidth and 0 <= p.y < screenheight:
                    m[p.y * screenwidth + p.x] = cha


def ProjectPoint(p):
    global camera_angle, screen_ratio

    temp = vec3(0, 0, 0)
    f = (1 / math.tan(camera_angle / 2))

    temp.x = (p.x * (screen_ratio * f)) / p.z
    temp.y = (p.y * f) / p.z

    temp.x = int((temp.x + 1.0) * (screenwidth / 2))
    temp.y = int((temp.y + 1.0) * (screenheight / 2))

    return temp


t1 = tri(vec3(0, 0, 0), vec3(0, 1, 0), vec3(1, 1, 0))
t2 = tri(vec3(0, 0, 0), vec3(1, 1, 0), vec3(1, 0, 0))

t3 = tri(vec3(1, 0, 0), vec3(1, 1, 0), vec3(1, 1, 1))
t4 = tri(vec3(1, 0, 0), vec3(1, 1, 1), vec3(1, 0, 1))

t5 = tri(vec3(0, 1, 0), vec3(0, 1, 1), vec3(1, 1, 0))
t6 = tri(vec3(1, 1, 0), vec3(0, 1, 1), vec3(1, 1, 1))

t7 = tri(vec3(0, 0, 0), vec3(1, 0, 0), vec3(0, 0, 1))
t8 = tri(vec3(1, 0, 0), vec3(1, 0, 1), vec3(0, 0, 1))

t9 = tri(vec3(0, 0, 0), vec3(0, 1, 1), vec3(0, 1, 0))
t10 = tri(vec3(0, 0, 0), vec3(0, 0, 1), vec3(0, 1, 0))

t11 = tri(vec3(1, 0, 1), vec3(1, 1, 1), vec3(0, 1, 1))
t12 = tri(vec3(1, 0, 1), vec3(0, 1, 1), vec3(0, 0, 1))

cube = mesh([t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12])
a = 20
u = 0
theta = 0
while True:

    theta += 0.3
    clearmat(screen)
    for t in cube.tris:

        temp = t.copy()

        for i in range(3):
            temp.p[i] = temp.p[i] + vec3(-0.5, -0.5, -0.5)
            temp.p[i] = RotZ(temp.p[i], theta)
            temp.p[i] = RotZ(temp.p[i], theta)
            temp.p[i] = temp.p[i] * 10
            temp.p[i] = temp.p[i] + vec3(0, u, a)

        normal = CrossProd(temp.p[1] - temp.p[0], temp.p[2] - temp.p[0])
        scalar = DotProd(normal.normalize(), temp.p[0])

        if scalar < 0:
            for i in range(3):
                temp.p[i] = ProjectPoint(temp.p[i])

            drawline(temp.p[0], temp.p[1], screen, "+")
            drawline(temp.p[1], temp.p[2], screen, "+")
            drawline(temp.p[2], temp.p[0], screen, "+")

    printmat(screen)
    time.sleep(0.2)

printmat(screen)






