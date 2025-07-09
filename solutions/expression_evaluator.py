import re


def calculate(input_expression: str):
    """
    Parses and calculates a mathematical expression represented as a string. The expression
    can include basic arithmetic operations: addition (+), subtraction (-), multiplication (*),
    and division (/). The method supports handling operator precedence for
    multiplication and division before addition and subtraction.

    :param input_expression: A string representing the mathematical expression to evaluate.
                             Contains numbers and the following operators: +, -, *, /.
                             Must not contain any invalid characters or improperly formatted expressions.
    :type input_expression: str

    :return: The computed result of the mathematical expression as an integer or float.
    :rtype: Union[int, float]

    :raises ValueError: If the input expression contains invalid characters or is improperly formatted.
    """
    num, action, p_num, p_action = None, None, None, None
    for expr in re.split(r"([+-/*])", input_expression.replace(" ", "")):
        if expr.isdigit():
            match expr:
                case expr if p_action is None and p_num is None and num is None:
                    if action is not None:
                        num, action = int(action + expr), None
                        continue
                    num = int(expr)
                case expr if p_action is None and p_num is None and num is not None:
                    p_num = int(expr)
                case expr if p_action in "*/" and p_num is not None:
                    p_num, p_action = p_num / int(expr) if p_action == "/" else p_num * int(expr), None
                case expr if p_action in "*/" and p_num is None and num is not None:
                    num, p_action = num / int(expr) if p_action == "/" else num * int(expr), None
        elif expr == "":
            continue
        elif expr in "*/+-":
            match expr:
                case expr if expr in "*/":
                    p_action = expr
                case expr if expr in "+-" and action is None:
                    action = expr
                case expr if expr in "+-":
                    num, action, p_num = num - p_num if action == "-" else num + p_num, expr, None
        else:
            raise ValueError(f"Invalid value/sign in expression: {expr}")

    if num is not None and action is not None and p_num is not None:
        num = num + p_num if action == "+" else num - p_num

    return num


examples = [
    "10 / 5",
    "10 + 5 * 2 - 3",
    "1 + 4 / 2",
    "1 + 2",
    "3 * 2 / 2",
    "1 + 3 * 2 / 2",
    "1 + 3 * 2 / 2 + 1",
]


if __name__ == "__main__":
    for example in examples:
        print(f"{example} = {calculate(example)}")
    user_input = input("Enter an expression: ")
    if not user_input:
        print("Skip empty expression")
        exit()
    else:
        print(f"{user_input} = {calculate(user_input)}")
