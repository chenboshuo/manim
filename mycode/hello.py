# reference https://www.bilibili.com/read/cv2539928?from=search
from manimlib.imports import *


class HelloWorld(Scene):

    def construct(self):  # construct方法对于manim很特殊，manim调用这个方法来创建动画。所以基本上这个方法是在运行manim时必不可少的；

        # Making object
        # 创建了一个叫helloworld的对象，颜色为红色（RED），你也可以直接输入十六进制的颜色代码或其他颜色名称（如YELLOW，BLUE_B等，这个在manimlib.constants的COLOR_MAP可以查到）；
        hello = TextMobject("hello world", color=RED)
        rectangle = Rectangle(color=BLUE)
        rectangle.surround(hello)  # 让该矩形包裹 hello

        # 将两个东西合并为VGroup,所有Mobject都可以打包为VGroup, VGroup 可以嵌套
        group1 = VGroup(hello, rectangle)

        hello_manim = TextMobject("hello Manim", color=BLUE)
        hello_manim.scale(2.5)

        # Position

        # Showing object
        self.play(Write(hello))
        self.wait(5)
        self.play(FadeIn(rectangle))
        self.wait(5)
        self.play(ApplyMethod(group1.scale, 2.5))
        self.wait(5)
        self.play(Transform(hello, hello_manim))
        self.wait(5)
