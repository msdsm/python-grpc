.PHONY: up down clean compile server client shell

# Docker Compose operations
up:
	docker-compose up -d

down:
	docker-compose down

clean:
	docker-compose down --rmi all --volumes --remove-orphans

# Protocol Buffer compilation
compile:
	docker exec -it python-grpc-grpc-demo-1 sh -c "mkdir -p /src/pb && python -m grpc_tools.protoc -I/src/proto --python_out=/src/pb --pyi_out=/src/pb --grpc_python_out=/src/pb /src/proto/hello_world.proto"
	@echo "Compilation completed successfully"

# gRPC server and client execution
server:
	docker exec -it python-grpc-grpc-demo-1 python server.py

client:
	docker exec -it python-grpc-grpc-demo-1 python client.py

# Container shell access
shell:
	docker exec -it python-grpc-grpc-demo-1 sh