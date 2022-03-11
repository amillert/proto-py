#!/bin/bash

protoc -I=src/ --python_out=src/ src/simple.proto
protoc -I=src/ --python_out=src/ src/enum.proto
