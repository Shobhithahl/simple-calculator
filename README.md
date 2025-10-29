# Age Calculator API

A simple FastAPI microservice that calculates a person's current age from their date of birth.

## Features

- Calculate age from date of birth in YYYY-MM-DD format
- Input validation (date format and future date check)
- RESTful API with automatic interactive documentation
- Clean response with age, original date, and calculation date

## Installation

1. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

Start the server using uvicorn:

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## API Endpoints

### GET `/`
Root endpoint that provides API information.

**Response:**
```json
{
  "message": "Age Calculator API",
  "description": "Use POST /calculate-age to get age from date of birth",
  "docs": "/docs"
}
```

### POST `/calculate-age`
Calculate age from date of birth.

**Request Body:**
```json
{
  "date_of_birth": "1990-05-15"
}
```

**Response:**
```json
{
  "age": 35,
  "date_of_birth": "1990-05-15",
  "calculation_date": "2025-10-07"
}
```

**Error Responses:**
- `400 Bad Request`: Invalid date format or future date

## Interactive Documentation

Once the server is running, visit:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Example Usage

### Using curl:

```bash
curl -X POST "http://localhost:8000/calculate-age" \
  -H "Content-Type: application/json" \
  -d '{"date_of_birth": "1990-05-15"}'
```

### Using Python requests:

```python
import requests

response = requests.post(
    "http://localhost:8000/calculate-age",
    json={"date_of_birth": "1990-05-15"}
)
print(response.json())
```

## Date Format

All dates must be in **YYYY-MM-DD** format (e.g., 1990-05-15).

## Validation

The API validates:
1. Date format must be YYYY-MM-DD
2. Date of birth cannot be in the future
# simple-calculator
