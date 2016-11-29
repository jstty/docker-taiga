#!/bin/bash

echo "--------------------------------------------"
echo "Taiga Init..."
echo "--------------------------------------------"
echo "Cloning Backend..."
echo "--------------------------------------------"
if [ -d "./taiga-back/src" ]; then
	echo "Already cloned"
else
	cd taiga-back
	git clone https://github.com/taigaio/taiga-back.git src
	cd ..
fi

echo "--------------------------------------------"
echo "Cloning Frontend..."
echo "--------------------------------------------"
if [ -d "./taiga-front-dist/src" ]; then
	echo "Already cloned"
else
	cd taiga-front-dist
	git clone https://github.com/taigaio/taiga-front-dist.git src
	cd ..
fi

echo "--------------------------------------------"
echo "Cloning Frontend..."
echo "--------------------------------------------"
if [ -d "./taiga-events/src" ]; then
	echo "Already cloned"
else
	cd taiga-events
	git clone https://github.com/taigaio/taiga-events src
	cd ..
fi
