import shuntingre
import thompsonConcatenation

if __name__ == "__main__":
    tests = [  ["a.a",   ["ab", "b", "bb", "aa"]]
             , ["c.a", ["ac", "abca", "aabcaca", "ca"]]
             , ["e.e", ["eee", "abee", "eeca", "ee"]]
    ]

    for test in tests:
        infix = test[0]
        print(f"infix:    {infix}")
        postfix = shuntingre.shunt(infix)
        print(f"postfix:  {postfix}")
        nfa = thompsonConcatenation.re_to_nfa(postfix)
        for s in test[1]:
            match = nfa.match(s)
            print(f"Match '{s}': {match}")
       