from fib import Stack


def is_same(p1, p2):
        if p1 == '(' and p2 == ')':
                return True
        elif p1 == '[' and p2 == ']':
                return True
        elif p1 == '{' and p2 == '}':
                return True
        else:
                return False

def is_balanced(check_string):
        s = Stack()
        index = 0
        is_bal = True
        while index < len(check_string) and is_bal:
                paren = check_string[index]
                if paren in '{[(':
                        s.push(paren)
                else:
                        if s.is_empty():
                                is_bal = False
                        else:
                                top = s.pop()
                                if not is_same(top, paren):
                                        is_bal = False
                index += 1

        if s.is_empty() and is_bal:
                return True
        else:
                return False

        
print(is_balanced('[((())})]'))