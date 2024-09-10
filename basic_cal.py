def calculate(a: int, b:int, op: str) -> int:
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b
    elif op == '//':
        return a // b
    else:
        print(f"Operator {op} is not supported")
        return None
    
if __name__ == '__main__':
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    op = input("Enter operand: ")
    results = calculate(a=a, b=b, op=op)
    print(f"{a} {op} {b} = {results}")
        