
# Wanderlust Travel Planner API

Welcome to the Wanderlust Travel Planner API! This API provides functionalities to manage travel destinations, itineraries, and expenses, along with fetching weather data.

## Prerequisites

Before you begin, ensure you have the following installed:

- [Python](https://www.python.org/downloads/)
- [PostgreSQL](https://www.postgresql.org/download/)

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up the database:

   - Create a PostgreSQL database and update the `DATABASE_URL` variable in your `.env` file.

4. Run the application:

   ```bash
   python app.py
   ```

   The application will be accessible at [http://localhost:5000/](http://localhost:5000/).

## API Endpoints

### 1. Welcome Message

- **Endpoint:** `/`
- **Method:** `GET`
- **Description:** Displays a welcome message.
- **Example:**
  ```bash
  curl http://localhost:5000/
  ```

### 2. Get Weather Data

- **Endpoint:** `/weather`
- **Method:** `GET`
- **Parameters:**
  - `location` (query parameter): The location for which weather data is requested.
- **Description:** Retrieves weather data for the specified location.
- **Example:**
  ```bash
  curl http://localhost:5000/weather?location=Paris
  ```

### 3. Create Destination

- **Endpoint:** `/destinations`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "name": "Paris",
    "description": "The City of Light",
    "location": "France"
  }
  ```
- **Description:** Creates a new travel destination.
- **Example:**
  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{"name": "Paris", "description": "The City of Light", "location": "France"}' http://localhost:5000/destinations
  ```

### 4. Get Destinations

- **Endpoint:** `/destinations`
- **Method:** `GET`
- **Description:** Retrieves a list of all travel destinations.
- **Example:**
  ```bash
  curl http://localhost:5000/destinations
  ```

### 5. Get Destination by ID

- **Endpoint:** `/destinations/{destination_id}`
- **Method:** `GET`
- **Description:** Retrieves details of a specific travel destination by ID.
- **Example:**
  ```bash
  curl http://localhost:5000/destinations/1
  ```

### 6. Update Destination

- **Endpoint:** `/destinations/{destination_id}`
- **Method:** `PUT`
- **Request Body:**
  ```json
  {
    "name": "Updated Paris",
    "description": "Updated description",
    "location": "Updated France"
  }
  ```
- **Description:** Updates details of a specific travel destination by ID.
- **Example:**
  ```bash
  curl -X PUT -H "Content-Type: application/json" -d '{"name": "Updated Paris", "description": "Updated description", "location": "Updated France"}' http://localhost:5000/destinations/1
  ```

### 7. Delete Destination

- **Endpoint:** `/destinations/{destination_id}`
- **Method:** `DELETE`
- **Description:** Deletes a specific travel destination by ID.
- **Example:**
  ```bash
  curl -X DELETE http://localhost:5000/destinations/1
  ```

### 8. Create Itinerary

- **Endpoint:** `/itineraries`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "destination_id": 1,
    "activity": "Visit the Eiffel Tower"
  }
  ```
- **Description:** Adds a new activity to the itinerary for a specific destination.
- **Example:**
  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{"destination_id": 1, "activity": "Visit the Eiffel Tower"}' http://localhost:5000/itineraries
  ```

### 9. Get Itineraries

- **Endpoint:** `/itineraries`
- **Method:** `GET`
- **Description:** Retrieves a list of all itinerary items.
- **Example:**
  ```bash
  curl http://localhost:5000/itineraries
  ```

### 10. Update Itinerary

- **Endpoint:** `/itineraries/{itinerary_id}`
- **Method:** `PUT`
- **Request Body:**
  ```json
  {
    "activity": "Updated activity"
  }
  ```
- **Description:** Updates the activity in the itinerary item by ID.
- **Example:**
  ```bash
  curl -X PUT -H "Content-Type: application/json" -d '{"activity": "Updated activity"}' http://localhost:5000/itineraries/1
  ```

### 11. Delete Itinerary

- **Endpoint:** `/itineraries/{itinerary_id}`
- **Method:** `DELETE`
- **Description:** Removes an activity from the itinerary by ID.
- **Example:**
  ```bash
  curl -X DELETE http://localhost:5000/itineraries/1
  ```

### 12. Create Expense

- **Endpoint:** `/expenses`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "destination_id": 1,
    "description": "Dinner at a local restaurant",
    "amount": 50.0
  }
  ```
- **Description:** Adds a new expense for a specific destination.
- **Example:**
  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{"destination_id": 1, "description": "Dinner at a local restaurant", "amount": 50.0}' http://localhost:5000/expenses
  ```

### 13. Update Expense

- **Endpoint:** `/expenses/{expense_id}`
- **Method:** `PUT`
- **Request Body:**
  ```json
  {
    "description": "Updated expense",
    "amount": 60.0
  }
  ```
- **Description:** Updates details of a specific expense by ID.
- **Example:**
  ```bash
  curl -X PUT -H "Content-Type: application/json" -d '{"description": "Updated expense", "amount": 60.0}' http://localhost:5000/expenses/1
  ```

### 14. Delete Expense

- **Endpoint:** `/expenses/{expense_id}`
- **Method:** `DELETE`
- **Description:** Deletes a specific expense by ID.
- **Example:**
  ```bash
  curl -X DELETE http://localhost:5000/expenses/1
  ```

### 15. Get Expenses

- **Endpoint:** `/expenses`
