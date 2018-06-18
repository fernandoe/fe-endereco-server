#!/bin/bash

set -ev

make build

echo "$DOCKER_PASS" | docker login -u $DOCKER_USER --password-stdin

make push
