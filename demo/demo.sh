#!/bin/env bash
echo "----------------------------------------"
echo -e "[THE GOOD]\n"
echo -e "$ python ../auditor.py ../models/good.json\n"
python ../auditor.py ../models/good.json
sleep 3
echo "----------------------------------------"
echo -e "[THE BAD]\n"
echo -e "$ python ../auditor.py ../models/bad.json\n"
python ../auditor.py ../models/bad.json
sleep 5
echo "----------------------------------------"
echo -e "[THE UGLY]\n"
echo -e "$ python ../auditor.py ../models/ugly.json\n"
python ../auditor.py ../models/ugly.json
echo "----------------------------------------"
