# **Distributed Systems Lab — Phase 2 - RESTful API Implementation**

This service implements a RESTful API for a simple User service using the Flask web framework.
It exposes standard API endpoints (GET, POST, PUT, DELETE) to interact with a collection of users stored in memory.

## Technologies used

- Python = 3.10 
- Flask 


### How to run standalone? 
Quick testing without docker. 


1.  Navigate to this directory (`/python-socket-lab`).

2. install the required dependices 

    
    `pip3 install -r requirements.txt`

3. Start flask server on one terminal:

        `python3 app.py `
The server will start on http://localhost:5000.

4. In a separate terminal, you can test the API with curl. For example, to get all users:

        `curl http://localhost:5000/api/users`

    or you could import the attached collection to Postman. 

### How to run using docker? 
A `DockerFile` is included to containerize the server component of this phase. This allows it to be managed and run by the main 
`docker-compose.yml` file at the project root. 


| Command                                     | Description                                                                                                            |
|:--------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------|
| **`FROM python:3.10-slim`**                 | *Starts from the official lightweight Python 3.10 image.*                                                              |
| **`WORKDIR /app`**                          | *Sets the working directory inside the container to `/app`.*                                                           |
| **`COPY requirements.txt .`**               | *Copies requirements.txt file from the current directory on the machine to current directory on the container `/app`.* |
| **`RUN pip3 install -r requirements.txt `** | *Installs dependencies.*                                                                                               |
| **`COPY . .`**                              | *Copies the application code into the container.*                                                                      |
| **`CMD ["python", app.py]`**                | *Runs the Flask server file*                                                                                           |

## **Testing the code**

After running the server, you can test the code via importing the collection and executing requests.
!(DistributedSystems.postman_collection.json)


## **Output**
Output of the code can be found as example after each endpoint..