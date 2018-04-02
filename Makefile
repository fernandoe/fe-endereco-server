docker-build:
	docker build -t fernandoe/fe-endereco-server:local .

test:
	python setup.py test
