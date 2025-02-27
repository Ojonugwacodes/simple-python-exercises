# Simple program that calculates the amount to be paid using a hourly basis
def compute_pay(hours,rate):
  try:
    hours = float(hours)
    rate = float(rate)
    if hours > 40:
      overtime_hours = hours - 40
      overtime_pay = rate * 1.5
      pay = (overtime_hours) * (overtime_pay)  + 40 * rate
    else:
      pay = hours * rate
    return pay
  except(ValueError, TypeError):
    return'Error'
hours = input("Enter hours:")
rate = input("Enter rate:")
result = compute_pay(hours,rate)
print("Pay", result)
