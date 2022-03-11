#!/usr/bin/env python

from proto.serializers.pb_enum import EnumProtoBuffSerializer as EnumPB
from proto.serializers.pb_simple import SimpleProtoBuffSerializer as SimplePB


def test_serialization(pb) -> None:
    pb.serialize()
    assert pb.get_message() == pb.deserialize(), "deserialization unsuccessful"


if __name__ == "__main__":
    spb = SimplePB("src/proto/message/bin/simple.bin")
    epb = EnumPB("src/proto/message/bin/enum.bin")

    test_serialization(spb)
    test_serialization(epb)
