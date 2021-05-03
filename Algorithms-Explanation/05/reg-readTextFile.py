import shuntingre
import thompson

textFile = []
# opening the text file
with open('file.txt','r') as file:
    for line in file:
        for word in line.split(): 
            textFile.append(word)

    

if __name__ == "__main__":
    tests = [  ["(a.b.c*)", textFile]]

    
    for test in tests:
        infix = test[0]
        print(f"infix:    {infix}")
        postfix = shuntingre.shunt(infix)
        print(f"postfix:  {postfix}")
        nfa = thompson.re_to_nfa(postfix)
        for s in test[1]:
            if nfa.match(s) == True:
                match = nfa.match(s)
                print(f"Match '{s}': {match}")