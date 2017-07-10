cost_per_hour=0.51
cost_per_day=24*cost_per_hour
print('COST PER DAY IS:')
print(cost_per_day)
cost_per_month=30*cost_per_day
print('COST PER MONTH IS:')
print(cost_per_month)

cost_per_day_twenty=20*cost_per_day
cost_per_month_twenty=20*cost_per_month

budget=918
operational_days=budget/cost_per_day

print('cost to operate one server per day is ${:.2f}.'.format(cost_per_day))
print('cost to operate one server per month is ${:.2f}.'.format(cost_per_month))

print('cost to operate twenty servers per day is ${:.2f}.'.format(cost_per_day_twenty))
print('cost to operate twenty servers per month is ${:.2f}.'.format(cost_per_month_twenty))
print('A Server can operate on a ${0:.2f} budget for {1:.0f} days.'.format(budget, operational_days))
