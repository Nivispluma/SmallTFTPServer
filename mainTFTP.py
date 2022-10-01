# import fbtftp

from fbtftp.base_handler import BaseHandler
from fbtftp.base_server import BaseServer

import os
from os.path import exists

from datetime import datetime

LISTEN_ON = '192.168.1.2'
SERVER_PORT = 69
TFTP_ROOT = 'opt/ztp/tftproot'
RETRIES = 3
TIMEOUT = 5


class TftpData:

    def __init__(self, filename):
        print(f"Filname: {filename}")
        path = os.path.join(TFTP_ROOT, filename)
        print(f"Path: {path}")
        file_exists = exists(path)
        if not file_exists:
            raise Exception("File doesnt exist")

        self._size = os.stat(path).st_size
        self._reader = open(path, 'rb')

    def read(self, data):
        return self._reader.read(data)

    def size(self):
        return self._size

    def close(self):
        self._reader.close()


class StaticHandler(BaseHandler):

    def get_response_data(self):
        return TftpData(self._path)


class TftpServer(BaseServer):

    def get_handler(self, server_addr, peer, path, options):
        print(f"listening on {LISTEN_ON}:{SERVER_PORT}")
        return StaticHandler(
            server_addr, peer, path, options, session_stats)


def session_stats(stats):
    print('')
    print('#' * 60)
    print('Peer: {} UDP/{}'.format(stats.peer[0], stats.peer[1]))
    print('File: {}'.format(stats.file_path))
    print('Sent Packets: {}'.format(stats.packets_sent))
    print('#' * 60)

    log_time = f"{datetime.now()}"
    log_time = log_time.replace(" ", "_")
    log_time = log_time.replace(":", "-")
    log_time = log_time.replace(".", "-")

    log_ipaddress = f"{stats.peer[0]}"
    log_ipaddress = log_ipaddress.replace(".", "-")

    log_requested_file = stats.file_path
    log_file_changed_extention = log_requested_file.replace(".","-")
    print(log_ipaddress)
    
    current_log_file = open(f"log/{log_time}_{log_file_changed_extention}_{log_ipaddress}.txt", "w")
    print("Logfile created")
    current_log_file.write(f"Peer: {stats.peer[0]}:{stats.peer[1]}")
    current_log_file.write(f"File {stats.file_path}")
    current_log_file.close()
    print("Logfile filled")


def main():
    server = TftpServer(LISTEN_ON, SERVER_PORT, RETRIES, TIMEOUT)
    server.run()


if __name__ == '__main__':
    main()
