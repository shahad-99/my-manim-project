FROM ubuntu:latest

# Install required packages
RUN apt-get update && \
    apt-get install -y python3-pip python3-dev python3-venv git manim

# Set up the working directory
WORKDIR /app

# Create a virtual environment
RUN python3 -m venv venv

# Activate the virtual environment
ENV PATH="/app/venv/bin:$PATH"

# Install manim dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy the Manim project
COPY . .

# Expose port for the Manim server
EXPOSE 8000

# Run the Manim server
CMD ["manim", "--disable-caching", "--open", "scenes/ExampleScene.py"]
