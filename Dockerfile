# Use an official Python runtime as a parent image
FROM python:3.11.4

# Set the working directory in the container to /app
WORKDIR /GW_WEB_CHAT

# Add the current directory contents into the container at /app
ADD . /GW_WEB_CHAT

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "app.py"]