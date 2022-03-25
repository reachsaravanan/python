"""
Function to decode and encode.

"""


def reverser(function):
    def inner(a):
        a = function(a)
        a = a[::-1]
        return a
    return inner


def encoder(function):
    def inner(b):
        temp_list =""
        for i in b:
            temp_list += chr(ord(i)+2)
        return temp_list
    return inner


def decoder(function):
    def inner(b):
        temp_list = ""
        for i in b:
            temp_list += chr(ord(i)-2)
        return temp_list
    return inner


@reverser
@encoder
def my_send_message(c):
    return c


@reverser
@decoder
def my_receive_message(c):
    return c


Input_Message = "Attack At Dawn"
print("Input Message\t\t:", Input_Message)
message_sent = my_send_message(Input_Message)
print("Message Sent\t\t:", message_sent)
message_received = my_receive_message(message_sent)
print("Message Receiver\t:", message_received)
