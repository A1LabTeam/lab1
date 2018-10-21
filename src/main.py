from enum import Enum


class Location(Enum):
    A = "a"
    B = "b"
    C = "c"


def success(rule):
    print("[+] " + rule + " success")


def fail(rule):
    print("[-] " + rule + " fail")


class State:
    def __init__(self, M, B, Box, On, success):
        self.M = M;
        self.B = B;
        self.Box = Box;
        self.On = On;
        self.success = success;

    def summary(self) -> str:
        condition = "(" + self.M.value + "," + self.B.value + "," + self.Box.value + "," + self.On.__str__() + "," + self.success.__str__() + ")"
        return condition

    # 猴子从state.M 移动到w
    def r1(self, w):
        currSummary = self.summary()
        if self.On != False or self.success != False:
            fail("r1")
        else:
            self.M = w
            success("r1")
        afterSummary = self.summary()
        print("from" + currSummary + "to" + afterSummary)

    # 猴子将state.M==state.Box 移动到z
    def r2(self, z):
        currSummary = self.summary()
        if self.M != self.Box or self.On != False or self.success != False:
            fail("r2")
        else:
            self.M = z
            self.Box = z
            success("r2")
        afterSummary = self.summary()
        print("from" + currSummary + "to" + afterSummary)

    # 猴子站上箱子
    def r3(self):
        currSummary = self.summary()
        if self.M != self.Box or self.On != False or self.success != False:
            fail("r3")
        else:
            self.On = True
            success("r3")
        afterSummary = self.summary()
        print("from" + currSummary + "to" + afterSummary)

    # 猴子从箱子上下来
    def r4(self):
        currSummary = self.summary()
        if self.M != self.Box or self.On != True or self.success != False:
            fail("r4")
        else:
            self.On = False
            success("r4")
        afterSummary = self.summary()
        print("from" + currSummary + "to" + afterSummary)

    # 猴子拿到香蕉
    def r5(self):
        currSummary = self.summary()
        if self.M != self.Box or self.M != self.B or self.On != True or self.success != False:
            fail("r5")
        else:
            self.success = True
            success("r5")
        afterSummary = self.summary()
        print("from" + currSummary + "to" + afterSummary)

    # run
    def run(self):
        if self.M != self.Box and self.On == True:
            print("init failed")
            return
        elif self.M != self.Box and self.On == False:
            self.r1(self.Box)
            self.run()
        elif self.On == True:
            if self.M == self.B:
                self.r5()
            else:
                self.r4()
                self.r2(self.B)
                self.r3()
                self.r5()
        else:
            if self.M == self.B:
                self.r3()
                self.r5()
            else:
                self.r2(self.B)
                self.r3()
                self.r5()


if __name__ == "__main__":
    # (monkey,香蕉,box,onbox??,get香蕉??)
    state = State(Location.C, Location.A, Location.C, True, False)
    state.run()
    # state.r1(Location.B)
    # state.r2(Location.C)
    # state.r3()
    # state.r5()
    if state.success:
        print("The monkey succeeded in getting the banana!")
