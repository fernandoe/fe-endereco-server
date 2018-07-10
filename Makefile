TRAVIS_REPO_SLUG ?= fernandoe/fe-endereco-server
TAG ?= local

build:
	docker build -t '${TRAVIS_REPO_SLUG}:${TAG}' .

test:
	cd src; pytest -s

travis.test:
	docker run --rm -it '${TRAVIS_REPO_SLUG}:${TAG}' pytest -s

compose-migrate:
	docker-compose exec api-conta python manage.py migrate
	docker-compose exec api-endereco python manage.py migrate
