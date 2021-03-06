
<a href="">

# graph-theory-project
- **Student ID G00365389**

# [Project Plan](https://i.imgur.com/JR9igmP.png)

**Graph Theory Learning outcomes**
  - Describe the mathematical properties of graphs.
  - Formulate and model problems using graph theory.
  - Solve computational problems using graph theory.
  - Investigate graph theoretical concepts using a computer.



# Table of contents
1. [Algorithms Explanation](#explain-algorithm)   
2. [How to Run & Test Program?](#how2run-program)
4. [Question & Answers](#qa)


#### Algorithms Explanation <a name="explain-algorithm"></a>
- Algorithms
  * The following algorithms are described in detail in the section.
    * **Collatz**       Algorithm
    * **Shunting**      Algorithm
    * **Shuntingre**    Algorithm   //Shunting Regular Expression
    * **Thompson**      Algorithm
  
  * All learning outcomes are based on lab code and hand-sketch exercises.

    * **#.00** Using lab code (even-p.py) and demonstrating how the concept of graph theory solves real-world problems.
        - Lesson Learnt:
            * Solved real world problem using DFA.[Hand-Sketh, Transistions](https://i.imgur.com/UbtGZH3.jpg)
            
    * **#.01** Examined the shunting-yard model and explained the concept in table shape and arrows showed how the elements are saved in stack and post memory.
        - Lesson Learnt:
            * Shunting-yard Model.[code](https://github.com/ammadaslam/graph-theory-project/tree/main/workspace/learning_outcome_Exercises/01)
            * Shunting-yard Algorithm.[Explanation](https://i.imgur.com/TWdVdRq.png)
                             
    * **#.02** Explained how the Thomson algorithm works, using concatenation as regular expression. 
        - Lesson Learnt:
            * Formulate and model regular expression concatenation using graph theory. 
            * Hand-Sketch Thomson NFA.[Concatenation a.b ](https://i.imgur.com/eMq28X1.png)
            * Hand-Sketch Thomson NFA, [Transitions](https://i.imgur.com/FJ1hI6y.png)
            * Hand-Sketch Last In and First Out from Stack,[LIFO](https://i.imgur.com/t9QYZ4I.png)
            * Searched concatenation set of string using computational algorithms. [code](https://github.com/ammadaslam/graph-theory-project/tree/main/workspace/learning_outcome_Exercises/02)

    * **#.03** Explained how the Thomson algorithm works, using Union as regular expression.
        - Lesson Learnt:
            * Formulate and model regular expression Union using graph theory. 
            * Hand-Sketch Thomson NFA .[Union a|b](https://i.imgur.com/C0VeuvV.png)
            * Searched Union set of string using computational algorithms. [code](https://github.com/ammadaslam/graph-theory-project/tree/main/workspace/learning_outcome_Exercises/03)

    * **#.04** Explained how the Thomson algorithm works, using Kleene Start as regular expression.
        - Lesson Learnt:
            * Formulate and model regular expression Kleene Start using graph theory. 
            * Hand-Sketch. NFA [Kleene Start a*](https://i.imgur.com/krp0y6N.png)
            * Hand-Sketch, [Kleene Start Transitions](https://i.imgur.com/FIhskn4.png)
            * Searched Kleene Start set of string using computational algorithms. [code](https://github.com/ammadaslam/graph-theory-project/tree/main/workspace/learning_outcome_Exercises/04)

    * **#.05** Reads the file line by line and outputs result from the file that matched the regular expression.
  

    * **#.06**  Added Python command line parsing (argparse)[https://docs.python.org/3/library/argparse.html]
    
    * **#.07**  Python Unit Testing.
      -Added 9 test cases 
      -Enter in the command line: python test.py
    


## How to run & test program? <a name="how2run-program"></a>

- Prerequisites:
  * (Download Latest version Python3)[https://www.python.org/downloads/]
  * (Clone Git Project)[https://github.com/ammadaslam/graph-theory-project]

- Project Directory Structure
  * Root directory 
    * graph-theory-project
  * Sub directories
    * run.py                 - Main Program 
    * test.py                - The test script includes 9 tests. 
    * file.txt               - Text file contain specific regular language.
    * file2.txt              - Text file 2 contain regular language in paragraph.
    * reg.py                 - This lab code has been slightly modified to read text files
    * shuntingre.py          - This lab code is used as it is.
    * thompson.py            - Modified (+) operator only and it is not complete yet. [Hand-Sketch](https://i.imgur.com/0ynEY1i.png)
    * Algorithms-Explanation - All algorithms are explained in this directory [00-04]

- How to run test script?
  * python3 test.py [Screen-Shot](https://i.imgur.com/OkaEOZy.png)
  
  
- How to run main program? 
  * python3 run.py -h
  * python3 run.py a.b.c* file [Screen-Shot](https://i.imgur.com/vj8yJyE.png)
  * python3 run.py (a.b|b*) file2


## Question & Answers <a name="qa"></a>
- What is a regular expression?
  * **Answer**:

Regular expressions are also termed as regexes, reg-ex, regexp, REs or regex patterns. Regular expression are used for representing certain sets of strings in a regular expression. 
 
The extremely specialized programming language used inside Python and the re module is used for making them available. By employing this language, you specify the rules for the probable strings set which you wish to match. Such sets may include e-mail addresses, English phrases, or tax orders, or your wishes. For example questions like this "Does this match the pattern?" You can also use regular expressions to edit or separate strings in different ways.

Regular expression gained popularity in the late 1960s. The early appearances of RE in programming can be credited to develop Kleene's notation. To match different patterns in multiple text files.
For speed, the implementation of regular expression was performed by using JIT to IBM 7094 code 
on the Compatible Time-Sharing System. Ken Thompson.

A relatively more complex race emerged in Pearl in the late 1980s. They are originally from a Regex library. In the current scenario, the RE is largely supported by text processing programs, programming languages and various other programs.

RE is an element of the standard library of various programming languages, including Python, etc. Deployment of RE functionality are mostly known as a regular expression engine, and various libraries are there for reuse.

RE are universal and they are existed in the latest programming frameworks and can also be found in UNIX tools 1970s.
Any modern programming language is incomplete if it does not support the RE.
 
In early 1943, when Warren McCulloch and Walter Pitts released a logical calculation of the concepts involved in neural activity. This research was, in fact, the starting point for regular expression and introduced the first mathematical model of the neural network.

In 1968, a contributor of computer science (Ken Thompson) understood and expanded on Kleene, publishing his work in regular expression.
The most important concept related to regular expression.

- Literal Characters
  * The most basic regex comprises of a single literal character. It matches the first occurrence of that character in the string. The maiden occurrence of the string character is mapped by it. For example, consider a string "Graph Theory Project". In this case, the 'r' after the G will be matched by the regular expression.

- Character Classes 
  * The "character class" regex engine is used to indicate that it needs to match a single character between a group of characters.
  Suppose you want to match an o or u, then you will use [ou].
  For example, this is especially helpful when you are unsure whether the document you are looking for is British or English style. hum[ou]r will not match humour, humor or any similar characters. For the character class, it doesn't matter what the order of the characters is and the result is the same. A word can be searched even though its spelling is not like hum[o]r.

  A hyphen can be employed in a character class to describe a particular character set.
  [0-20] will provide a digit match that is between 0 and 9.

- Anchors 
  * Anchors work by matching a particular place, either before or after or between the letter, rather than a matching any specific character.

- Repetition Operator
  * There are three main iteration operators: asterisk, question mark, star. The preceding token in the regex is made selective by using question mark.
  For example Dec(ember)? Will match Dec as well as December.The asterisk or star commands the regex engine to try to match the former token either zero or multiple times.

---
references:
- title: Python Regular Expressions [Learn Python Regular Expression in an Easy Way]
  Chapter: 1 Introduction to regular expression
  publisher: Acodemy
  page: 08-14
  type: Book
  issued:
    year: 2015
---


- How do regular expressions differ across implementations?
  * **Answer**:

The "regular expressions" in the more scientific sense that can match regular languages
and on the other hand language that can match significantly more complex programming languages Perl, Python, java all most any language. Most of them rely on a particular
style called Perl Compatible Regular Expression (PCRE).

- Academic Regular Expression
  * First of all we discussed general academic regular expressions are quite limited but their
  efficient implementation is more interesting as compared to power full regular expression based on PCRE. 

  Regular expressions are matching certain set of strings from alphabets fashion. 
  In general, a set of strings is known as a language, and in particular the set that can be defined by the use of regular expressions is called regular languages.

  Sigma (??) is a finite set called the alphabet. There is always the null expression  ???  which doesn't match anything at all and  ??  which only match the empty string. An example of a sets,  ??????{}  and  ?????{??????}.

  We can also combine the above expressions to form a more complex. Such as concatenation: given regular expressions  a  and  b ,  a.b  matches  a  followed by  b. 
  So if  a???{???ab???,???cd???}  and  b???{???ef???}  then  a.b???{???abef???,???cdef???} .

  There is an operation called alternation (union), Given  a  and  b ,  a|b  matches if either  a  or  b  match.  a|b???{???ab???,???cd???}???{???ef???} = {???ab???,???cd???,???ef???} .

  Another operation is the Kleene star which is repetition. Given an expression  a ,  a???  matches the empty string ( ?? ),  a ,  aa  and so on. This is also where the  ?????  notation comes from for the set of strings. Given the  a  above,  a??????{??????,???ab???,???cd???,???abab???,???abcd???,???cdcd???,???}.

  Also have some additional operation like  a+  for matching at least one or more instance of an expression. This operation also written as  aa??? .
  - Design Nondeterministic Finite Automata(NFA) and Deterministic Finite Automata(DFA):
    * Effectively design regular expressions into a finite state automata. Every DFA is an NFA but not the vise versa. Both the NFA and the DFA have 5 tuples (Q,??,Transition function:,q0,F).
      
      Q = is a finite set of states,
      ?? = is a finite set called the alphabet,
      Transition function: = is the transition function (Q ?? ?? -> Q),
      q0 =  is the start state (??? Q), and
      F = is the set of accept states (??? Q).
    This only difference DFA always have exactly one state to transition to when in
  any given state and reading any given symbol. On the other hand NFA finite automata can have any number of arrows for each state and symbol.

  The empty string ??? = {??????} is also used to label arrows that are followed without reading a character from the input, while also remaining in the original state.

  Non-determinism can simplify automata but it can be shown that NFAs and DFAs recognise the same set of languages.

  - Implementation (NFA/DFA)
    * A NFA is made up of a bunch of states SS and the transitions between them F:Q???????P(Q).
    At given current state there could be multiple next states. The next state may be chosen at random or all the next states may be chosen in parallel. So it make matching operation possible and fast implementation.

    * In DFA, given the current state we know what the next state will be. It has no choice only one unique next state. Hence it simple and easy to design.

- Module Based Regexps
  * Module-based regexps provides regular expression matching operations, such as those found in Pearl. The regexps modules in most languages are actually more powerful.
  Both patterns and strings to be searched can be Unicode strings (str) as well as 8-bit strings (bytes). 
  The important point to make clear here is that these module based regex cannot be implemented as NFA / DFA methods.


---
references:
- title: Python Standard Library
  Topic: re-Regular expression operations
  type:  Documentation
  Url:   https://docs.python.org/3/library/re.html
  version:
    English: 3.9.4

references:
- title: Regular Expressions.info
  Topic: re-Regular expression operations
  type:  website
  Url:   http://www.regular-expressions.info/refunicode.html
  date:
    last update: Nov 2019

references:
- title: Implementing a Regular Expression Engine
  type:  website/Article
  Url:   https://deniskyashif.com/2019/02/17/implementing-a-regular-expression-engine/
  date:
    published: Feb 2019

references:
- title: How are regular expressions implemented?
  type:  website/Blog
  Url:   https://www.quora.com/How-are-regular-expressions-implemented
  date:
    published : 4 years ago, by  Daniele Paolo Scarpazza, PhD in Computer Engineering. and Valeriy Ivanov, M.S. Wireless Telecommunications & Software Engineering, MTUCI (2010)

---
  



- Can all formal languages be encoded as regular expressions?
  * **Answer**:

  Before answering this question, it is important to understand the difference between formal language, regular language and regular expression. So the answer is divided into three parts and in the third part it will give a clear understanding and correct answer to this question.

  -First define the formal language:
    - [Basic Definition](https://introcs.cs.princeton.edu/java/51language/)
      * A symbol is the basic building block, typically a character or a digit.
      * An alphabet is a finite set of symbols.
      * A string is a finite sequence of alphabet symbols.
      * A formal language is a set of strings (possibly infinite), all over the same alphabet.

  Any alphabet can be used when working with formal languages. Hence the Roman alphabet used for text processing and the decimal numbers used for number processing. and so forth.

  -Second define the regular language:
    This is an important class of formal languages called regular languages. For which we can solve specified problems.
    The union (U), concatenation(.), and closure (*) operations on sets, along with parentheses, to specify a regular language

    - The union R1 | R2 of two formal languages R1 and R2 is the set of strings that are in either R1 or R2 (or both). 
      * For example,
          R1 = { a, ba }
          R2 = { ab, ba, b }
          (R1 U R2) = { a, ba } | { ab, ba, b } = { a, ab, ba, b }

    - The concatenation R1R2 of two formal languages R1 and R2 is the set of all strings that can be created by appending a string from R to a string from R2. Note, duplicate results are not allowed.
      * For example,
          R1 = { a, ab }
          R2 = { a, ba, bab }
          (R1R2) = { a, ab } { a, ba, bab } = { aa, aba, abab, abba, abbab }

    - The closure R* of a formal language R is the concatenation of zero or more strings from R.
      * R* = {??,R,RR,RRR,RRRR,...}      

  -Third define the regular expression:
    For every regular expression, there is a corresponding regular set of language

                        **Regular expression**  	**Regular Set**
                            ???                       {}
                            a for a ??? ??             {a}
                              ???	                    {???}
                            (R1 U R2)             L(R1) U L(R2)
                            (R1R2)                L(R1)L(R2)
                            (R*)                  L(R*)
                            R+                     RR*

    RE is a string of symbols that specifies a formal language. RE is either an alphabet symbol or composed from the following operations (where R1 and R2 are REs):
    - Union:
      * R1 | R2, specifying the union of the sets R1 and R2,
    - Concatenation:
      * R1R2, specifying the concatenation of the sets R1 and R2,
    - Closure:
      * R*, specifying the closure of the set R,
    - Parentheses:
      (R), specifying the same set as R.


  Conclusion: A formal language is encoded if and only if it can be specified by an RE.
  **Therefore, not all formal languages are encoded in regular expressions.**


  ---
  references:
  - title: Formal Language
    type:  website
    Url:   https://introcs.cs.princeton.edu/java/51language/
    date:
      published: August 2016

  references:
  - title: Formal Language
    type:  website
    Url:   https://archive.csfieldguide.org.nz/2.7.1/en/chapters/formal-languages.html
    published:
      CS Education Research Group, University of Canterbury, New Zealand
      
  references:
  - title: Regular Expressions and Formal Languages
    type:  Article
    Url:   https://dzone.com/articles/back-basics-regular
    date:
      posted: March 2014

  references:
  - title: What is the Relationship Between Programming Languages, Regular Expressions and   Formal Languages
    type:  blog/stackoverflow
    Url:   https://cs.stackexchange.com/questions/30639/what-is-the-relationship-between-programming-languages-regular-expressions-and


  references:
  - title: Regular expression
    type:  wikipedia
    Url:   https://en.wikipedia.org/wiki/Regular_expression

  references:
  - Recommended Resource:
      * Url:  https://realpython.com/regex-python/
      * Url:  https://realpython.com/python3-object-oriented-programming/
      * Url:  http://norvig.com/21-days.html
      * Url:  https://stackoverflow.blog/2020/05/27/2020-stack-overflow-developer-survey-results/
      * Url:  https://github.com/ianmcloughlin/fib-languages
      * Url:  https://hckrnews.com/
      * Url:  https://realpython.com/
      * Url:  https://docs.python.org/3/library/unittest.html
      
  ---
