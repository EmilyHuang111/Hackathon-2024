import time
import serial

ser = serial.Serial('/dev/tty.usbserial-14120', 9600)

def main():
    time.sleep(2)
    run()
    print("Program Stopped")


def move(command):
    ser.write(command.encode())

def run():
    while True:
        command = input("Enter command (F/B/L/R/S): ")
        if command == "FS":
            move("S")
            ser.close()
            break
        move(command)


if __name__ == "__main__":
    main()