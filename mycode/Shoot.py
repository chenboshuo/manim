# reference https://www.bilibili.com/read/cv2539928?from=search
from manimlib.imports import *


def scope():
    """ Generage the aim scope"""
    circle1 = Circle(color=BLUE)
    circle2 = Circle(color=RED, fill_color=RED, fill_opacity=1)
    circle2.scale(0.1)
    line1 = Line(vector(-1, 0), vector(1, 0), color=RED)
    line2 = Line(vector(0, 1), vector(0, -1), color=RED)
    return VGroup(circle1, circle2, line1, line2)


def vector(x, y, z=0):
    """Return np.array([x,y,z])"""
    return np.array([x, y, z])


class Shoot(Scene):

    def construct(self):
        # Making self.aim_scope

        self.aim_scope = scope()

        # Making target
        self.target_list = []
        for i in range(3):
            for j in range(5):
                target_ij = Circle(
                    color=YELLOW, fill_color=YELLOW, fill_opacity=0.4)
                target_ij.scale(0.4)
                target_ij.shift(vector(-4+j*2, -2+i*2))
                self.play(FadeIn(target_ij))
                self.target_list.append(target_ij)

        self.wait(1)

        self.add(self.aim_scope)
        self.play(ApplyMethod(self.aim_scope.shift, DOWN*3 + LEFT*6.1))
        self.shoot_ij(0, 1)
        self.shoot_ij(2, 0)
        self.shoot_ij(1, 3)
        self.shoot_ij(0, 0)
        self.shoot_ij(2, 4)

    def shoot_ij(self, i, j):
        """Shoot the target (i,j)""""
        target_ij = self.target_list[j+i*5]
        self.play(ApplyMethod(self.aim_scope.next_to, target_ij, 0))
        self.play(ApplyMethod(target_ij.set_fill, GREY),
                  ApplyMethod(target_ij.set_color, GREY))
        self.wait(0.5)
        ij = TextMobject(f"({i},{j})", color=GREY)
        ij.next_to(target_ij, DOWN)
        self.play(Write(ij))
        self.wait(1)
        return 0
