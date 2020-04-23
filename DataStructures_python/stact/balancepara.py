from array_stack import Stack


def is_valid(expr):
    st = Stack()

    for ch in expr:
        if ch in "({[":
            st.push(ch)
        if ch in "}])":
            if st.is_empty():
                print("right parentheses are more than left parathses")
                return False
            else:
                char = st.pop()
                if not match_parenthses(char, ch):
                    print("mismatched parenthesis are", char, "and", ch)
                    return False

    if st.is_empty():
        print("Balanced parantheses")
        return True

    else:
        print("left prentheses are more than right paratheses")
        return False


def match_parenthses(left, right):
    if left == "(" and right == ")":
        return True
    if left == "{" and right == "}":
        return True
    if left == "[" and right == "]":
        return True

    return False


while True:
    print("enter the expression with parentheses (q to quit)")
    exp = input()
    if exp == "q":
        break
    if is_valid(exp):
        print("valid expression")
    else:
        print("Invalid expression")
