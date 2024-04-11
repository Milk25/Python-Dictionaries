weekly_sales = {
    "Week 1": {"Electronics": 12000, "Clothing": 5000, "Groceries": 7000},
    "Week 2": {"Electronics": 15000, "Clothing": 6000, "Groceries": 8000}
}

import copy

copied_weekly_sales2 = copy.deepcopy(weekly_sales)
print(copied_weekly_sales2)




copied_weekly_sales2['Week 2']['Electronics'] = 18000


print(copied_weekly_sales2)

