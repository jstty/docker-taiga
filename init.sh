#!/bin/bash

echo "--------------------------------------------"
echo "Taiga Init..."
echo "--------------------------------------------"
echo "Cloning Backend..."
echo "--------------------------------------------"
git clone https://github.com/taigaio/taiga-back.git taiga-back

echo "--------------------------------------------"
echo "Cloning Frontend..."
echo "--------------------------------------------"
git clone https://github.com/taigaio/taiga-front-dist.git taiga-front-dist

echo "--------------------------------------------"
echo "Cloning Frontend..."
echo "--------------------------------------------"
git clone https://github.com/benhutchins/docker-taiga-events.git docker-taiga-events
