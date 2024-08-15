import csv
from datetime import datetime, timedelta
import random

def generate_dummy_data(min_rows_today=100, rows_per_day_before=1000, days_back=20):
    data = [['date_added', 'name', 'value']]
    base_date = datetime.now()
    
    # Generate rows for each day
    for i in range(days_back + 1):
        # Determine the date for this iteration
        date_added = (base_date - timedelta(days=i, seconds=random.randint(0, 86400))).strftime('%Y-%m-%d %H:%M:%S')
        
        # Set the number of rows based on the day
        if i == 0:
            rows_per_day = min_rows_today
        else:
            rows_per_day = rows_per_day_before
        
        for j in range(rows_per_day):
            name = f'Item-{i+1}-{j+1}'
            value = random.randint(1, 100)
            data.append([date_added, name, value])
    
    return data
    
filename = './transform/data/test_data.csv'

data = generate_dummy_data(min_rows_today=100, rows_per_day_before=1000, days_back=20)

with open(filename, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    
    csvwriter.writerows(data)
    
print(f"CSV file '{filename}' generated successfully.")