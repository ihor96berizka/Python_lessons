import serial

with serial.Serial() as ser:
    ser.baudrate = 9600
    ser.port = '/dev/ttyUSB0'
    ser.open()
    while True:
        data = input('Enter led: ')
        if not data: break
        ser.write((data.rstrip().encode()))
        print(data.rstrip())
    
