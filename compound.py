def compound_interest(t):

    principal, iRate_percent, time, numTimes = t

    iRate_percent /= 100
    inside = 1 + (iRate_percent / numTimes)
    result = principal * (pow(inside, time * numTimes))
    return result



def printResult(case):
    print(f"""
Given the principal amount is {case[0]},
interest rate is {case[1]},
over a period of {case[2]} years,
and repeated {case[3]} times:
          """)
    print(f"The compunded interest is {compound_interest(case)}")



case1 = (6000, 10, 3, 2)
case2 = (2000, 12, 4, 5)
case3 = (8000, 15, 10, 6)

# answer = compound_interest(case1)
# print("{:.2f}".format(answer))

# answer = compound_interest(case2)
# print("{:.2f}".format(answer))

# answer = compound_interest(case3)
# print("{:.2f}".format(answer))

printResult(case1)
printResult(case2)
printResult(case3)