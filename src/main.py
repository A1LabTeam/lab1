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

    def r1(self, w):
        currSummary = self.summary()
        if self.On != False or self.success != False:
            fail("r1")
        else:
            self.M = w
            success("r1")
        afterSummary = self.summary()
        print("from" + currSummary + "to" + afterSummary)

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

    def r3(self):
        currSummary = self.summary()
        if self.M != self.Box or self.On != False or self.success != False:
            fail("r3")
        else:
            self.On = True
            success("r3")
        afterSummary = self.summary()
        print("from" + currSummary + "to" + afterSummary)

    def r4(self):
        currSummary = self.summary()
        if self.M != self.Box or self.On != True or self.success != False:
            fail("r4")
        else:
            self.On = False
            success("r4")
        afterSummary = self.summary()
        print("from" + currSummary + "to" + afterSummary)

    def r5(self):
        currSummary = self.summary()
        if self.M != self.Box or self.M != self.B or self.On != True or self.success != False:
            fail("r5")
        else:
            self.success = True
            success("r5")
        afterSummary = self.summary()
        print("from" + currSummary + "to" + afterSummary)

if __name__ == "__main__":
    state = State(Location.A, Location.C, Location.B, False, False)
    state.r1(Location.B)
    state.r2(Location.C)
    state.r3()
    state.r5()
    if state.success:
        print("The monkey succeeded in getting the banana!")
