import unittest
import reg 



class TestCases(unittest.TestCase):
    
    fileName = "file"
    reg.input_file_name(fileName)
    
    print("\n\t Note: All regular expressions from this file has been searched. --> ",fileName+'.txt',"\n\n")
    
    def test_case_1(self):
        result = reg.input_regex("a.b.c")
        expected = True
        print("\tExpected result:  ",True,)
        print("\tActual result:    ", result,"\n\n")
        self.assertEqual(expected, result)
        
    def test_case_2(self):
        result = reg.input_regex("a.b.c*")
        expected = True
        print("\tExpected result:  ",True,)
        print("\tActual result:    ", result,"\n\n")
        self.assertEqual(expected, result)
    
    def test_case_3(self):
        result = reg.input_regex("(a.b|b*)")
        expected = True
        print("\tExpected result:  ",True,)
        print("\tActual result:    ", result,"\n\n")
        self.assertEqual(expected, result)

    def test_case_4(self):
        result = reg.input_regex("a.(b.b)*.a")
        expected = True
        print("\tExpected result:  ",True,)
        print("\tActual result:    ", result,"\n\n")
        self.assertEqual(expected, result)

    def test_case_5(self):
        result = reg.input_regex("(a.a*)")
        expected = True
        print("\tExpected result:  ",True,)
        print("\tActual result:    ", result,"\n\n")
        self.assertEqual(expected, result)   

    def test_case_6(self):
        result = reg.input_regex("a*")
        expected = True
        print("\tExpected result:  ",True,)
        print("\tActual result:    ", result,"\n\n")
        self.assertEqual(expected, result)
        
    
    def test_case_7(self):
        result = reg.input_regex("1*")
        expected = True
        print("\tExpected result:  ",True,)
        print("\tActual result:    ", result,"\n\n")
        self.assertEqual(expected, result)     
        
    def test_case_8(self):
        result = reg.input_regex("0*")
        expected = True
        print("\tExpected result:  ",True,)
        print("\tActual result:    ", result,"\n\n")
        self.assertEqual(expected, result)

    def test_case_9(self):
        result = reg.input_regex("1.(0.0)*.1")
        expected = True
        print("\tExpected result:  ",True,)
        print("\tActual result:    ", result,"\n\n")
        self.assertEqual(expected, result)

unittest.main()