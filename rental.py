# OOP project
# will probably use classes, methods, and functions
# four square method

# i am very lost.
# break the code down into pieces - start off with the very basics/tackle each part one at a time, don't try to do everything all at once (yet)

# Here we assume that we have a client coming to us asking for an automated Rental Property Calculator. 
# Our client's name is Brandon from a company called "Bigger Pockets". Below, you will find a video of what Brandon usually does to calculate his Rental Property ROI.


# cost of owning the property
        # tax ($150/mon), insurance ($100), utilities ($0) (electric, hydro, garbo, gas, sewer), HOA ($0), lawn/snow care ($0), vacancy ($100), repairs ($100)
        # capital expenditures (saving up for big things like a new roof/water heater/big items) - price will depend on quality (if/else) ($100/mon)
        # property management ($200/mon), and mortgage ($160000 @ 5% int = $860/mon) = total monthly expenses: $1610
        # might need to break these up into different methods or functions

# what return on your cash flow are you getting (how much money you put in and how much you get back)
        # add up all money you put in (down payment ($40000), closing costs ($3000), rehab budget ($7000), misc ($0)) to get total investment ($50000)
        # figure out cashOnCashROI, take annual cash flow (monthly cashflow by 12 = 390 x 12 = 4680) and divide by total investment (4680/50000 = 9.36% (to make a percentage multiply this by 100))

# how to call the classes and methods properly:
# test = ROICalc()
# print(test)

class ROICalc():

    def __init__(self, income=0, expenses=0, cashFlow=0): #anything called in this class is available everywhere else - in this case: income and expenses
        self.inc = income
        self.exp = expenses
        self.cash = cashFlow

    def rentIncome(self):
        self.inc = float(input("enter your monthly rent: "))

    def expenses(self): 

        tax = float(input("Please enter your taxes: "))

        insurance = input("Do you have insurance payments? (Yes/No) ")
        if insurance.lower() == 'yes':
            insurance = float(input("enter your insurance amount: "))
        else:
            insurance = float(0)

        utilities = input("Do you have utility fees to pay? (Yes/No) ")
        if utilities.lower() == 'yes':
            utilities = float(input("enter utilities cost: "))
        else:
            utilities = float(0)

        hoa = input("Do you have hoa fees to pay? (Yes/No) ")
        if hoa.lower() == 'yes':
            hoa = float(input("enter hoa fees: "))
        else:
            hoa = float(0)

        vacancy = input("Do you have vacancy fees to pay? (Yes/No) ")
        if vacancy.lower() == 'yes':
            vacancy = float(input("enter your vacancy fees: "))
        else:
            vacancy = float(0)

        repairs = input("Do you have repair fees to pay? (Yes/No) ")
        if repairs.lower() == 'yes':
            repairs = float(input("enter your repairs fees: "))
        else:
            repairs = float(0)

        capex = input("Do you have capex fees to pay? (Yes/No) ")
        if capex.lower() == 'yes':
            capex = float(input("enter your capex fees: "))
        else:
            capex = float(0)

        propman = input("Do you have property management fees to pay? (Yes/No) ")
        if propman.lower() == 'yes':
            propman = float(input("enter your propman fees: "))
        else:
            propman = float(0)

        mortgage = float(input("enter your mortgage fees: "))

        self.exp = tax + insurance + utilities + hoa + vacancy + repairs + capex + propman + mortgage

    def cashFlow(self):
        self.cash = self.inc - self.exp

    def cashOnCashROI(self):
        downPay = float(input("Enter your down payment: "))
        closeCost = float(input("Enter your closing costs: "))

        rehab = input("Do you have a rehab budget? (yes/no) ")
        if rehab.lower() == 'yes':
            rehab = float(input("Enter your rehab budget: "))
        else:
            rehab = float(0)

        miscExp = input("Do you have any other miscellaneous expenses? (Yes/No) ")
        if miscExp.lower() == 'yes':
            miscExp = float(input("Enter any additional expenses you have: "))
        else:
            miscExp = float(0)

        totalInvest = downPay + closeCost + rehab + miscExp
        ROI = (self.cash*12 / totalInvest) * 100 # completely forgot to multiply self.cash * 12 in the first couple commits
        return ROI

# to run the program
def run():
    property = ROICalc()
    property.rentIncome()
    property.expenses()
    property.cashFlow()
    result = property.cashOnCashROI()
    print(result)
    
run()