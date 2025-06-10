.PHONY: compile shell

compile:
	docker exec -it python-grpc-grpc-demo-1 sh -c "mkdir -p /src/pb && python -m grpc_tools.protoc -I/src/proto --python_out=/src/pb --pyi_out=/src/pb --grpc_python_out=/src/pb /src/proto/hello_world.proto"
	@echo "Compilation completed successfully"

shell:
	docker exec -it python-grpc-grpc-demo-1 sh