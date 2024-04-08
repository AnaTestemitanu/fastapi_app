# FastAPI Async Application

This project is a FastAPI application that asynchronously retrieves data from multiple endpoints, performs complex data analysis, and exposes a simple REST API to access the results. It fetches data from the JSONPlaceholder Typicode API, analyzes the data to identify the user with the highest number of posts, calculates the average length of their post titles, finds the most common words used across all post titles, and uses FastAPI to create an endpoint /analysis to return the analysis results.

## Installation

To install the required dependencies, use pip:

```bash
pip install -r requirements.txt
```

## Running the App

You can run the app using:

```bash
uvicorn app.main:app --reload
```

And then open your browser and navigate to `http://localhost:8000/` to interact with the API.

## Docker

Build the Docker image using:

```bash
docker build -t fastapi_app .
```

Run the Docker container using:

```bash
docker run -d -p 8000:8000 fastapi_app
```

Then, open your browser and navigate to `http://localhost:8000/` to interact with the API.

## Testing

To run the tests, use pytest:

```bash
pytest
```

## API Endpoints

- `/analysis`: Fetches the analysis results.
