import time
import random

def sliding_window_protocol(window_size, frames):
    print(f"Total frames to send: {frames}")
    sent = 0
    ack = 0

    while sent < frames:
        print(f"\nSliding Window: Frames {sent + 1} to {min(sent + window_size, frames)}")
        for i in range(sent, min(sent + window_size, frames)):
            print(f"Frame {i + 1} sent")
        
        time.sleep(1)
        acks_received = random.randint(1, window_size)
        ack = min(sent + acks_received, frames)
        print(f"Acknowledgements received up to frame {ack}")
        
        if ack == frames:
            print("All frames acknowledged successfully.")
            break
        
        sent = ack
        print(f"Sliding window to next unacknowledged frame: {sent + 1}")

if __name__ == "__main__":
    frames = int(input("Enter the number of frames to send: "))
    window_size = int(input("Enter the sliding window size: "))
    sliding_window_protocol(window_size, frames)