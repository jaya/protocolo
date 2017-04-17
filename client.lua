local socket = require("socket")

host = 'localhost'
port = 8080

local client = socket.connect(host, port)
line = io.read()

while line and line ~= "" do
	size_header = string.char(string.len(line))
	message = size_header .. line
	client:send(message)
	data, err = client:receive(1)
	size = string.byte(data, 1)
	data, err = client:receive(size)
	print(data)
	line = io.read()
end