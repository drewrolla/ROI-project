# OOP project
# will probably use classes, methods, and functions
# four square method

# i am very lost.

# Here we assume that we have a client coming to us asking for an automated Rental Property Calculator. 
# Our client's name is Brandon from a company called "Bigger Pockets". Below, you will find a video of what Brandon usually does to calculate his Rental Property ROI.

class ROICalc():

    def __init__(self, income=0, expenses=0, cashFlow=0): #anything called in this class is available everywhere else - in this case: income and expenses
        self.inc = income
        self.exp = expenses
        self.cash = cashFlow

    def rentIncome(self): # rental income - $2000/mon | total monthly income = $2k/mon
        income = float(input("enter your monthly rent: "))
        self.inc = income
        return self.inc # we want the income to be whatever the inputted income is

    def expenses(self): # cost of owning the property
        # tax ($150/mon), insurance ($100), utilities ($0) (electric, hydro, garbo, gas, sewer), HOA ($0), lawn/snow care ($0), vacancy ($100), repairs ($100)
        # capital expenditures (saving up for big things like a new roof/water heater/big items) - price will depend on quality (if/else) ($100/mon)
        # property management ($200/mon), and mortgage ($160000 @ 5% int = $860/mon) = total monthly expenses: $1610
        # might need to break these up into different methods or functions
        tax = float(input("Please enter your taxes: "))
        insurance = float(input("enter your insurance amount: "))
        utilities = float(input("enter utilities cost: "))
        hoa = float(input("enter hoa fees: "))
        vacancy = float(input("enter your vacancy fees: "))
        repairs = float(input("enter your repairs fees: "))
        capex = float(input("enter your capex fees: "))
        propman = float(input("enter your propman fees: "))
        mortgage = float(input("enter your mortgage fees: "))
        total_exp = tax + insurance + utilities + hoa + vacancy + repairs + capex + propman + mortgage
        self.exp = total_exp
        return self.exp

    def cashFlow(self):
        # income - expenses (2000 - 1610 = 390) total monthly cash flow = 390
        cashFlow = self.inc - self.exp
        self.cash = cashFlow
        return self.cash

    def cashOnCashROI(self):
        # what return on your cash flow are you getting (how much money you put in and how much you get back)
        # add up all money you put in (down payment ($40000), closing costs ($3000), rehab budget ($7000), misc ($0)) to get total investment ($50000)
        # figure out cashOnCashROI, take annual cash flow (monthly cashflow by 12 = 390 x 12 = 4680) and divide by total investment (4680/50000 = 9.36% (to make a percentage multiply this by 100))
        # cash on cash ROI is 9.36%
        downPay = float(input("Enter your down payment: "))
        closeCost = float(input("Enter your closing costs: "))
        rehab = float(input("Enter your rehab budget: "))
        miscExp = float(input("Enter any additional expenses you have: "))
        totalInvest = downPay + closeCost + rehab + miscExp
        ROI = (self.cash / totalInvest) * 100
        return ROI

# how to call the classes and methods properly:
# test = ROICalc()
# print(test)

def run():
    property = ROICalc()
    property.rentIncome()
    property.expenses()
    property.cashFlow()
    result = property.cashOnCashROI()
    print(result)
    
run()