import socket

HEADER = 64 
PORT =5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "10.65.188.123"
ADDR= (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send (msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length+= b' ' * (HEADER - len(send_length))    # dopełnienie tak, aby długość wynosiła 64, 
                                                        # b - oznacza bajtową reprezentacje ciągu. Dodając spacje dodajemy dopełniene
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))             # widaomości z serwera do klienta. Liczba musi byc odpowienio duża aby odesłać wiadomość lub uzyto tego samego protokołu którego użyto do wysyłania wiadomość do serwera. Wiadomość zdekodowalismy aby miec pewność ze to nie jest bajt

send("Hello World!")
input()
send("Hello wszystkim!")
input()
send("Hello Jarek!")
input()
send("Hello World!")
send(DISCONNECT_MESSAGE)                # wysłanie wiadomości o rozłączeniu i zamkniecie servera. 
                                        # Jeśli uruchomimy ponownie ten skrypt cały czas w konsoli
                                        #  bedziemy widzieli ze mamy tylko jedno aktywne połaczenie 