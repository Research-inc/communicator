import os

COMM_NAME = "naocomm"
def writeCommunicator(data):

    # Create a named pipe
    os.mkfifo(COMM_NAME)

    # In another process or script
    with open(COMM_NAME, "w") as pipe:
        pipe.write(data)

    os.remove(COMM_NAME)

def readCommunicator():
    data = None
    with open(COMM_NAME, "r") as pipe:
        data = pipe.read()
    return data

