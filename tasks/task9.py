from enum import Enum


class State(Enum):
    A = 0
    B = 1
    C = 2
    D = 3
    E = 4
    F = 5
    G = 6


class StateMachine:
    state = State.A

    def cue(self):
        return self.update({
            State.A: [State.A, 2],
            State.C: [State.D, 5],
            State.E: [State.F, 8],
        })

    def turn(self):
        return self.update({
            State.A: [State.B, 0],
            State.B: [State.C, 3],
            State.C: [State.A, 6],
        })

    def march(self):
        return self.update({
            State.B: [State.F, 4],
            State.F: [State.G, 9],
            State.A: [State.G, 1],
            State.D: [State.E, 7],
        })

    def update(self, transitions):
        self.state, signal = transitions[self.state]
        return signal


def main():
    return StateMachine()

o = main()
o.turn() # 0
o.turn() # 3
o.turn() # 6
o.cue() # 2
o.turn() # 0
o.turn() # 3
o.cue() # 5
o.march() # 7
o.cue() # 8
o.turn() # KeyError
o.march() # 9