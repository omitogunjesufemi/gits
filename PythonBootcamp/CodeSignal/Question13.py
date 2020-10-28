def reverseInParentheses(inputString):
    if '(' not in inputString:
        return inputString

    depth = 0
    start = -1
    i = 0
    n = len(inputString)
    while i < n:
        if inputString[i] == '(':
            if depth == 0:
                start = i
            depth += 1
        if inputString[i] == ')':
            depth -= 1
            if depth == 0:
                result = reverseInParentheses(inputString[start + 1:i])
                result = result[::-1]
                inputString = f'{inputString[:start]}{result}{inputString[i+1:]}'
                n = len(inputString)
                i = start + len(result) - 1
        i += 1
    return inputString


print(reverseInParentheses("(abc(def))(abc(def))"))
