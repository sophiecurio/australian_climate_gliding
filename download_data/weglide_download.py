import requests
import pandas as pd
from datetime import datetime
import time

columns = ['date', 'name', 'km', 'km/h', 'Points', 'Airfield', 'Club', 'Region of club', 'Aircraft']
df = pd.DataFrame(columns=columns)

parameters = {
    "country_id_in": "AU",
}

base_url = "https://api.weglide.org/v1/flight" 


# Initialize the skip parameter
skip = 0
limit = 100  # Number of records to fetch per request

rows = []

while True:
    # Fetch data from the API with the current skip value
    response = requests.get(f"{base_url}?skip={skip}", params=parameters)
    time.sleep(1)
    
    
    # Check if the response is successful
    if response.status_code != 200:
        print(f"Error fetching data: {response.status_code}")
        break
    
    # Parse the JSON response
    query_results = response.json()
    
    # If there are no more results, break the loop
    if not query_results:
        break
    
    # Process each result
    for result in query_results:
        # Reformat the date
        original_date = result['scoring_date']
        formatted_date = datetime.strptime(original_date, '%Y-%m-%d').strftime('%d/%m/%Y')
        
        # Create a new row as a dictionary
        new_row = {
            'date': formatted_date,
            'name': result['user']['name'],  # Accessing the user's name
            'km': result['contest']['distance'],  # Accessing the contest distance
            'km/h': result['contest']['speed'],  # Accessing the contest speed
            'Points': result['contest']['points'],
            'Airfield': result['takeoff_airport']['name'],  # Accessing the takeoff airport name
            'Club': result.get('club', {}).get('name', 'N/A'),  # Using .get() to avoid KeyError
            'Region of club': result['takeoff_airport'].get('region', 'N/A'),  # Accessing the region
            'Aircraft': result.get('aircraft', {}).get('name', 'N/A')  # Accessing the aircraft name
        }
        
        # Append the new row to the DataFrame
        print(new_row)
        print(len(rows))
        rows.append(new_row)
    
    # Increment the skip parameter for the next batch
    skip += limit

# Display the first few rows of the DataFrame
df = pd.DataFrame(rows)
print(df.head())
df.to_csv("241016weglide_flights.csv")

