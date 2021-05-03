import shuntingre
import thompson



textFile = []


def input_file_name(fileName):
    # opening the text file
    with open(fileName+'.txt', 'r') as file:
        for line in file:
            for word in line.split(): 
                textFile.append(word)



def input_regex(regex):
    global match_result
    match_result = False
    tests = [ [regex,   textFile]]

    
    for test in tests:
        infix = test[0]
        print(f"infix:    {infix}")
        postfix = shuntingre.shunt(infix)
        print(f"postfix:  {postfix}")
        nfa = thompson.re_to_nfa(postfix)
        for s in test[1]:
            if nfa.match(s) == True:
                match = nfa.match(s)
                match_result = match
                print(f"Match Result: '{s}': {match}")
    return  match_result       
                        
