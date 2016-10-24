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
	
	echo "--------------------------------------------"
	echo "Stop Service Containers"
	echo "--------------------------------------------"
	docker-compose stop
else
	echo "env.sh is missing, it's need, run build.sh to create it."
fi
