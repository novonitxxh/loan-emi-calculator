"""
Loan EMI (Equated Monthly Installment) Calculator
---------------------------------------------------
Formula:
            P * R * (1 + R)^N
    EMI = ----------------------
            (1 + R)^N - 1

Where:
    P = Principal loan amount
    R = Interest rate PER MONTH (as a decimal, e.g. annual 12% -> 0.01 monthly)
    N = Number of months (loan tenure)
"""


def calculate_emi(principal: float, annual_rate: float, tenure_months: int) -> dict:
    """
    Calculate the EMI for a loan.

    Args:
        principal: Loan amount (P)
        annual_rate: Annual interest rate in percent (e.g. 10 for 10%)
        tenure_months: Loan tenure in months (N)

    Returns:
        A dictionary with emi, total_payment, and total_interest.
    """
    if principal <= 0:
        raise ValueError("Principal must be greater than zero.")
    if tenure_months <= 0:
        raise ValueError("Tenure must be greater than zero.")
    if annual_rate < 0:
        raise ValueError("Interest rate cannot be negative.")

    # Convert annual rate (%) to monthly rate (decimal)
    monthly_rate = (annual_rate / 12) / 100

    # Special case: 0% interest loan -> EMI is simply principal / months
    if monthly_rate == 0:
        emi = principal / tenure_months
    else:
        factor = (1 + monthly_rate) ** tenure_months
        emi = (principal * monthly_rate * factor) / (factor - 1)

    total_payment = emi * tenure_months
    total_interest = total_payment - principal

    return {
        "emi": emi,
        "total_payment": total_payment,
        "total_interest": total_interest,
        "monthly_rate": monthly_rate,
    }


def format_currency(amount: float) -> str:
    """Format a number as currency with thousands separators."""
    return f"{amount:,.2f}"


def print_result(principal, annual_rate, tenure_months, result):
    """Pretty-print the EMI calculation result."""
    print("\n" + "=" * 50)
    print("           LOAN EMI CALCULATION SUMMARY")
    print("=" * 50)
    print(f"{'Principal Amount (P)':<25}: {format_currency(principal)}")
    print(f"{'Annual Interest Rate':<25}: {annual_rate:.2f}%")
    print(f"{'Monthly Interest Rate':<25}: {result['monthly_rate']*100:.4f}%")
    print(f"{'Loan Tenure':<25}: {tenure_months} months "
          f"({tenure_months / 12:.1f} years)")
    print("-" * 50)
    print(f"{'Monthly EMI':<25}: {format_currency(result['emi'])}")
    print(f"{'Total Payment':<25}: {format_currency(result['total_payment'])}")
    print(f"{'Total Interest Payable':<25}: {format_currency(result['total_interest'])}")
    print("=" * 50)


def get_float_input(prompt: str) -> float:
    """Repeatedly prompt the user until a valid positive float is entered."""
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("  ⚠ Invalid input. Please enter a numeric value.")


def get_int_input(prompt: str) -> int:
    """Repeatedly prompt the user until a valid positive integer is entered."""
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("  ⚠ Invalid input. Please enter a whole number.")


def run_interactive():
    """Main interactive loop for the EMI calculator."""
    print("\n***** LOAN EMI CALCULATOR *****")

    while True:
        print("\nEnter loan details below:")
        principal = get_float_input("  Principal amount (P): ")
        annual_rate = get_float_input("  Annual interest rate (in %, e.g. 10.5): ")
        tenure_months = get_int_input("  Loan tenure (in months): ")

        try:
            result = calculate_emi(principal, annual_rate, tenure_months)
            print_result(principal, annual_rate, tenure_months, result)
        except ValueError as e:
            print(f"\n  ⚠ Error: {e}")
            continue

        again = input("\nCalculate another EMI? (y/n): ").strip().lower()
        if again != "y":
            print("\nThank you for using the Loan EMI Calculator. Goodbye!\n")
            break


if __name__ == "__main__":
    run_interactive()
