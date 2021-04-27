import shuntingre
import thompson


if __name__ == "__main__":
    tests = [  ["a|b.c",   ["ac", "bc", "bb", "aa"]]
             , ["(a|b).c", ["ac", "bc", "bb", "aa"]] 
    ]

    for test in tests:
        infix = test[0]
        print(f"infix:    {infix}")
        postfix = shuntingre.shunt(infix)
        print(f"postfix:  {postfix}")
        nfa = thompson.re_to_nfa(postfix)
        for s in test[1]:
            match = nfa.match(s)
            print(f"Match '{s}': {match}")
       