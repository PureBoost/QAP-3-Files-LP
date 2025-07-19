#Description: Program to track vehicle sales.
#Author: Lucas
#Date: 07/16/2025 - 07/17/2025


#Define Libraries
import datetime
import FormatValues as FV

#Define Constants
CURRENT_DATE = datetime.date.today()

#Define Functions
TAX_RATE = 0.15
LUX_TAX_RATE = 0.016
TRANS_FEE_RATE = 0.01
FINANCE_FEE_RATE = 39.99

#Main Program
while True:
    while True:
        CustFirst = input("Enter your first name (or type 'end' to quit): ").title()
        if CustFirst.lower() == "end":
            print("Exiting the program...")
            exit()
        if not CustFirst.isalpha():
            print("First name cannot be a number. Please try again.")
        else:
            FirstIntial = (CustFirst[0]).upper()
            break

    while True:
        CustLast = input("Enter your last name: ").title()
        if not CustLast.isalpha():
            print("Last name cannot be a number. Please try again.")
        else:
            break

    while True:
        Phone = input("Enter your phone number: ") #must be 10 digits
        if not (Phone.isdigit() and len(Phone) == 10):
            print("Invalid phone number. Please enter a 10-digit phone number.")
        else:
            break

    while True:
        Plate = input("Enter the license plate number: ").upper() #must be 6 characters "AAA111"
        if not (len(Plate) == 6 and Plate[:3].isalpha() and Plate[3:].isdigit()):
            print("Invalid license plate number. Please enter a valid plate number (e.g., AAA111).")
        else:
            break

    while True:
        VehMake = input("Enter the vehicle make: ").title()
        if not VehMake.isalpha():
            print("Invalid vehicle make. Please enter a valid make.")
        else:
            break

    while True:
        VehModel = input("Enter the vehicle model: ").title()
        if not VehModel.isalpha():
            print("Invalid vehicle model. Please enter a valid model.")
        else:
            break

    while True:
        VehYear = input("Enter the vehicle year: ") #must be 4 digits
        if not (VehYear.isdigit() and len(VehYear) == 4):
            print("Invalid vehicle year. Please enter a 4-digit year.")
        else:
            break

    while True:
        SalePrice = input("Enter the vehicle price: ") #cant be over 50k
        if not (SalePrice.isdigit() and int(SalePrice) <= 50000):
            print("Invalid vehicle price. Please enter a price under $50,000.")
        else:
            break
    while True:
        TradeIn = input("Enter the trade-in value: ") #cant be more than SalePrice
        if not (TradeIn.isdigit() and int(TradeIn) <= int(SalePrice)):
            print("Invalid trade-in value. Please enter a value less than or equal to the sale price.")
        else:
            break
    while True:
        SalesFirst = input("Enter the salesperson's first name: ").title()
        if not SalesFirst.isalpha():
            print("Invalid first name. Please enter a valid name.")
        else:
            break
    while True:
        SalesLast = input("Enter the salesperson's last name: ").title()
        if not SalesLast.isalpha():
            print("Invalid last name. Please enter a valid name.")
        else:
            break



    #Preforming calculations.
    SalePrice = float(SalePrice)
    TradeIn = float(TradeIn)

    if SalePrice > 15000:
        LicenceFee = 165
    else:
        LicenceFee = 75

    if SalePrice > 20000:
        TransferFee = SalePrice * TRANS_FEE_RATE
    else:
        TransferFee = 0

    LuxTax = SalePrice * LUX_TAX_RATE
    TransferFee = TransferFee + LuxTax

    AfterTradePrice = SalePrice - TradeIn
    Subtotal = AfterTradePrice + LicenceFee + TransferFee
    Tax = Subtotal * TAX_RATE
    TotalPrice = Subtotal + Tax
    TotalBase = Subtotal + Tax

    today = CURRENT_DATE
    if today.day >= 25:
        Month = today.month + 2
    else:
        Month = today.month + 1
    Year = today.year
    if Month > 12:
        Month -= 12
        Year += 1
    FirstPayment = datetime.date(Year, Month, 1)



    #Formatting values.
    ReciptID = "{}-{}-{}".format(FV.FInitials(CustFirst, CustLast), Plate[-3:], Phone[-4:])
    SalePrice = FV.FDollar2(SalePrice)
    TradeIn = FV.FDollar2(TradeIn)
    AfterTradePrice = FV.FDollar2(AfterTradePrice)
    LicenceFee = FV.FDollar2(LicenceFee)
    if len(LicenceFee) == 4:
        LicenceFee = " " + LicenceFee
    TransferFee = FV.FDollar2(TransferFee)
    Subtotal = FV.FDollar2(Subtotal)
    Tax = FV.FDollar2(Tax)
    TotalPrice = FV.FDollar2(TotalPrice)
    Phone = FV.PhoneFull(Phone)


    #Displaying results.
    print("         1         2         3         4         5         6         7         8")
    print("12345678901234567890123456789012345678901234567890123456789012345678901234567890")
    print("")
    print(f"Honest Harry Car Sales                                Invoice Date: {CURRENT_DATE.strftime('%B-%d-%Y')}")
    print(f"Used Car Sale and Receipt                             Receipt ID:    {ReciptID}")
    print("")
    print(f"                                                  Sale Price:         {SalePrice:>10}")
    print(f"Sold To:                                          Trade Allowance:    {TradeIn:>10}")
    print("                                                  ------------------------------")
    print(f"     {FirstIntial}. {CustLast:>10}                                Price After Trade:  {AfterTradePrice:>10}")
    print(f"     {Phone:>12}                               Licence Fee:        {LicenceFee:>10}")
    print(f"                                                  Transfer Fee:       {TransferFee:>10}")
    print("                                                  ------------------------------")
    print(f"Car Details:                                      Subtotal:           {Subtotal:>10}")
    print(f"     {VehYear} {VehMake:>8} {VehModel:>8} {Plate}                HST:                {Tax:>10}")
    print("                                                  ------------------------------")
    print(f"                                                  Total sales price:  {TotalPrice:>10}")
    print("")
    print("--------------------------------------------------------------------------------")
    print("")
    print("                                 Financing        Total        Monthly")
    print("        #Years     #Payments        Fee           Price        Payment")
    print("        ----------------------------------------------------------------")
    for years in range(1, 5):
        NumPayments = years * 12
        FinanceFee = FINANCE_FEE_RATE * years
        TotalYearly = TotalBase + FinanceFee
        MonthlyPayment = TotalYearly / NumPayments
        print(f"           {years:<7}    {NumPayments:<12}{FV.FDollar2(FinanceFee):<12}   {FV.FDollar2(TotalYearly):<13} {FV.FDollar2(MonthlyPayment):<10}")
    print("        ----------------------------------------------------------------")
    print("        First payment date: ", FirstPayment.strftime('%d-%m-%Y'))
    print("--------------------------------------------------------------------------------")
    print("                     Best used cars at the best prices!")
    print("")