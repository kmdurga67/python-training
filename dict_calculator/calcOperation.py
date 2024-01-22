from operations import add, subtract, multiply, divide

operationDict = {
    'add': add,
    'sub': subtract,
    'mult': multiply,
    'div': divide
}


def perform_operation(num1, operator, num2):
    if operationDict.get(operator):
        operationFunction = operationDict[operator]
        return operationFunction(num1, num2)
    else:
        return "Invalid operator. Please use add, sub, mult, div"
