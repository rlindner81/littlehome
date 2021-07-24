#!/bin/sh
script=`readlink -f "$0"`
script_dir=`dirname "$script"`
script_name=`basename "$script" .sh`
cd script_dir/../

# requires
# npm i -g yarn @quasar/cli

git pull \
&& yarn \
&& rm -rf dist/ \
&& quasar build
