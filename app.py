import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import datetime

def calculate_compound_interest(principal, monthly_investment, interest_rate, years):
  """
  Calculates the compound interest earned and final investment value for each year.

  Args:
      principal: Initial investment amount.
      monthly_investment: Regular investment amount.
      interest_rate: Annual interest rate (as a decimal).
      years: Target investment period (in years).

  Returns:
      A list of dictionaries containing investment details for each year.
  """

  # Initialize variables for calculations
  investment_data = []  # List to store data for each year
  current_balance = principal
  cumulated_investment = principal
  yearly_investment = monthly_investment*12

  # Get the current year
  today = datetime.date.today()
  current_year = today.year

  for year in range(1, years + 1):
    interest_earned = current_balance * interest_rate
    cumulated_investment += yearly_investment
    current_balance += (principal + yearly_investment) + interest_earned

    # Append data for each month (consider changing to yearly if needed)
    investment_data.append({
        "Year": current_year + year,
        "Cumulated Investment": cumulated_investment,
        "Interest Earned": interest_earned,
        "Total Balance": current_balance
    })

  return investment_data

def main():
  """
  Main function to display the app and call the calculation function.
  """
  # Title and description
  st.title("Compound Interest Calculator")
  st.write("Grow your wealth with the power of compound interest!")

  # Input fields
  principal = st.number_input("Initial Investment ($)", min_value=0.0)
  monthly_investment = st.number_input("Monthly Investment ($)", min_value=150.0)
  interest_rate = st.number_input("Annual Interest Rate (%)", min_value=4.0) / 100  # Convert percentage to decimal
  years = st.number_input("Investment Period (Years)", min_value=15)

  # Button to trigger calculation
  if st.button("Calculate"):
    # Calculate investment data for each year
    investment_data = calculate_compound_interest(principal, monthly_investment, interest_rate, years)

    # Convert to dataframe for further manipulation
    investment_df = pd.DataFrame(investment_data)
    
    # Visualize the results
    st.line_chart(data=investment_df, x="Year", y=["Cumulated Investment", "Total Balance"])
    st.write(investment_df)


if __name__ == "__main__":
  main()
