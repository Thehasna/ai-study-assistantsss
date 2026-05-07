
def calculate(expression):

    try:
        result = eval(expression)
        return f"Result: {result}"

    except Exception:
        return "Invalid calculation."
