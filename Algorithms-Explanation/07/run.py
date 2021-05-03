import argparse
import reg 


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("regex", help="argument 1: Regular Expression, e.g. a.b.c*")
    parser.add_argument("file", help="argument 2: File Name without .txt extesnion")

    args = parser.parse_args()

    print("Your regular expression:", args.regex)
    print("Your test file name:    ", args.file+".txt")

    reg.input_file_name(args.file)
    reg.input_regex(args.regex)
    
    



