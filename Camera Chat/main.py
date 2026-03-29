from vidstream import CameraClient, StreamingServer
import threading
import time
import sys

# ================= CONFIG =================
HOST = "127.0.0.1"   # Use 127.0.0.1 for same device
PORT = 9999
# ==========================================


def start_receiver(server):
    print(f"[INFO] Starting receiver on {HOST}:{PORT}")
    server.start_server()


def start_sender(client):
    print(f"[INFO] Starting camera stream to {HOST}:{PORT}")
    client.start_stream()


def main():
    # Initialize
    receiver = StreamingServer(HOST, PORT)
    sender = CameraClient(HOST, PORT)

    # Start receiver thread
    t1 = threading.Thread(target=start_receiver, args=(receiver,))
    t1.daemon = True
    t1.start()

    # Give server time to bind socket
    time.sleep(2)

    # Start sender thread
    t2 = threading.Thread(target=start_sender, args=(sender,))
    t2.daemon = True
    t2.start()

    print("[INFO] Streaming started")
    print("[INFO] Type STOP to terminate")

    # Keep running
    while True:
        cmd = input()
        if cmd.strip().upper() == "STOP":
            break

    # Cleanup
    print("[INFO] Stopping...")
    sender.stop_stream()
    receiver.stop_server()
    sys.exit()


if __name__ == "__main__":
    main()