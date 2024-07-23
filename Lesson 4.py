import re
pattern=re.compile(r'hello',re.IGNORECASE)
result=pattern.search('HeLLo world')
print(result.group())

pattern=re.compile(r'hello.world',re.DOTALL)
result=pattern.search('hello\nworld')
print(result.group())

pattern=re.compile(r'hello.world',re.IGNORECASE | re.DOTALL)
result=pattern.search('HeLLO\nworld')
print(result.group())

result=re.search(r'\d+','abc 123 def')
print(result.group())

result=re.match(r'\d+','123 def')
print(result.group())

result=re.match(r'\d+','abc 123 def')
print(result)

pattern = re.compile(r'\d+')  # Raw string notation
result = pattern.search('abc 123 def')
print(result.group())  # Outputs: '123'

pattern = re.compile('\\d+')

pattern = re.compile(r'.')  # Matches any character except newline
pattern = re.compile(r'^hello')  # Matches 'hello' at the start of the string
pattern = re.compile(r'world$')  # Matches 'world' at the end of the string
pattern = re.compile(r'a*')  # Matches 0 or more 'a' characters
pattern = re.compile(r'a+')  # Matches 1 or more 'a' characters
pattern = re.compile(r'a?')  # Matches 0 or 1 'a' character
pattern = re.compile(r'a{2,4}')  # Matches between 2 and 4 'a' characters


import glob

files = glob.glob('*.txt')  # Matches all .txt files in the current directory

pattern = re.compile(r'^\d+$')  # Matches a string composed entirely of digits

pattern = re.compile(r'[aeiou]')  # Matches any vowel
result = pattern.search('hello')
print(result.group())  # Outputs: 'e'

pattern = re.compile(r'[a-z]')  # Matches any lowercase letter

pattern = re.compile(r'(\d+)-(\d+)')
result = pattern.search('123-456')
if result:
    print(result.group(1))  # Outputs: '123'
    print(result.group(2))  # Outputs: '456'



# #Task 1: Extracting All Timestamps
# #Write a Python function to extract all timestamps from the log file.
# import re

# log_data = """
# [2024-07-18 10:23:45] [ERROR] [Authentication] User login failed
# [2024-07-18 10:24:00] [INFO] [Payment] Payment processed successfully
# [2024-07-18 10:25:30] [WARNING] [Database] Connection timeout
# [2024-07-18 10:17:15] [INFO] [Authentication] User login succeeded
# """

# def extract_timestamps(log_data):
#     pattern = re.compile(r'\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\]')
#     return pattern.findall(log_data)

# timestamps = extract_timestamps(log_data)
# print(timestamps)


# #Task 2: Counting Different Log Levels
# #Write a Python function to count the number of occurrences of each log level (ERROR, INFO, WARNING).
# def count_log_levels(log_data):
#     pattern = re.compile(r'\[(ERROR|INFO|WARNING)\]')
#     matches = pattern.findall(log_data)
#     return {level: matches.count(level) for level in set(matches)}

# log_levels_count = count_log_levels(log_data)
# print(log_levels_count)


# #Task 3: Extracting Messages from a Specific Module
# #Write a Python function to extract all log messages from a specific module (e.g., "Authentication").
# def extract_module_messages(log_data, module_name):
#     pattern = re.compile(r'\[.*?\] \[.*?\] \[' + re.escape(module_name) + r'\] (.*)')
#     return pattern.findall(log_data)

# auth_messages = extract_module_messages(log_data, 'Authentication')
# print(auth_messages)


# #Task 4: Identifying and Extracting User Login Failures
# #Write a Python function to identify and extract the timestamps of all user login failures.
# def extract_login_failures(log_data):
#     pattern = re.compile(r'\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\] \[ERROR\] \[Authentication\] User login failed')
#     return pattern.findall(log_data)

# login_failures = extract_login_failures(log_data)
# print(login_failures)


# #Task 5: Extracting and Grouping Data
# #Write a Python function to extract all log data and group it by date.
# def group_logs_by_date(log_data):
#     pattern = re.compile(r'\[(\d{4}-\d{2}-\d{2}) \d{2}:\d{2}:\d{2}\] \[(ERROR|INFO|WARNING)\] \[(.*?)\] (.*)')
#     matches = pattern.findall(log_data)
#     logs_by_date = {}
#     for date, log_level, module, message in matches:
#         if date not in logs_by_date:
#             logs_by_date[date] = []
#         logs_by_date[date].append({'log_level': log_level, 'module': module, 'message': message})
#     return logs_by_date

# logs_grouped_by_date = group_logs_by_date(log_data)
# print(logs_grouped_by_date)


# data_usage_patterns = [
#     r'\b(?:how much|what is) (?:my|the) data usage\b',
#     r'\bcheck data usage\b'
# ]

# bill_payment_patterns = [
#     r'\bpay (?:my )?bill\b',
#     r'\bbill payment\b'
# ]

# troubleshooting_patterns = [
#     r'\bmy (?:internet|connection) (?:is not working|is down|is slow)\b',
#     r'\b(?:fix|troubleshoot) (?:my )?(?:internet|connection)\b'
# ]


# account_number_pattern = r'\b\d{8,12}\b'

# date_pattern = r'\b(?:\d{2}/\d{2}/\d{4}|\d{2}/\d{2}/\d{4})\b'

# amount_pattern = r'\b[$₹]?\d+\.\d+?\b'

# import re

# def classify_query(query):
#     data_usage_patterns = [
#         r'\b(?:how much|what is) (?:my|the) data usage\b',
#         r'\bcheck data usage\b'
#     ]
    
#     bill_payment_patterns = [
#         r'\bpay (?:my )?bill\b',
#         r'\bbill payment\b'
#     ]
    
#     troubleshooting_patterns = [
#         r'\bmy (?:internet|connection) (?:is not working|is down|is slow)\b',
#         r'\b(?:fix|troubleshoot) (?:my )?(?:internet|connection)\b'
#     ]
    
#     if any(re.search(pattern, query, re.IGNORECASE) for pattern in data_usage_patterns):
#         return "data usage"
#     elif any(re.search(pattern, query, re.IGNORECASE) for pattern in bill_payment_patterns):
#         return "bill payment"
#     elif any(re.search(pattern, query, re.IGNORECASE) for pattern in troubleshooting_patterns):
#         return "troubleshooting"
#     else:
#         return "unknown"

# def extract_info(query):
#     account_number_pattern = r'\b\d{8,12}\b'
#     date_pattern = r'\b(?:\d{2}/\d{2}/\d{4}|\d{2}/\d{2}/\d{4})\b'
#     amount_pattern = r'\b(?:[$₹€£]|(?:USD|INR|EUR|GBP)\s?)?\s?\d+(?:,\d{3})*(?:\.\d{1,2})?\b'
    
#     account_numbers = re.findall(account_number_pattern, query)
#     dates = re.findall(date_pattern, query)
#     amounts = re.findall(amount_pattern, query)
  
#     info = {
#         "account_numbers": account_numbers,
#         "dates": dates,
#         "amounts": amounts
#     }
#     arr=[]
#     for i in info['amounts']:
#         for j in query:
#             if query[query.index(i)-1]=='$':
#                 arr.append(i)
    
#     print(set(arr))
#     return [info['account_numbers'],info['dates']]


# query = "My internet is not working and I want to pay my bill."
# print(classify_query(query))  # Output: bill payment

# info = extract_info(query)
# print(info)

# query2 = "Pay my bill with account number 12345678 and $50."
# print(classify_query(query2))  # Output: bill payment

# info2 = extract_info(query2)
# print(info2)

# query2 = "Pay my bill with account number 12345678 and dollar 50.00 on 02/05/2024."
# print(classify_query(query2))  # Output: bill payment

# info2 = extract_info(query2)
# print(info2)

import math
from typing import List, Tuple

# Function to calculate Euclidean distance
def euclidean_distance(loc1: Tuple[float, float], loc2: Tuple[float, float]) -> float:
    return math.sqrt((loc1[0] - loc2[0])**2 + (loc1[1] - loc2[1])**2)

# Function to assign deliveries to trucks
def assign_deliveries(deliveries: List[Tuple[int, Tuple[float, float]]], 
                      trucks: List[Tuple[int, Tuple[float, float]]]) -> List[List[int]]:
    # deliveries: List of tuples (size, (x, y))
    # trucks: List of tuples (capacity, (x, y))
    assignments = [[] for _ in trucks]
    truck_remaining_capacities = [truck[0] for truck in trucks]
    
    for delivery_index, (size, dest) in enumerate(deliveries):
        best_truck_index = None
        best_distance = float('inf')
        
        for truck_index, ((capacity, loc)) in enumerate(trucks):
            if truck_remaining_capacities[truck_index] >= size:
                distance = euclidean_distance(loc, dest)
                if distance < best_distance:
                    best_distance = distance
                    best_truck_index = truck_index
        
        if best_truck_index is not None:
            assignments[best_truck_index].append(delivery_index)
            truck_remaining_capacities[best_truck_index] -= size
            trucks[best_truck_index] = (trucks[best_truck_index][0], dest)
    
    return assignments

# Truck class to track location, mileage, and fuel efficiency
class Truck:
    def __init__(self, capacity: int, location: Tuple[float, float], fuel_efficiency: float):
        self.capacity = capacity
        self.location = location
        self.fuel_efficiency = fuel_efficiency
        self.total_mileage = 0.0
        self.last_maintenance_mileage = 0.0
    
    def update_location(self, new_location: Tuple[float, float]):
        distance = euclidean_distance(self.location, new_location)
        self.location = new_location
        self.add_mileage(distance)
    
    def add_mileage(self, distance: float):
        self.total_mileage += distance
    
    def calculate_fuel_consumption(self, distance: float) -> float:
        return distance / self.fuel_efficiency
    
    def needs_maintenance(self) -> bool:
        return (self.total_mileage - self.last_maintenance_mileage) > 10000
    
    def perform_maintenance(self):
        self.last_maintenance_mileage = self.total_mileage

# Function to get maintenance recommendations
def maintenance_recommendations(trucks: List[Truck]) -> List[Truck]:
    return [truck for truck in trucks if truck.needs_maintenance()]

# Example usage

# Define some example deliveries and trucks
deliveries = [(5, (10, 10)), (3, (20, 20)), (7, (30, 30))]
trucks = [(10, (0, 0)), (15, (5, 5))]

# Assign deliveries to trucks
assignments = assign_deliveries(deliveries, trucks)
print("Assignments:", assignments)

# Create some Truck objects
truck1 = Truck(capacity=10, location=(0, 0), fuel_efficiency=15)
truck2 = Truck(capacity=15, location=(5, 5), fuel_efficiency=12)

# Update truck locations and mileage
truck1.update_location((10, 10))
truck2.update_location((20, 20))

# Check for maintenance needs
trucks = [truck1, truck2]
maintenance_needed = maintenance_recommendations(trucks)
print("Trucks needing maintenance:", maintenance_needed)
