#!/bin/bash

cp replace_host_key.sh ../riehseun.github.io/terraform/main
cd main
cp main.tf backend.tf variable.tf outputs.tf ../../riehseun.github.io/terraform/main
cd ..
cd modules
cp -r * ../../riehseun.github.io/terraform/module
cd ..
cd ../riehseun.github.io
sh git.sh
cd ../terraform
