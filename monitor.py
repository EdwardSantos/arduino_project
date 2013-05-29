import time
import serial
from threading import Thread

# List where we store the data read from the arduino
data = []

# Function which continuously appends new data.
def data_maker(port):
    global data
    data_buffer = ''
    while True:
        data_buffer = data_buffer + port.read(port.inWaiting())
        temp = data_buffer.splitlines()
        try:
            #data.append(float(x) for x in temp)
            for x in temp: data.append(float(x))
        except ValueError,e:
            print e
        time.sleep(0.005)

if __name__=='__main__':
    port = serial.Serial(port='/dev/tty.usbmodemfa131', # device name
                         baudrate=115200                 # matches arduino firmware
                        )
    thread = Thread(target=data_maker, args=(port,))
    thread.start()
    # Wait while data starts being added.
    time.sleep(5)
    print data
    # This will throw an exception which stops the started thread.
    port.close()
