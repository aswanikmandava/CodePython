import socket


def server_program():
    # get the hostname
    host = '192.168.1.1'
    port = 7110 # initiate port no above 1024
    server_socket = socket.socket()  # get instance
    server_socket.bind((host, port))  # bind host address and port together
    # configure how many client the server can listen simultaneously
    server_socket.listen(5)
    try:
        while True:
            conn, address = server_socket.accept()  # accept new connection
            print(f"Connection from: {address}")
            # receive data stream. it won't accept data packet greater than 1024 bytes
            data = conn.recv(1024).decode()
            # print(f"Got this data from connected user: {data}")
            data = "Hello from server"
            conn.send(data.encode())  # send data to the client
            print(f"Sent Hello to client {address}")
            conn.close()  # close the connection
            print(f"client connection {address} is closed")
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(f"Caught err: {e}")
    finally:
        server_socket.close()
        print("server socket is closed")


if __name__ == '__main__':
    server_program()