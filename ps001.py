# annualSalary = int(input("annual salary = "))
# portionSaved = float(input("save percentage = "))
# semiRaise = float(input("raise in % = "))
# totalCost = int(input("cost of house = "))
#
def getMonths(annualSalary, portionSaved, totalCost, semiRaise, intRate=0.04):
    salary = annualSalary
    downpayment = totalCost * 0.25
    monthlyInt = annualSalary / 12 * portionSaved
    totalSavings = 0
    numberOfMonths = 0
    for month in range(36):
        numberOfMonths += 1
        totalSavings = totalSavings + totalSavings * intRate / 12 + monthlyInt
        if numberOfMonths % 6 == 0:
            salary = salary + salary * semiRaise
            monthlyInt = salary / 12 * portionSaved
    return totalSavings
#
# numberOfMonths = getMonths(annualSalary, portionSaved, totalCost, semiRaise)
#
# print('number of months to save = %d'%(numberOfMonths))

# annualSalary = int(input("annual salary = "))
# portionSaved = float(input("save percentage = "))


# print(getMonths(120000, 50, 1000000, 0.03))

def bestSave(annualSalary, totalCost=1000000, semiRaise=0.07):

    downpayment = totalCost * 0.25
    epsilon = totalCost / 10000
    numGuesses = 0
    low = 0
    high = 10000
    res = 0
    finished = False
    while not finished:
        if getMonths(annualSalary, 1, totalCost, semiRaise) < downpayment:
            print('Can"t get to downpayment in 36 months')
            return
        guess = (low + high) / 2
        res = getMonths(annualSalary, guess/10000, totalCost, semiRaise)
        if res > downpayment:
            high = guess
        else:
            low = guess
        numGuesses += 1
        if res < downpayment and downpayment - res <= epsilon:
            finished = True
    print('best savings rate in %% of yearly salary = %f'%(round(guess/100, 2)))
    print('Steps = %d'%(numGuesses))

annualSalary = int(input("annual salary = "))

bestSave(annualSalary)



    #
    # while downpayment > totalSavings:
    #     numberOfMonths += 1
    #     totalSavings = totalSavings + totalSavings * intRate / 12 + monthlyInt
    #     if numberOfMonths % 6 == 0:
    #         salary = salary + salary * semiRaise
    #         monthlyInt = salary / 12 * portionSaved
    #         print(monthlyInt)
    #     print(totalSavings)
    # return numberOfMonths
