#!/bin/bash
cd "$(dirname "$0")"
uname -m > info.txt
python3 --version >> info.txt 2>&1
ldd --version | head -1 >> info.txt