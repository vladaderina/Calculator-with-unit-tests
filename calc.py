import re
def calc(expression):
    reg = "[+\-*/]"
    if not re.search(reg, expression):
        raise ValueError("Выражение должно содержать оператор")
    sign = re.findall(reg, expression)[0]
    try:
        first, second = expression.split(sign)
        first, second = int(first), int(second)
        match sign:
            case '+':
                return first + second
            case '-':
                return first - second
            case '*':
                return first * second
            case '/':
                if second == 0:
                    raise ValueError('На ноль делить нельзя!')
                else:
                    return first / second
    except (ValueError, TypeError):
        raise ValueError("Выражение должно содержать только 2 целых числа и 1 знак")


exeption = input('Введи выражение вида a ? b, на месте ? стоит любой оперэнд\n')
if __name__ == '__main__':
    print(calc(exeption))