from vidstream import StreamingServer
import threading

HOST = "127.0.0.1"
PORT = 9999
def main():
    receiver = StreamingServer(HOST, PORT)

    # Start server in a separate thread
    server_thread = threading.Thread(target=receiver.start_server)
    server_thread.daemon = True
    server_thread.start()

    print(f"[INFO] Receiver started on {HOST}:{PORT}")
    print("[INFO] Type STOP to terminate")

    # Keep running until STOP is entered
    while True:
        cmd = input()
        if cmd.strip().upper() == "STOP":
            break

    receiver.stop_server()
    print("[INFO] Receiver stopped")

if __name__ == "__main__":
    main()