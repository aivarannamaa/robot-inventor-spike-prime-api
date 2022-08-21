#!/usr/bin/env bash

. venv/bin/activate

echo "isorting ..."
isort enhanced_stubs

echo
echo "blackening ..."
black enhanced_stubs

#echo
#echo "running mypy ..."
#mypy thonny

echo
#echo "running pylint ..."
#pylint --msg-template='{abspath}:{line},{column:2d}: {msg} ({symbol})' thonny
