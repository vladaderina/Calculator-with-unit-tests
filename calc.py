import re
def calc(expression):
    reg = "[+\-*/]"
    if not re.search(reg, expression):
        raise ValueError("Выражение должно содержать оператор")
    sign = re.findall(reg, expression)[0]
    try:
        first, second = expression.split(sign)
        first, second = int(first), int(second)
        if sign == "+":
            return first + second
        elif sign == "-":
            return first - second
        elif sign == "*":
            return first * second
        elif sign == "/":
            return first / second
    except (ValueError, TypeError):
        raise ValueError("Выражение должно содержать только 2 целых числа и 1 знак")

if __name__ == '__main__':
    print(calc("2+4"))