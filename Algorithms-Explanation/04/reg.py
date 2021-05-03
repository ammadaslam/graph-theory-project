import shuntingre
import thompsonKleeneStar


if __name__ == "__main__":
    tests = [  ["a*",   ["", "a", "aa", "aaaa", "aaa","baaa"]]
             , ["1*", ["", "1", "11","111","0111"]]
             , ["0*", ["", "0", "00","000","1000"]]
             ]

    for test in tests:
        infix = test[0]
        print(f"infix:    {infix}")
        postfix = shuntingre.shunt(infix)
        print(f"postfix:  {postfix}")
        nfa = thompsonKleeneStar.re_to_nfa(postfix)
        for s in test[1]:
            match = nfa.match(s)
            print(f"Match '{s}': {match}")
       