#!/usr/bin/env python3
import os
import sys

# EAFP - Easy to ASk Forrgiveness than permission
# (É mais fácil pedir perdão do que permissão)

try:
    names = open("names.txt").readlines()
    # FileNotFoundError
except FileNotFoundError as e:
    print(f"{str(e)}.")
    sys.exit()
    # TODO: Usar retry

try:
    print(names[2])
except:
    print("[Error] Missing name in the list")
    sys.exit()
