def arithmetic_arranger(problems, *flag):
    if len(problems) > 5:
        return "Error: Too many problems."

    firstLine, secondLine, thirdLine, fourthLine = ("", "", "", "")
    
    for i, problem in enumerate(problems):
        numOne, oprtr, numTwo = problem.split()

        if not numOne.isnumeric() or not numTwo.isnumeric():
            return "Error: Numbers must only contain digits."
        elif len(numOne) > 4 or len(numTwo) > 4:
            return "Error: Numbers cannot be more than four digits."
        elif not oprtr in ("+", "-"):
            return "Error: Operator must be '+' or '-'."

        if oprtr == "+":
            result = int(numOne) + int(numTwo)
        else:
            result = int(numOne) - int(numTwo)

        numberLength = len(max([numOne, numTwo], key=len))

        firstLine += numOne.rjust(numberLength + 2)
        secondLine += oprtr + numTwo.rjust(numberLength + 1)
        thirdLine += "-" * (numberLength + 2)
        fourthLine += str(result).rjust(numberLength + 2)

        if i < len(problems) - 1:
            firstLine += "    "
            secondLine += "    "
            thirdLine += "    "
            fourthLine += "    "

    arranged_problems = firstLine + "\n" + secondLine + "\n" + thirdLine

    if flag:
        arranged_problems += "\n" + fourthLine

    return arranged_problems