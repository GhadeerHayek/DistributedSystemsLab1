FROM python:3.10-slim

LABEL authors="ghadeerhayek"

WORKDIR /app

# copy requirements file

COPY requirements.txt .

# copy the rest of the project files into the working dir

COPY . .

# run the app

CMD ["python3", "server.py"]