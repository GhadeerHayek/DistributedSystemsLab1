# step 1: declare the foundation - the base : FROM instruction
FROM python:3.10-slim

# step 2: get the code into the image

WORKDIR /app

# to optimise the steps: we'll copy the requirements and install them first

COPY requirements.txt .

# step 3: install dependencies

RUN pip3 install -r requirements.txt

# step 4: copy the application logic
COPY . .

CMD [ "python3", "app.py" ]