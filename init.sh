#!/bin/bash

echo "--------------------------------------------"
echo "Taiga Init..."
echo "--------------------------------------------"
echo "Cloning Backend..."
echo "--------------------------------------------"
if [ -d "taiga-back" ]; then
	echo "Already cloned"
else
	git clone https://github.com/taigaio/taiga-back.git taiga-back
fi

echo "--------------------------------------------"
echo "Cloning Frontend..."
echo "--------------------------------------------"
if [ -d "taiga-front-dist" ]; then
	echo "Already cloned"
else
	git clone https://github.com/taigaio/taiga-front-dist.git taiga-front-dist
fi

echo "--------------------------------------------"
echo "Cloning Frontend..."
echo "--------------------------------------------"
if [ -d "taiga-events" ]; then
	echo "Already cloned"
else
	git clone https://github.com/taigaio/taiga-events taiga-events
fi
