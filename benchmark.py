import time
import requests
import user_service_pb2
import user_service_pb2_grpc
import grpc
import socket


# Benchmark settings
NUM_REQUESTS = 10000
HOST = "0.0.0.0"
SOCKET_PORT = 8080
REST_PORT = 5050
REST_URL = f"http://{HOST}:{REST_PORT}/api/users"
GRPC_PORT = 50051


# Add this function after the configuration section

def benchmark_socket():
    print("--- Benchmarking Sockets ---")
    latencies = []
    for i in range(NUM_REQUESTS):
        start_time = time.time()
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((HOST, SOCKET_PORT))
                message = f"hello {i}"
                s.sendall(message.encode())
                s.recv(1024)
        except ConnectionRefusedError:
            print("Socket server is not running. Aborting.")
            return None, None  # Return None if the test fails
        end_time = time.time()
        latencies.append(end_time - start_time)

    total_time = sum(latencies)
    avg_latency = total_time / NUM_REQUESTS
    throughput = NUM_REQUESTS / total_time
    return avg_latency, throughput


def benchmark_rest():
    print("--- Benchmarking REST (Flask) ---")
    latencies = []
    # Use a session for connection pooling, which is more efficient
    session = requests.Session()
    for i in range(NUM_REQUESTS):
        start_time = time.time()
        try:
            # We will test a POST request as it's a common operation
            payload = {'name': f'User {i}', 'email': f'user{i}@example.com'}
            response = session.post(REST_URL, json=payload)
            response.raise_for_status()  # Raise an exception for bad status codes
        except requests.exceptions.RequestException as e:
            print(f"REST server is not running or encountered an error: {e}. Aborting.")
            return None, None
        end_time = time.time()
        latencies.append(end_time - start_time)

    total_time = sum(latencies)
    avg_latency = total_time / NUM_REQUESTS
    throughput = NUM_REQUESTS / total_time
    return avg_latency, throughput


def benchmark_grpc():
    print("--- Benchmarking gRPC ---")
    latencies = []
    try:
        with grpc.insecure_channel(f'{HOST}:{GRPC_PORT}') as channel:
            stub = user_service_pb2_grpc.UserServiceStub(channel)
            for i in range(NUM_REQUESTS):
                start_time = time.time()
                request = user_service_pb2.CreateUserRequest(name=f"gRPC User {i}", email=f"grpc{i}@example.com")
                stub.createUser(request)
                end_time = time.time()
                latencies.append(end_time - start_time)
    except grpc.RpcError as e:
        if e.code() == grpc.StatusCode.UNAVAILABLE:
            print("gRPC server is not running. Aborting.")
            return None, None
        else:
            print(f"An unexpected gRPC error occurred: {e}")
            return None, None

    total_time = sum(latencies)
    avg_latency = total_time / NUM_REQUESTS
    throughput = NUM_REQUESTS / total_time
    return avg_latency, throughput


if __name__ == "__main__":
    print(
        "Starting benchmarks ...\n")

    socket_latency, socket_throughput = benchmark_socket()
    rest_latency, rest_throughput = benchmark_rest()
    grpc_latency, grpc_throughput = benchmark_grpc()

    print("\n--- Benchmark Results ---")
    print(f"{'Metric':<20} | {'Socket':<15} | {'REST (Flask)':<15} | {'gRPC':<15}")
    print("-" * 70)

    # Check if results are valid before printing
    if all(res is not None for res in [socket_latency, rest_latency, grpc_latency]):
        print(
            f"{'Avg Latency (ms)':<20} | {socket_latency * 1000:<15.2f} | {rest_latency * 1000:<15.2f} | {grpc_latency * 1000:<15.2f}")
        print(
            f"{'Throughput (req/s)':<20} | {socket_throughput:<15.2f} | {rest_throughput:<15.2f} | {grpc_throughput:<15.2f}")
    else:
        print("One or more benchmarks failed to run. Cannot display results.")

    print("\n--- Analysis ---")
    if rest_latency and grpc_latency and grpc_latency < rest_latency:
        print(
            "As expected, gRPC shows lower average latency than the REST API due to its use of HTTP/2 and binary Protocol Buffers.")
    if rest_throughput and grpc_throughput and grpc_throughput > rest_throughput:
        print("gRPC also demonstrates higher throughput, able to handle more requests per second.")
