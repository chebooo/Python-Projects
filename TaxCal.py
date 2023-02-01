# Tax calculator program

# Taxable income bracket for each filing status
tax_brackets = {
    'Single': [0, 9700, 39475, 84200, 160725, 204100, 510300],
    'Married Filing Jointly': [0, 19400, 78950, 168400, 321450, 408200, 612350],
    'Head of Household': [0, 13850, 52850, 84200, 160700, 204100, 510300],
    'Married Filing Separately': [0, 9700, 39475, 84200, 160725, 204100, 510300]
}

# Tax rate for each bracket
tax_rates = [0.1, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37]

def calculate_tax(income, status):
    """
    Calculate federal income tax based on taxable income and filing status
    """
    # Get the appropriate tax bracket for the filing status
    bracket = tax_brackets[status]

    # Determine the tax bracket the income falls into
    for i in range(len(bracket) - 1):
        if income > bracket[i] and income <= bracket[i + 1]:
            tax_bracket = i
            break
    else:
        tax_bracket = len(bracket) - 1

    # Calculate the tax
    tax = sum([(bracket[i + 1] - bracket[i]) * tax_rates[i] for i in range(tax_bracket)]) + (income - bracket[tax_bracket]) * tax_rates[tax_bracket]

    return tax

# Example usage
income = 214000
status = 'Single'
tax = calculate_tax(income, status)
print(f'Tax for {income} with {status} status: {tax:.2f}')
