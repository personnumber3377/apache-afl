

'''
const char *response1 = "220 FuzzFTP ready\r\n";
    const char *response2 = "331 Please specify the password.\r\n";
'''


SEPARATOR = "ABC"

thing = ["220 Ready\r\n",
    "331 Password required\r\n",
    "230 Login OK\r\n",
    "200 PWD successful\r\n",
    "200 Type set to I\r\n",
    "227 Entering Passive Mode (127,0,0,1,123,45)\r\n",
    "150 Here comes the directory listing\r\n",
    "226 Directory send OK\r\n"]


# data = "220 FuzzFTP ready\r\nABC331 Please specify the password.\r\nABC230 Login successful.\r\n"

data = SEPARATOR.join(thing)

fh = open("payload.txt", "w")
fh.write(data)
fh.close()


print(data, end="")
