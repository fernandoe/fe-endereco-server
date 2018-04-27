TRAVIS_REPO_SLUG ?= fernandoe/fe-endereco-server
TAG ?= local

docker-build:
	docker build -t fernandoe/fe-endereco-server:local .

build:
	docker build -t fernandoe/fe-endereco-server:local .

test:
	cd src; pytest -s

travis.test:
	docker run --rm -it '${TRAVIS_REPO_SLUG}:${TAG}' pytest -s
