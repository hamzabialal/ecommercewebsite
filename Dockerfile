# Use the official Python image
FROM python:3.10

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the requirements file into the container
#COPY ecommercewebiste/EcomProject/requirement.txt requirement.txt
COPY requirement.txt requirement.txt

# Install project dependencies
RUN pip install -r requirement.txt

# Copy project files into the container
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
CMD ["python", "manage.py", "runserver"]
