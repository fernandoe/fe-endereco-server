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

compose-dump:
	docker-compose exec mysql-api-conta mysqldump -ppassword --add-drop-database conta > ./sandbox/docker-compose/mysql-init/api-conta/1.conta.sql
	docker-compose exec mysql-api-endereco mysqldump -ppassword --add-drop-database endereco > ./sandbox/docker-compose/mysql-init/api-endereco/1.endereco.sql
