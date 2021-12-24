import math
import sys

mode = None
principal = None
annuity_payment = None
periods = None
loan_interest = None

try:
    for i in sys.argv:
        if "--type=" in i:
            mode = i.replace("--type=", "")
        elif "--payment" in i:
            annuity_payment = float(i.replace("--payment=", ""))
        elif "--principal" in i:
            principal = float(i.replace("--principal=", ""))
        elif "--periods" in i:
            periods = int(i.replace("--periods=", ""))
        elif "--interest" in i:
            loan_interest = float(i.replace("--interest=", "")) / (12 * 100)
except ValueError:
    print("Incorrect parameters")

if len(sys.argv) < 5 or \
    mode != "annuity" and mode != "diff" or \
    annuity_payment is not None and annuity_payment < 0 or \
    principal is not None and principal < 0 or \
    periods is not None and periods < 0 or \
    loan_interest is not None and loan_interest < 0:
        print("Incorrect parameters")

else:
    if mode == "diff":
        total_payment = 0
        for m in range(1, periods + 1):
            payment = (principal / periods) \
                      + (loan_interest * (principal - (principal * (m - 1)) / periods))
            payment = math.ceil(payment)
            total_payment += payment
            print(f"Month {m}: payment is {payment}")
        overpayment = math.ceil(total_payment - principal)
        print(f"\nOverpayment = {overpayment}")

    else:
        if principal is None:
            dividend = loan_interest * math.pow(1 + loan_interest, periods)
            divisor = math.pow(1 + loan_interest, periods) - 1
            principal = math.ceil(annuity_payment / (dividend / divisor))
            print(f"Your loan principal = {principal}!")
            overpayment = math.ceil(annuity_payment * periods - principal)
            print(f"\nOverpayment = {overpayment}")

        elif periods is None:
            x = annuity_payment / (annuity_payment - loan_interest * principal)
            n = math.log(x, (1 + loan_interest))
            months = math.ceil(n)
            periods = months
            years = months // 12
            months = months % 12
            if not months:
                if years != 1:
                    print(f"It will take {years} years to repay this loan!")
                else:
                    print(f"It will take {years} year to repay this loan!")
            elif not years:
                if months != 1:
                    print(f"It will take {months} months to repay this loan!")
                else:
                    print(f"It will take {months} month to repay this loan!")
            else:
                print(f"It will take {years} years and {months} months")
            overpayment = math.ceil(annuity_payment * periods - principal)
            print(f"Overpayment = {overpayment}")

        else:
            dividend = loan_interest * math.pow(1 + loan_interest, periods)
            divisor = math.pow(1 + loan_interest, periods) - 1
            annuity_payment = math.ceil(principal * (dividend / divisor))
            print(f"Your annuity payment = {annuity_payment}!")
            overpayment = math.ceil(annuity_payment * periods - principal)
            print(f"\nOverpayment = {overpayment}")
