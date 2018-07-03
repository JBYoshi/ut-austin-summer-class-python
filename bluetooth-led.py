# The communication format looks like this:
# '0' - light is off
# '1' - light is on
# Send '0' to turn the light off, '1' to turn it on
# Send '?' to get the current state of the light
# The RPi sends '0' when the light is off, '1' when the light is on

from bluetooth import *
import RPi.GPIO as GPIO

server_sock = BluetoothSocket(RFCOMM)
server_sock.bind(("",PORT_ANY))
server_sock.listen(1)

uuid = "00001101-0000-1000-8000-00805f9b7541"

advertise_service(server_sock, 'JR',
                  service_id = uuid,
                  service_classes = [uuid, SERIAL_PORT_CLASS],
                  profiles = [SERIAL_PORT_PROFILE],
                 )

on = False
gpioSlot = 18
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(gpioSlot, GPIO.OUT)

while True:
    print 'Waiting for connection on RFCOMM'
    client_sock, client_info = server_sock.accept()
    print 'Accepted connection from: ', client_info

    try:
        data = client_sock.recv(1)
        if len(data) == 0: break
        print 'received [%s]' % data
        if data == '1':
            on = True
            GPIO.output(gpioSlot, GPIO.HIGH)
            client_sock.send('1')
        elif data == '0':
            on = False
            GPIO.output(gpioSlot, GPIO.LOW)
            client_sock.send('0')
        elif data == '?':
            if on:
                client_sock.send('1')
            else:
                client_sock.send('0')

    except IOError:
        pass

    except KeyboardInterrupt:
        print 'disconnected'
        client_sock.close()
        server_sock.close()
        GPIO.output(gpioSlot, GPIO.LOW)
        print 'all done!'
        break
    
