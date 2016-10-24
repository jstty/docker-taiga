#!/bin/bash

export PWD=$(pwd)
ENV_FILE="./env.sh"


# if Mac OSX then set env to docker machine so docker commands work
if [ "$(uname)" == "Darwin" ]; then
	eval "$(docker-machine env default)"
fi

echo "--------------------------------------------"
echo "Taiga"
echo "--------------------------------------------"

if [ -f "${ENV_FILE}" ]; then
	source ${ENV_FILE}
else
	./build.sh	
fi

# convert to absolute path
export TAIGA_DATA_DIR=`cd "$TAIGA_DATA_DIR"; pwd`

echo "--------------------------------------------"
echo "Starting Containers in background"
echo "--------------------------------------------"
docker-compose up -d "$@"

URL="http://${TAIGA_HOST}:${TAIGA_PORT}/login"
echo "--------------------------------------------"
echo "Go to: ${URL}"
echo "Default Login"
echo "user: admin"
echo "pass: 123123"
echo "--------------------------------------------"
