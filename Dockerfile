# Use official Python base image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy only the Python script into the container
COPY app.py /app/

# Install required Python packages
RUN pip install flask

EXPOSE 12120

# Run the script
CMD ["python", "app.py"]
