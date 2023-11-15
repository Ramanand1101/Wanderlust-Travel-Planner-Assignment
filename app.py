from flask import Flask, request, jsonify
import psycopg2
import requests
import os
from dotenv import load_dotenv

app = Flask(__name__)

# Load environment variables from the .env file
load_dotenv()

# Database connection setup
DATABASE_URL = os.environ.get("DATABASE_URL")
conn = psycopg2.connect(DATABASE_URL)

# Create tables
with conn.cursor() as cursor:
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS destinations (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            description TEXT,
            location VARCHAR(100)
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS itineraries (
            id SERIAL PRIMARY KEY,
            destination_id INTEGER,
            activity TEXT,
            FOREIGN KEY (destination_id) REFERENCES destinations (id)
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id SERIAL PRIMARY KEY,
            destination_id INTEGER,
            description TEXT,
            amount DECIMAL,
            FOREIGN KEY (destination_id) REFERENCES destinations (id)
        )
    ''')
    conn.commit()


# Routes
@app.route('/')
def welcome():
    return jsonify(message='Welcome to the Wanderlust Travel Planner API!')


# Define the route to get weather data
@app.route('/weather', methods=['GET'])
def get_weather():
    location = request.args.get('location')  # Get the location from the request

    # Replace 'YOUR_OPENWEATHERMAP_API_KEY' with your actual API key
    api_key = '2d3e100db5399dd8864b892220c55e32'

    # Define the OpenWeatherMap API URL with the location and API key
    weather_url = f'https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'

    try:
        # Make the API request to get weather data
        response = requests.get(weather_url)
        data = response.json()

        # Check if the request was successful
        if response.status_code == 200:
            # Extract relevant weather information from the response
            weather_data = {
                'location': location,
                'temperature': data['main']['temp'],
                'condition': data['weather'][0]['description'],
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed']
            }

            return jsonify(weather_data), 200
        else:
            return jsonify({'error': 'Weather data not found'}), 404

    except Exception as e:
        return jsonify({'error': 'An error occurred while fetching weather data'}), 500


# Destination Routes 
@app.route('/destinations', methods=['POST'])
def create_destination():
    data = request.get_json()
    name = data['name']
    description = data['description']
    location = data['location']

    with conn.cursor() as cursor:
        cursor.execute("INSERT INTO destinations (name, description, location) VALUES (%s, %s, %s)", (name, description, location))
        conn.commit()

    return jsonify(message='Destination created successfully'), 201

@app.route('/destinations', methods=['GET'])
def get_destinations():
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM destinations")
        destinations = cursor.fetchall()

    return jsonify(destinations), 200

@app.route('/destinations/<int:destination_id>', methods=['GET'])
def get_destination(destination_id):
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM destinations WHERE id = %s", (destination_id,))
        destination = cursor.fetchone()

    if destination is not None:
        return jsonify(destination), 200
    else:
        return jsonify(message='Destination not found'), 404

@app.route('/destinations/<int:destination_id>', methods=['PUT'])
def update_destination(destination_id):
    data = request.get_json()
    name = data['name']
    description = data['description']
    location = data['location']

    with conn.cursor() as cursor:
        cursor.execute("UPDATE destinations SET name = %s, description = %s, location = %s WHERE id = %s",
                       (name, description, location, destination_id))
        conn.commit()

    return jsonify(message='Destination updated successfully'), 200

@app.route('/destinations/<int:destination_id>', methods=['DELETE'])
def delete_destination(destination_id):
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM destinations WHERE id = %s", (destination_id,))
        conn.commit()

    return jsonify(message='Destination deleted successfully'), 200


# Itinerary Routes
@app.route('/itineraries', methods=['POST'])
def create_itinerary():
    data = request.get_json()
    destination_id = data['destination_id']
    activity = data['activity']

    with conn.cursor() as cursor:
        cursor.execute("INSERT INTO itineraries (destination_id, activity) VALUES (%s, %s)", (destination_id, activity))
        conn.commit()

    return jsonify(message='Activity added to itinerary'), 201

@app.route('/itineraries', methods=['GET'])
def get_itineraries():
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM itineraries")
        itineraries = cursor.fetchall()

    return jsonify(itineraries), 200

@app.route('/itineraries/<int:itinerary_id>', methods=['PUT'])
def update_itinerary(itinerary_id):
    data = request.get_json()
    activity = data['activity']

    with conn.cursor() as cursor:
        cursor.execute("UPDATE itineraries SET activity = %s WHERE id = %s", (activity, itinerary_id))
        conn.commit()

    return jsonify(message='Activity updated in itinerary'), 200

@app.route('/itineraries/<int:itinerary_id>', methods=['DELETE'])
def delete_itinerary(itinerary_id):
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM itineraries WHERE id = %s", (itinerary_id,))
        conn.commit()

    return jsonify(message='Activity removed from itinerary'), 200


# Expense Routes
@app.route('/expenses', methods=['POST'])
def create_expense():
    data = request.get_json()
    destination_id = data['destination_id']
    description = data['description']
    amount = data['amount']

    with conn.cursor() as cursor:
        cursor.execute("INSERT INTO expenses (destination_id, description, amount) VALUES (%s, %s, %s)", (destination_id, description, amount))
        conn.commit()

    return jsonify(message='Expense added successfully'), 201

@app.route('/expenses/<int:expense_id>', methods=['PUT'])
def update_expense(expense_id):
    data = request.get_json()
    description = data['description']
    amount = data['amount']

    with conn.cursor() as cursor:
        cursor.execute("UPDATE expenses SET description = %s, amount = %s WHERE id = %s", (description, amount, expense_id))
        conn.commit()

    return jsonify(message='Expense updated successfully'), 200

@app.route('/expenses/<int:expense_id>', methods=['DELETE'])
def delete_expense(expense_id):
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM expenses WHERE id = %s", (expense_id,))
        conn.commit()

    return jsonify(message='Expense deleted successfully'), 200

@app.route('/expenses', methods=['GET'])
def get_expenses():
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM expenses")
        expenses = cursor.fetchall()

    return jsonify(expenses), 200


if __name__ == '__main__':
    app.run(debug=True)