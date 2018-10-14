import State
import location as l

if __name__ == "__main__":
    state = State.State(l.Location.A, l.Location.C, l.Location.B, False, False)
    state.r1(l.Location.B)
    state.r2(l.Location.C)
    state.r3()
    state.r5()
    if state.success:
        print("The monkey succeeded in getting the banana!")
