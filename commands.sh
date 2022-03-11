#!/bin/bash

protoc -I=simple/ --python_out=simple/ simple/simple.proto
