# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import socket

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
def service_client(new_socket):
    request = new_socket.recv(1024)     #套接字每次接收页面内容的最大字节
    print(request)
    response = 'HTTP/1.1 200 OK\r\n'
    response += '\r\n'
    response += 'hello world'
    new_socket.send(response.encode('utf-8'))                   #通过套接字发送内容


def main():
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)    #创建套接字


    tcp_server_socket.bind(('', 8000))   #绑定服务到IP及端口
    tcp_server_socket.listen(128)       #最大支持同时访问的用户数

    while True:
        #new_socket: 服务器连接浏览器时，产生一个套接字来负责数据的接收和发送
        #client-addr: 用户的IP和port
        new_socket, client_addr = tcp_server_socket.accept()
        service_client(new_socket)

    tcp_server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)   #结束服务时立即释放端口
    tcp_server_socket.close()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    main()
