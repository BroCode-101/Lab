import random
import time

n, r = 0, 0

class Frame:
    def __init__(self):
        self.ack = 'y'
        self.data = 0

frm = [Frame() for _ in range(10)]

def sender():
    global n
    print("\nEnter the number of packets to be sent:")
    n = int(input())
    for i in range(n):
        print(f"\nEnter data for packet[{i}]:")
        frm[i].data = int(input())
        frm[i].ack = 'y'
    return 0

def recvfrm():
    global r
    random.seed()  # Initialize random number generator
    r = random.randint(0, n - 1)
    frm[r].ack = 'n'
    for i in range(n):
        if frm[i].ack == 'n':
            print(f"\nPacket no {r} is not received.")

def resend():
    global r
    print(f"\nResending packet {r}")
    time.sleep(2)
    frm[r].ack = 'y'
    print(f"\nReceived packet is {frm[r].data}")

def resend1():
    global r
    print(f"\nResending packet from {r}")
    for i in range(r, n):
        time.sleep(2)
        frm[i].ack = 'y'
        print(f"\nReceived data of packet {i} is {frm[i].data}")

def goback():
    sender()
    recvfrm()
    resend1()
    print("\nAll packets sent.")

def selective():
    sender()
    recvfrm()
    resend()
    print("\nAll packets are sent.")

def main():
    while True:
        print("\n1. Selective Repeat ARQ\n2. Go Back ARQ\n3. Exit")
        choice = int(input("\nEnter choice: "))
        if choice == 1:
            selective()
        elif choice == 2:
            goback()
        elif choice == 3:
            print("Exiting program.")
            break

if __name__ == "__main__":
    main()
