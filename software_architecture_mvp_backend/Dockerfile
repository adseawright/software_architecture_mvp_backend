# Use the official Python image from the Docker Hub
FROM python:3.12

# Set the working directory inside the container to /usr/src/app
WORKDIR /usr/src/app

# Copy the requirements.txt file and install any needed packages
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to /usr/src/app
COPY . .

# Run database migrations
RUN flask db upgrade

# Expose port 5000 to the outside world
EXPOSE 5000

# Command to run the application
CMD ["python", "run.py"]
