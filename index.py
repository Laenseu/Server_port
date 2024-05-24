import http.server
import socketserver
import threading

# Define the ports to open
PORTS = [1111, 1112, 1113]

class ServerThread(threading.Thread):
    def __init__(self, port):
        threading.Thread.__init__(self)
        self.port = port

    def run(self):
        handler = http.server.SimpleHTTPRequestHandler
        httpd = socketserver.TCPServer(("", self.port), handler)
        print(f"Serving on port {self.port}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print(f"Server on port {self.port} is stopping.")
            httpd.server_close()

def start_servers(ports):
    threads = []
    for port in ports:
        server_thread = ServerThread(port)
        server_thread.start()
        threads.append(server_thread)

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    start_servers(PORTS)
