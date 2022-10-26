from stack import Stack

def eval_postfix(exp: str) -> float:
    '''Evaluate a Postfix Expression'''
    if not isinstance(exp, str):
        raise ValueError()
    stack = Stack()
    print(exp)
    for c in exp:
        if c == '/' or c == '*' or c == '-' or c == '+':
            if stack.size() < 2:
                raise SyntaxError()
            match c:
                case '+':
                    stack.push(stack.pop() + stack.pop())
                case '-':
                    stack.push(stack.pop() - stack.pop())
                case '*':
                    stack.push(stack.pop() * stack.pop())
                case '/':
                    stack.push(stack.pop() / stack.pop())
        elif c == ' ':
            pass
        else:
            stack.push(float(c))
    return float(stack.top())


def in2post(exp: str) -> str:
    '''convert Infix to Postfix'''
    if not isinstance(exp, str):
        raise ValueError()
    postfix: str = ""
    stack = Stack()
    for c in exp:
        if c == '(':
            stack.push(c)
        elif c.isnumeric():
            postfix += c + ' '
        elif c == '/' or c == '*' or c == '-' or c == '+':
            while stack.size() > 0 and stack.top() != '(' and (
                    stack.top() == '/' or stack.top() == '*' or c == '-' or c == '+'):
                postfix += stack.pop() + ' '
            stack.push(c)
        elif c == ')':
            postfix += stack.pop() + ' '
            while stack.top() != '(':
                postfix += stack.pop() + ' '
            stack.pop()
    while stack.size() > 0:
        if stack.top() == '(' or stack.top() == ')':
            raise SyntaxError()
        postfix += stack.pop() + ' '

    return postfix


def main():
    file = open("data.txt", "r")
    exps = file.readlines()

    for exp in exps:
        exp = exp.strip()
        print()
        print("infix: " + exp)
        postfix: str = in2post(exp)
        print("postfix: " + postfix)
        answer: str = eval_postfix(postfix)
        print("answer: " + str(answer))

    file.close()


if __name__ == "__main__":
    main()
