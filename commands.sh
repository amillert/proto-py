#!/bin/bash

protoc -I=src/proto/message/ --python_out=src/proto/message/reflection src/proto/message/simple.proto
protoc -I=src/proto/message/ --python_out=src/proto/message/reflection src/proto/message/enum.proto
