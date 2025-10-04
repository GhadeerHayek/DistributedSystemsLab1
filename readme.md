# Distributed Systems Lab 1: Synchronous Communication Patterns

**Author**: Ghadeer Alhayek

**Student** ID: 25253905 

## 📖 Project Overview

This project implements three different patterns of synchronous request-response communication in distributed systems.
With each phase, we move from the low-leve (sockets) to modern high-performance RPC frameworks.

- Phase 1: A simple client-server application using the socket library in Python.
- Phase 2: A RESTful API server using the Flask framework.
- Phase 3: A client-server application using the gRPC and Protocol Buffers. 


## 🚀 How to Run the Entire Project

The project is fully containerized using Docker compose, allowing all services to be built and run with one single command.
1- Clone the repository to your local machine 
2- Navigate to the root directory 
3- Run the following command

    `docker-compose up --build`

- This will run the servers in the three phases (socket, flask, gRPC)

4- To see the client in action, you can run them in a seperate terminal
for the socket lab and the gRPC lab: 
docker exec -it <container_name> python client.py 

for the flask app: 
docker exec -it <container_name> python3 app.py 

5- to stop and remove all containers, run: 

    `docker-compose down`

## 📂 Project Structure


## 🎓 Core Concepts: Synchronous Communication & Key Differences

A synchronous call is when the client sends a request, and it stops and waits until it receives a response from the server. 

_Each phase demonstrates this pattern:_ 

**Phase 1**: 

The client will not execute

    Line 15: `print("server said: ", response)` 

until this is executed
    
    Line 16: `response = client_socket.recv(1024)`  

It is blocked by the Operating system until the server sends data back over TCP connection, this is a classical example of a blocking, synchronous call. 


**Phase 2**: 

Phase 2 represents the standard HTTP request-response model, which is a synchronous one.
When a client sends an HTTP GET or POST request, it waits for the server to send back a complete HTTP response. 
The client code's execution is paused until that response is fully received. 



**Phase 3**: 

Phase 3 represents a standard gRPC call which is synchronous by default. 
When a client calls a method via the client stub, 
what happens behind the scenes is that the client stub in that thread blocks the execution of that thread until the server's response comes back. 


## Trade-offs and key differences

### Sockets

- #### Pros

    Lightweight, no external libraries needed 
  
- #### Cons

    You have to manage everything manually, not scalable for complex APIs 

### REST/Flask 

- #### Pros

    human-readable (JSON), easy to debug with tools like postman, stateless, follows web standards (HTTP)

- #### Cons

    could be slower compared with gRPC since it uses text-based JSON parsing over HTTP. 

### gRPC

- #### Pros

    Extermely high performance due to binary protocol buffers. 

- #### Cons

    More complex initial setup, not human-readable

