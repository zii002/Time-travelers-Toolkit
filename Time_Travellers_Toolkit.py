import datetime as dt
import random
from decimal import Decimal
from random import randint
from random import choice
import custom_module
today_date=dt.date.today()
#print(today_date)
current_time=dt.datetime.today()
#print(current_time)
all_today= dt.datetime.now().time()
print(all_today)
base_cost = Decimal('1000.00')
current_year= current_time.year
random_year = randint(1800,2500)
year_difference=abs(current_year-random_year)
cost_multiplier= Decimal('0.05')
final_cost= base_cost + (Decimal(year_difference)*cost_multiplier)
#print(final_cost)
final_cost=round(final_cost,2)
possible_destinations=["Amsterdam","Rome","Washington",
"Paris","London"]
selected_random_destination= random.choice(possible_destinations)
message = custom_module.generate_time_travel_message(random_year,selected_random_destination,final_cost)
print(message)




