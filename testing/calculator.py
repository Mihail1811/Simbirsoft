def calculators(expression):
    allowed = '+-/*'
    if not any(sign in expression for sign in allowed):
        raise ValueError(f'Выражение должно иметь хотя бы 1 знак ({allowed})')
    for sign in allowed:
        if sign in expression:
            try:
                left, right = expression.split(sign)
                left, right = int(left), int(right)
                if sign == '+':
                    return left + right
                elif sign == '-':
                    return left - right
                elif sign == '/':
                    return left / right
                else:
                    return left * right
            except ValueError:
                raise ValueError('Выражение дожно иметь 2 числа и 1 знак')
            
if __name__ == '__main__':
    print('/n')
    print(calculators('87 - 3'))