import fbtftp

from fbtftp.base_handler import BaseHandler
from fbtftp.base_server import BaseServer

import os
from os.path import exists

LISTEN_ON = '192.168.178.61'
SERVER_PORT = 50102
TFTP_ROOT = '/opt/ztp/tftproot'
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


def main():
    server = TftpServer(LISTEN_ON, SERVER_PORT, RETRIES, TIMEOUT)
    server.run()



if __name__ == '__main__':
    main()
