TRAVIS_REPO_SLUG ?= fernandoe/fe-endereco-api
TAG ?= local

build:
	docker build -t '${TRAVIS_REPO_SLUG}:${TAG}' .

push:
	docker push '${TRAVIS_REPO_SLUG}:${TAG}'

test:
	cd src; pytest -s

coveralls:
	cd src; coveralls

travis.test:
	docker run --rm -it '${TRAVIS_REPO_SLUG}:${TAG}' pytest -s
