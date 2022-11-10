''' Project 4 of cs2420 '''
from stack import Stack

def eval_postfix(exp: str) -> float:
    '''Evaluate a Postfix Expression'''
    if not isinstance(exp, str):
        raise ValueError()
    stack = Stack()
    for char in exp:
        if char in ('/', '*', '+', '-'):
            if stack.size() < 2:
                raise SyntaxError()
            match char:
                case '+':
                    stack.push(stack.pop() + stack.pop())
                case '-':
                    first = stack.pop()
                    stack.push(stack.pop() - first)
                case '*':
                    stack.push(stack.pop() * stack.pop())
                case '/':
                    first = stack.pop()
                    stack.push(stack.pop() / first)
        elif char == ' ':
            pass
        else:
            stack.push(float(char))
    return float(stack.top())


def in2post(exp: str) -> str:
    '''convert Infix to Postfix'''
    if not isinstance(exp, str):
        raise ValueError()
    postfix: str = ""
    stack = Stack()
    for char in exp:
        if char == '(':
            stack.push(char)
        elif char.isnumeric():
            postfix += char + ' '
        elif char in ('/', '*', '+', '-'):
            while stack.size() > 0 and stack.top() != '(' and (
                    stack.top() == '/' or stack.top() == '*' or char == '-' or char == '+'):
                postfix += stack.pop() + ' '
            stack.push(char)
        elif char == ')':
            if stack.size() < 1:
                raise SyntaxError()
            postfix += stack.pop() + ' '
            if stack.size() < 1:
                raise SyntaxError()
            while stack.top() != '(':
                postfix += stack.pop() + ' '
            stack.pop()
    while stack.size() > 0:
        if stack.top() == '(' or stack.top() == ')':
            raise SyntaxError()
        postfix += stack.pop() + ' '

    return postfix


def main():
    '''open data.txt, convert each expression to postfix, evaluate answer'''
    with open("data.txt", "r") as file:
        exps = file.readlines()

        for exp in exps:
            exp = exp.strip()
            print()
            print("infix: " + exp)
            postfix: str = in2post(exp)
            print("postfix: " + postfix)
            answer: str = eval_postfix(postfix)
            print("answer: " + str(answer))


if __name__ == "__main__":
    main()
