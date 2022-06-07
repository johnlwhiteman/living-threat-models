#!/bin/env bash

echo "THE GOOD"
echo "$ python ./auditor.py ./models/good.json"
python ./auditor.py ./models/good.json
sleep 2

echo "THE BAD"
echo "$ python ./auditor.py ./models/bad.json"
python ./auditor.py ./models/bad.json
sleep 3

echo "THE UGLY"
echo "$ python ./auditor.py ./models/ugly.json"
python ./auditor.py ./models/ugly.json
