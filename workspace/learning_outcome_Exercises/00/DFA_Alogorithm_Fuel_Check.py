#Ammad
#Reference:
 #   The code is also taken from the Graph Theory Lab.
 #   Edited the code and presented a real world example.
 #   Modified the code and showed a real-world scenario, 
 #   Where the features of graphs mathematics can be 
 #   easily understood.
#Algorithm: 
 #   Designed a Deterministic Finite Automata (DFA), 
 #   with alphabet {0,1}. 
    
 #   Assume a real-world example of a car fuel tank, if 
 #   tank is empty then take fuel from a fuel pump otherwise
 #   drive a car.
    
 #   Therefore, S0 state represents the fuel pump and S1 state
 #   represents the drive.
 #   S0 is the initial state and S1 is the accept state.
#Input:  '100001', '1000010', '0000001101010101010101010101010101', '10101010101010101', '00101010101010101'
#Output:
 #   100001 -> Drive
 #   1000010 -> Get Fuel
 #   0000001101010101010101010101010101 -> Drive
 #   10101010101010101 -> Drive
 #   00101010101010101 -> Drive
    
class State:
    """A state in an automaton."""
    def __init__(self, accept, arrows):
        # True if this is an accept state.
        self.accept = accept
        # Arrows (keys are labels) out of state.
        self.arrows = arrows

class DFA:
    """An automaton"""
    def __init__(self, Fuel):
        # Fuel state of the automaton.
        self.Fuel = Fuel

    def match(self, s):
        """See if s is accepted by the automaton."""
        # Current state.
        current = self.Fuel
        # Loop through the characters in s.
        for c in s:
            # Find the state in arrows with key c.
            current = current.arrows[c]
        # Return whether we're in an accept state.
        return current.accept


def compile():
    """Create the automaton."""

    # Create the Fuel state.
    Fuel = State(True, {})
    # Create drive state.
    drive = State(False, {})

    # The states point to themselves on a 0.
    Fuel.arrows['0'] = Fuel
    drive.arrows['0'] = Fuel

    # The states point to themselves on a 0.
    Fuel.arrows['1'] = drive
    drive.arrows['1'] = drive

    # Create an automaton.
    parity = DFA(Fuel)

    # return automaton.dx
    return parity

# Create automaton instance.

myautomaton = compile()
# A few small tests.
for s in ['100001', '1000010', '0000001101010101010101010101010101', '10101010101010101', '00101010101010101']:
    # Check if s is accepted by the automaton.
    res = myautomaton.match(s)    
    result = {True: "Get Fuel", False: "Drive"}
    # Print the result.
    print(f"{s} -> {result[res]}")