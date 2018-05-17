TRAVIS_REPO_SLUG ?= fernandoe/fe-endereco-server
TAG ?= local

build:
	docker build -t '${TRAVIS_REPO_SLUG}:${TAG}' .

test:
	cd src; pytest -s

travis.test:
	docker run --rm -it '${TRAVIS_REPO_SLUG}:${TAG}' pytest -s
