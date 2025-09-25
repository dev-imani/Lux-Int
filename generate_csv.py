import csv
import random
from datetime import datetime, timedelta

def generate_csv_data():
    """Generate sample CSV data for demonstration"""
    
    # Sample data arrays
    first_names = ['John', 'Jane', 'Mike', 'Sarah', 'David', 'Emily', 'Chris', 'Lisa', 'Tom', 'Anna']
    last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Martinez']
    departments = ['Engineering', 'Marketing', 'Sales', 'HR', 'Finance', 'Operations']
    cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia']
    
    # Generate data
    data = []
    for i in range(100):  # Generate 100 rows
        # Generate random date within last year
        start_date = datetime.now() - timedelta(days=365)
        random_days = random.randint(0, 365)
        hire_date = start_date + timedelta(days=random_days)
        
        row = {
            'ID': i + 1,
            'First Name': random.choice(first_names),
            'Last Name': random.choice(last_names),
            'Email': f"{random.choice(first_names).lower()}.{random.choice(last_names).lower()}@company.com",
            'Department': random.choice(departments),
            'Salary': random.randint(40000, 120000),
            'Hire Date': hire_date.strftime('%Y-%m-%d'),
            'City': random.choice(cities),
            'Age': random.randint(22, 65),
            'Active': random.choice([True, False])
        }
        data.append(row)
    
    return data

def save_to_csv(data, filename):
    """Save data to CSV file"""
    if not data:
        print("No data to save")
        return
    
    fieldnames = data[0].keys()
    
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    
    print(f"CSV file '{filename}' has been generated successfully!")
    print(f"Generated {len(data)} rows of data")

if __name__ == "__main__":
    # Generate sample data
    csv_data = generate_csv_data()
    
    # Save to jeff.csv
    save_to_csv(csv_data, 'jeff.csv')
    
    # Also create a backup with timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_filename = f'generated_data_{timestamp}.csv'
    save_to_csv(csv_data, backup_filename)
    
    print(f"\nFiles created:")
    print(f"- jeff.csv (overwrites existing)")
    print(f"- {backup_filename} (backup with timestamp)")