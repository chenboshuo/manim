# reference https://www.bilibili.com/read/cv2539928?from=search
from manimlib.imports import *


class HelloWorld(Scene):

    def construct(self):  # construct方法对于manim很特殊，manim调用这个方法来创建动画。所以基本上这个方法是在运行manim时必不可少的；

        # Making object
        # 创建了一个叫helloworld的对象，颜色为红色（RED），你也可以直接输入十六进制的颜色代码或其他颜色名称（如YELLOW，BLUE_B等，这个在manimlib.constants的COLOR_MAP可以查到）；
        hello = TextMobject("hello world", color=RED)

        # Position

        # Showing object
        self.play(Write(hello))
        self.wait(10)
