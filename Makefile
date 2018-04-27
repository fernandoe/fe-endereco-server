docker-build:
	docker build -t fernandoe/fe-endereco-server:local .

test:
	python setup.py test

travis.test:
	docker run --rm -it '${TRAVIS_REPO_SLUG}:${COMMIT}' pytest -s
