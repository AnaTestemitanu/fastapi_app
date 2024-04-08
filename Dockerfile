# Official Python runtime as a base image
FROM python:3.9

# Set working directory in the container to /code
WORKDIR /code

# Copy current directory contents into the container at /code
COPY ./app /code/app
COPY requirements.txt /code/

# Install required packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available
EXPOSE 8000

# Command to run app using Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
