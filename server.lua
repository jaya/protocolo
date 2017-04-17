local socket = require("socket")

function parse_set(message)
	res = message:match("SET (%d+)")
	if res then
		state = res
		return "OK " .. state
	else
		return nil
	end
end

function parse_get(message)
	res = message:match("GET")
	if res then
		return "OK " .. state
	else
		return nil
	end
end

local parsers = {parse_set, parse_get}
local host = 'localhost'
local port = 8080

server = socket.bind('*', 8080)

local ip, port = server:getsockname()

print("Escutando em " .. ip .. ":" .. port)

while true do

	local client = server:accept()

	print("Conexão aceita")

	while true do

		local data, err = client:receive(1)

		if err then 
			print("Erro / cliente desconectado")
			break
		end

		local size = string.byte(data, 1)

		print("Aguardando", size .. " bytes")

		data, err = client:receive(size)

		if err then 
			print("Erro / cliente desconectado")
			break
		end

		print("Recebido", data)

		res = nil

		for _, parser in pairs(parsers) do
			res = parser(data)
			if res then
				
				local size_header = string.char(string.len(res))
				local payload = res
				local message = size_header .. res

				print("Resposta", payload)
				client:send(message)
				break
			end
		end

	end

	client:close()
end