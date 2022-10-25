from tokenize import Double
from stack import Stack

def eval_postfix(exp: str) -> str:
    '''Evaluate a Postfix Expression'''
    stack = Stack()
    for char in exp:
        if char.isnumeric(): 
            stack.push(int(char))
        else:
            match char:
                case '+':
                    stack.push(stack.pop() + stack.pop())
                case '-':
                    stack.push(stack.pop() - stack.pop())
                case '*':
                    stack.push(stack.pop() * stack.pop())
                case '/':
                    stack.push(stack.pop() / stack.pop())
    return stack.top()

def in2post(exp: str) -> str:
    '''convert Infix to Postfix'''
    stack = Stack()
    for char in exp:
        if char == '(':
            stack.push(char)
        
    return exp

def main():
    file = open("data.txt", "r")
    exps = file.readlines()

    for exp in exps:
        exp = exp.strip()
        print()
        print(exp)
        postfix: str = in2post(exp)
        print(postfix)
        print(eval_postfix(postfix))

    file.close() 

if __name__ == "__main__":
    main()