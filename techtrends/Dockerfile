# Start from the Python 3.8 base image
FROM python:3.8-slim-buster

# Set the working directory in the Docker container
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD techtrends /app

# Install the Python dependencies, suppress caching
RUN pip install --no-cache-dir -r requirements.txt

# Run the database initialization script
RUN python init_db.py

# Expose the port the app runs on
EXPOSE 3111

# Start the application
CMD ["python", "app.py"]
