import sys
sys.path.append("../")

from core import writeCommunicator

print("Waiting for server...")
writeCommunicator("helloworld")
print('Sent:', 'helloworld')