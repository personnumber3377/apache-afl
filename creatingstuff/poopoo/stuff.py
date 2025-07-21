
'''
> PUT /ff/test31232.txt HTTP/1.1
> Host: 127.0.0.1:8080
> Authorization: Digest username="user1", realm="DAV-upload", nonce="w7OFLWU6BgA=6637d8a07db2e677058ae7c11fa8f18144330e32", uri="/ff/test31232.txt", cnonce="NWE5NDUxYmMyNWUzZDFmN2ViNGNlMTU1MTZjM2JkMzA=", nc=00000001, qop=auth, response="3bee47705e57bbaa999dc2f30a26dfba", algorithm=MD5
> User-Agent: curl/8.5.0
> Accept: */*
>
'''

'''

PUT /ff/test31232.txt HTTP/1.1
Host: 127.0.0.1:8080
Authorization: Digest username="user1", realm="DAV-upload", nonce="w7OFLWU6BgA=6637d8a07db2e677058ae7c11fa8f18144330e32", uri="/ff/test31232.txt", cnonce="NWE5NDUxYmMyNWUzZDFmN2ViNGNlMTU1MTZjM2JkMzA=", nc=00000001, qop=auth, response="3bee47705e57bbaa999dc2f30a26dfba", algorithm=MD5
User-Agent: curl/8.5.0
Accept: */*


'''

data = '''PUT /ff/test31231.txt HTTP/1.1
Host: 127.0.0.1:8080
Authorization: Digest username="user1", realm="DAV-upload", nonce="w7OFLWU6BgA=6637d8a07db2e677058ae7c11fa8f18144330e32", uri="/ff/test31231.txt", cnonce="NWE5NDUxYmMyNWUzZDFmN2ViNGNlMTU1MTZjM2JkMzA=", nc=00000001, qop=auth, response="3bee47705e57bbaa999dc2f30a26dfba", algorithm=MD5
User-Agent: curl/8.5.0
Accept: */*'''

data = data.replace("\n", "\r\n")
data = data + "\r\n\r\n"

# data += "aaaaaaa"



thing = '''PUT /ff/test31231.txt HTTP/1.1
Host: 127.0.0.1:8080
User-Agent: curl/8.5.0
Accept: */*'''




thing = thing.replace("\n", "\r\n")
thing = thing + "\r\n\r\n"

# print(thing, end="")
# print(data, end="")

things = ["OPTIONS", "MKCOL", "PUT", "DELETE", "MOVE", "PROPFIND"]

def save_data(data, i):
	fh = open("out/"+str(i), "w")
	fh.write(data)
	fh.close()
	return

for i, option in enumerate(things):
	# Replace the method here...
	actual_data = data.replace("PUT", option) # Replace the thing
	save_data(actual_data, i)
	actual_data = actual_data.replace("test31231.txt", "")
	save_data(actual_data, i+1000)
