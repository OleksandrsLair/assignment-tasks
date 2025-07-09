import operator
import re
from decimal import Decimal

prior_expr_regex = re.compile(
    r"(\d+\D+)?(?P<num1>\d+)(?P<action>[/*])(?P<num2>\d+)(\d+\D+)?"
)
sec_expr_regex = re.compile(
    r"(\d+\D+)?(?P<num1>\d+)(?P<action>[+-])(?P<num2>\d+)(\d+\D+)?"
)
actions = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
}


def calculate(input_expression: str):
    """
    Evaluates a mathematical expression step-by-step prioritizing operations based
    on predefined regular expressions. The provided input expression is processed
    and reduced until it cannot be evaluated further, ultimately returning the
    simplified result as a string.

    :param input_expression: A string containing the mathematical expression to be
        evaluated.
    :return: The simplified mathematical expression or result in string format.
    :rtype: str
    """
    for expr in [prior_expr_regex, sec_expr_regex]:
        match = expr.match(input_expression.replace(" ", ""))
        if match:
            action = actions[match.group("action")]
            result = action(Decimal(match.group("num1")), Decimal(match.group("num2")))
            return calculate(
                f'{match.string[:match.start("num1")]}'
                f"{str(result)}"
                f'{match.string[match.end("num2"):]}'
            )

    return input_expression


examples = [
    "10/5",
    "10+5*2-3",
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
