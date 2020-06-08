.venv :
	( \
		python -m venv .venv ; \
		source .venv/bin/activate ; \
		pip install -r requirements.txt \
	)

setup : .venv

generated : .venv
	(\
		source .venv/bin/activate ; \
		mkdir generated; \
		python -m grpc_tools.protoc -Iproto --python_out=. --grpc_python_out=. proto/generated/summer.proto \
	)

test : generated
	.venv/bin/python -m pytest .

run : generated
	.venv/bin/python -m server

run_client : generated
	.venv/bin/python -m client 1 2 3

clean_venv :
	rm -rf .venv

clean_generated :
	rm -rf generated

clean : clean_venv clean_generated
