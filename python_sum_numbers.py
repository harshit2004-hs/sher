import sys
 
def main():
    if len(sys.argv) != 3:
        print("Please provide two numbers.")
        return
 
    first = int(sys.argv[1])
    second = int(sys.argv[2])
    sum_ = first + second
    print(f"{first} + {second} = {sum_}")
 
if _name_ == "_main_":
    main()