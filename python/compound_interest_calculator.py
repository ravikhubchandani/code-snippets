def compound_interest(principal, years, interest_rate, annual_deposit):
    """
    Recursively calculates the compound interest on an initial principal.    
    Parameters:
    - principal: the initial amount
    - years: total number of years to compound
    - interest_rate: annual interest percentage (e.g., 5 for 5%)
    - annual_deposit: additional amount added at the end of each year    
    Returns:
    - The total amount after the given number of years.
    """
    if years == 0:
        return principal
    else:
        return compound_interest(principal, years - 1, interest_rate, annual_deposit) * (1 + interest_rate / 100) + annual_deposit


# Example usage:
if __name__ == '__main__':
    
    initial_amount = 20000
    total_years = 25
    annual_interest = 7
    annual_deposit = 1200
    
    invested_amount = initial_amount + total_years * annual_deposit
    final_amount = compound_interest(initial_amount, total_years, annual_interest, annual_deposit)
    print(f"Invested {invested_amount:.2f} have been converted to {final_amount:.2f}. Profit: {final_amount - invested_amount:.2f}. Gain of {100 * (final_amount / invested_amount - 1):.2f}%")
