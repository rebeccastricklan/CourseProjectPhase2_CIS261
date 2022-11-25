#Rebecca Stricklan
#Course Project Phase 2 
#CIS261

def GetEmpName():
    empname = input("Enter employee name (END to terminate): ")
    return empname
def GetDatesWorked():
    fromdate = input("Enter Start Date (mm/dd/yyyy:")
    todate = input("Enter End Date (mm/dd/yyyy:")
    return fromdate, todate

def GetHoursWorked():
    hours = float(input('Enter hours worked: '))
    return hours
def GetHourlyRate():
    hourlyrate = float(input('Enter hourly rate: '))
    return hourlyrate
def GetTaxRate():
    taxrate = float(input('Enter tax rate: '))
    return taxrate
def CalcTaxAndNetPay(hours, hourlyrate, taxrate):
    grosspay = hours * hourlyrate
    incometax = grosspay * taxrate
    netpay = grosspay - incometax
    return grosspay, incometax, netpay

def printinfo(EmpDetailList):
    TotEmployees = 0
    TotHours = 0.00
    TotGrossPay = 0.00
    TotTax = 0.00
    TotNetPay = 0.00

    for EmpList in EmpDetailList:
        fromdate = EmpList[0]
        todate = EmpList[1]
        empname = EmpList[2]
        hours = EmpList[3]
        hourlyrate = EmpList[4]
        taxrate = EmpList[5]


        grosspay, incomtax, netpay = CalcTaxAndNetPay(hours, hourlyrate, taxrate)
        print(fromdate, todate, empname, f"{hours:,.2f}", f"{hourlyrate:,.2f}",f"{grosspay:,.2f}", f"{taxrate:,.1%}", f"{incometax:,.2f}", f"{netpay:,.2f}")
        TotEmployees += 1
        TotHours += hours
        TotGrossPay += grosspay
        TotTax += incomtax
        TotNetPay += netpay

        EmpTotals["TotEmp"] = TotEmployees
        HoursTotals["TotHours"] = TotHours
        GrossPayTotals["TotGrossPay"] = TotGrossPay
        TaxTotals["TotTax"] = TotTax
        NetPayTotals["TotNetPay"] = TotNetPay

def PrintTotals(EmpTotals):
    print()
    
    


    print(f'Total Number Of Employees: {EmpTotals["TotEmp"]} ')
    print(f'Total Hours Worked: {EmpTotals["TotHours"]:,.2f} ')
    print(f'Total Gross Pay: {EmpTotals["TotGrossPay"]:,.2f} ')
    print(f'Total Of Tax: {EmpTotals["TotTax"]:,.2f} ')
    print(f'Total Net Pay: {EmpTotals["TotNetPay"]:,.2f} ')

if __name__ == "__main__":

    EmpDetailLis = []
    EmpTotals = {}
    while True:
        empname = GetEmpName()
        if (empname.upper() == "END"):
            break       
        fromdate, todate = GetDatesWorked()
        hours = GetHoursWorked()
        hourlyrate = GetHourlyRate()
        taxrate = GetTaxRate()

    EmpDetail = [fromdate, todate, empname, hours, hourlyrate, taxrate]
    EmpDetailList.append(EmpDetail)
    printinfo(DetailsPrinted)
    PrintTotals (EmpTotals)







        



