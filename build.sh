#!/bin/bash

export PWD=$(pwd)
ENV_FILE="./env.sh"


# if Mac OSX then set env to docker machine so docker commands work
if [ "$(uname)" == "Darwin" ]; then
	eval "$(docker-machine env default)"
fi

echo "--------------------------------------------"
echo "Taiga Setup Wizard"
echo "--------------------------------------------"

error () {
	echo "$1" >&2
	kill -INT $$
}

yesNoPrompt () {
	read -p "$2 [Yes/No] (default: $1)?" -n 1 choice
	echo "" >&2
	case "$choice" in 
  		y|Y ) echo "Yes";;
  		n|N ) echo "No";;
  		* ) echo "$1";;
	esac
}

prompt () {
	if [ -z "$3" ]; then
		read -p "$2 (default: $1)?" var

		if [ -z "$var" ]; then
			var=$1
		fi
	elif [ "$3" = "--required" ]; then

		if [ -z "$1" ]; then
			read -p "$2 (ex. $4)?" var

			if [ -z "$var" ]; then
				error "$2 is require"
			fi
		else
			read -p "$2 (enter to use: $1)?" var

			if [ -z "$var" ]; then
				var=$1
			fi
		fi
	fi

	echo $var
	return 0
}

CLEANUP_CONTAINERS=$(yesNoPrompt "No" "Do you want to stop and remove Taiga services")
if [ "$CLEANUP_CONTAINERS" == "Yes" ]; then
	# # Stop all containers
	# docker stop $(docker ps -a -q)
	# # Delete all containers
	# docker rm $(docker ps -a -q)

	# Stop service containers
	docker-compose stop
	# Delete service containers
	docker-compose rm
fi

CLEANUP_IMAGES=$(yesNoPrompt "No" "Do you want to remove Taiga images before we start")
if [ "$CLEANUP_IMAGES" == "Yes" ]; then
	# # Delete all images
	# docker rmi $(docker images -q)

	# Delete taiga images
	docker rmi taiga-events
	docker rmi taiga
fi

if [ -f "${ENV_FILE}" ]; then
	USE_ENV=$(yesNoPrompt "Yes" "Do you want to use the 'env.sh' settings")
fi

if [ "${USE_ENV}" == "Yes" ]; then
	source ${ENV_FILE}
else
	HOST_IP=$(docker-machine ip)

	export TAIGA_PORT=$(prompt "${TAIGA_PORT-8000}" "Frontend Port")
	export TAIGA_HOST=$(prompt "$TAIGA_HOST" "Frontend Hostname" --required "${HOST_IP}" )

	export EMAIL_HOST=$(prompt "${HOST_IP}" "Email Hostname")
	export EMAIL_PORT=$(prompt "25" "Email Port")
	export EMAIL_HOST_USER=$(prompt "" "Email Login Username")
	export EMAIL_HOST_PASSWORD=$(prompt "" "Email Login Password")

	export TAIGA_DB_NAME=$(prompt "taiga" "Taiga DB Name")
	export TAIGA_DB_USER=$(prompt "taiga" "Taiga DB Username")
	export TAIGA_DB_PASSWORD=$(prompt "password" "Taiga DB Password")

	EMAIL_USETLS=$(yesNoPrompt "No" "Email use TLS")
	if [ "$EMAIL_USETLS" == "Yes" ]; then
		export EMAIL_USE_TLS="True"
	else
		export EMAIL_USE_TLS="False"
	fi

	GITHUB=$(yesNoPrompt "No" "Github Integration")
	if [ "$GITHUB" == "Yes" ]; then
		export GITHUB_URL=$(prompt "https://github.com/" "Github URL")
		export GITHUB_API_URL=$(prompt "https://api.github.com/" "Github API URL")
		export GITHUB_API_CLIENT_ID=$(prompt "$GITHUB_API_CLIENT_ID" "Github API Client ID" --required "yourClientId")
		export GITHUB_API_CLIENT_SECRET=$(prompt "$GITHUB_API_CLIENT_SECRET" "Github API Client Secret" --required "yourClientSecret")
	else
		export GITHUB_URL=""
		export GITHUB_API_URL=""
		export GITHUB_API_CLIENT_ID=""
		export GITHUB_API_CLIENT_SECRET=""
	fi
fi

echo "--------------------------------------------"
echo "Hostname: $TAIGA_HOST"
echo "Port: $TAIGA_PORT"

echo "Email use TLS: $EMAIL_USE_TLS"
echo "Email Hostname: $EMAIL_HOST"
echo "Email Port: $EMAIL_PORT"
echo "Email Login User: $EMAIL_HOST_USER"
echo "Email Login Password: $EMAIL_HOST_PASSWORD"

echo "Taiga DB Name: $TAIGA_DB_NAME"
echo "Taiga DB Username: $TAIGA_DB_USER"
echo "Taiga DB Password: $TAIGA_DB_PASSWORD"

echo "Github URL: $GITHUB_URL"
echo "Github API URL: $GITHUB_API_URL"
echo "Github API Client ID: $GITHUB_API_CLIENT_ID"
echo "Github API Client Secret: $GITHUB_API_CLIENT_SECRET"
echo "--------------------------------------------"

if [ "$USE_ENV" != "Yes" ]; then
cat >${ENV_FILE} <<EOL
export TAIGA_HOST=$TAIGA_HOST
export TAIGA_PORT=$TAIGA_PORT

export EMAIL_USE_TLS=$EMAIL_USE_TLS
export EMAIL_HOST=$EMAIL_HOST
export EMAIL_PORT=$EMAIL_PORT
export EMAIL_HOST_USER=$EMAIL_HOST_USER
export EMAIL_HOST_PASSWORD=$EMAIL_HOST_PASSWORD

export TAIGA_DB_NAME=$TAIGA_DB_NAME
export TAIGA_DB_USER=$TAIGA_DB_USER
export TAIGA_DB_PASSWORD=$TAIGA_DB_PASSWORD

export GITHUB_URL=$GITHUB_URL
export GITHUB_API_URL=$GITHUB_API_URL
export GITHUB_API_CLIENT_ID=$GITHUB_API_CLIENT_ID
export GITHUB_API_CLIENT_SECRET=$GITHUB_API_CLIENT_SECRET
EOL

	# change file permin so it's executable
	chmod +x ${ENV_FILE}
fi

echo "--------------------------------------------"
echo "Build Services..."
echo "--------------------------------------------"
docker-compose build

echo "--------------------------------------------"
echo "Creating Containers..."
echo "--------------------------------------------"
docker-compose create
