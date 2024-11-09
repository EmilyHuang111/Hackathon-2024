import time
import serial
#import struct

ser = serial.Serial('/dev/tty.usbserial-14120', 9600)
time.sleep(2)

def main():
    run()
    print("Program Stopped")


def move(command):
    c = ser.write(command.encode())
    if command == "U":
        #print(struct.unpack('b',ser.read(c)))
        distance = ser.readline().decode('utf-8').strip()
        print(distance)

def run():
    while True:
        command = input("Enter command (F/B/L/R/S/U/FS): ").upper()
        if command == "FS":
            move("S")
            ser.close()
            break
        move(command)


if __name__ == "__main__":
    main()

