from socket import *


# First , let us start by creating a TCP/UDP client socket : 

## Part 1 : TCP Client Socket
#############################

clientSocket = socket(AF_INET,SOCK_STREAM)
serverPort = 50005


## Part 2 : Making a connection to the server :
################################################
clientSocket.