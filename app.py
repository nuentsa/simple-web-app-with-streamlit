import streamlit as st

def calculate_compound_interest(principal, monthly_investment, interest_rate, years):
  """
  Calculates the compound interest earned and final investment value.

  Args:
      principal: Initial investment amount.
      monthly_investment: Regular investment amount.
      interest_rate: Annual interest rate (as a decimal).
      years: Target investment period (in years).

  Returns:
      A tuple containing the compound interest earned and final investment value.
  """
  # Convert annual interest rate to monthly rate
  monthly_interest_rate = interest_rate / 12

  # Calculate number of months in investment period
  total_months = years * 12

  # Initialize variables for future calculations
  future_value = principal
  total_interest = 0

  # Iterate through each month and calculate compounding effect
  for _ in range(total_months):
    interest_earned = future_value * monthly_interest_rate
    future_value += (principal + monthly_investment) + interest_earned
    total_interest += interest_earned

  return total_interest, future_value

def main():
  """
  Main function to display the app and call the calculation function.
  """
  # Title and description
  st.title("Compound Interest Calculator")
  st.write("Grow your wealth with the power of compound interest!")

  # Input fields
  principal = st.number_input("Initial Investment ($)", min_value=0.0)
  monthly_investment = st.number_input("Monthly Investment ($)", min_value=0.0)
  interest_rate = st.number_input("Annual Interest Rate (%)", min_value=0.0) / 100  # Convert percentage to decimal
  years = st.number_input("Investment Period (Years)", min_value=0.0)

  # Button to trigger calculation
  if st.button("Calculate"):
    # Calculate compound interest and final investment
    total_interest, future_value = calculate_compound_interest(principal, monthly_investment, interest_rate, years)

    # Display results
    st.write(f"Total Interest Earned: ${total_interest:.2f}")
    st.write(f"Final Investment Value: ${future_value:.2f}")

if __name__ == "__main__":
  main()
