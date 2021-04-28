
<a href="">

# graph-theory-project
- **Student ID G00365389**


**Learning outcomes**
  - Describe the mathematical properties of graphs.
  - Formulate and model problems using graph theory.
  - Solve computational problems using graph theory.
  - Investigate graph theoretical concepts using a computer.




# Table of contents
1. [Introduction](#introduction)
    1. [Readme About Directory Structure](#dir-structure)
        1. [Workspace](#workspace)
        2. [Regular Expression Search (Algorithm)](#regexp-algorithm)
    
2. [How to Run & Test Program?](#how2run-program)
3. [Algorithms Explanation](#explain-algorithm)  
4. [Question & Answers](#qa)




## Introduction <a name="introduction"></a>

  



### Readme about directory structure <a name="dir-structure"></a>
The workspace directory includes labs, notes, learning outcomes based exercises.
Another directory includes a regular expression algorithm that reads the file using command line arguments and reads the file by line and outputs the lines of the file matching the regular expression.
#### Workspace <a name="workspace"></a>
- Workspace
  * Labs
    * **Collatz**       Algorithm
    * **Shunting**      Algorithm
    * **Shuntingre**    Algorithm   //Shunting Regular Expression
    * **Thompson**      Algorithm
  * Notes
    * Finite_Automata
    * Language
    * Thomas_Construction
    * Thompson-hand-sketch

  * Learning_Outcomes
    * **#.00** Using lab code (name of code), Graph Theory concept solves the real world problem. 
        - Lesson Learnt:
            * Solved real world problem using DFA.[Hand-Sketh, Transistions](https://i.imgur.com/r72EpOH.jpg)
            
    * **#.01** Examined the shunting-yard model and explained the concept in table shape and arrows showed how the elements are saved in stack and post memory.
        - Lesson Learnt:
            * Shunting-yard Model.[code](https://github.com/ammadaslam/graph-theory-project/tree/main/workspace/learning_outcome_Exercises/01)
            * Shunting-yard Algorithm.[Explanation](https://i.imgur.com/FOQRLoP.png)

    * **#.02** Explained how the Thomson algorithm works, using concatenation as regular expression. 
        - Lesson Learnt:
            * Formulate and model regular expression concatenation using graph theory. 
            * Hand-Sketch Thomson NFA.[Concatenation a.b ](https://i.imgur.com/UaY1zln.png)
            * Hand-Sketch Thomson NFA, [Transitions](https://i.imgur.com/rFkOKsW.png)
            * Searched concatenation set of string using computational algorithms. [code](https://github.com/ammadaslam/graph-theory-project/tree/main/workspace/learning_outcome_Exercises/02)

    * **#.03** Explained how the Thomson algorithm works, using Union as regular expression.
        - Lesson Learnt:
            * Formulate and model regular expression Union using graph theory. 
            * Hand-Sketch Thomson NFA .[Union a|b](https://i.imgur.com/mEshxJg.png)
            * Searched Union set of string using computational algorithms. [code](https://github.com/ammadaslam/graph-theory-project/tree/main/workspace/learning_outcome_Exercises/03)

   * **#.04** Explained how the Thomson algorithm works, using Kleene Start as regular expression.
        - Lesson Learnt:
            * Formulate and model regular expression Kleene Start using graph theory. 
            * Hand-Sketch. NFA [Kleene Start a*](https://i.imgur.com/4nNNGNB.png)
            * Hand-Sketch, [Kleene Start Transitions](https://i.imgur.com/ZYPYLFE.png)
            * Searched Kleene Start set of string using computational algorithms. [code](https://github.com/ammadaslam/graph-theory-project/tree/main/workspace/learning_outcome_Exercises/04)


Describe the mathematical properties of graphs.
  - Formulate and model problems using graph theory.
  - Solve computational problems using graph theory.
  - Investigate graph theoretical concepts using a computer.

#### Regular Expression Search (Algorithm) <a name="regexp-algorithm"></a>
- regular-expression-algorithm




## How to run & test program? <a name="how2run-program"></a>


















## Algorithms Explanation <a name="explain-algorithm"></a>









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
  



- Can all formal languages be encoded as regular expressions?
  * **Answer**:
