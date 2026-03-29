from vidstream import ScreenShareClient
import threading

HOST = "127.0.0.1"
PORT = 9999

def main():
    sender = ScreenShareClient(HOST, PORT)

    # Start streaming in a separate thread
    stream_thread = threading.Thread(target=sender.start_stream)
    stream_thread.daemon = True
    stream_thread.start()

    print(f"[INFO] Streaming to {HOST}:{PORT}")
    print("[INFO] Type STOP to terminate")

    # Keep running until STOP is entered
    while True:
        cmd = input()
        if cmd.strip().upper() == "STOP":
            break

    sender.stop_stream()
    print("[INFO] Streaming stopped")

if __name__ == "__main__":
    main()