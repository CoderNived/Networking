from vidstream import AudioSender, AudioReceiver
import threading
import socket
import sys

# ================= CONFIG =================
# Receiver machine IP (the one that will play audio)
RECEIVER_IP = "192.168.0.207"
PORT = 9999
# ==========================================

def main():
    # Receiver listens on all interfaces (important)
    receiver = AudioReceiver("0.0.0.0", PORT)

    # Sender sends audio to receiver IP
    sender = AudioSender(RECEIVER_IP, PORT)

    # Threads
    receive_thread = threading.Thread(target=receiver.start_server)
    receive_thread.daemon = True

    sender_thread = threading.Thread(target=sender.start_stream)
    sender_thread.daemon = True

    # Start
    receive_thread.start()
    sender_thread.start()

    print("[INFO] Audio streaming started")
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