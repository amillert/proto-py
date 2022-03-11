from .pb_abc import ProtoBuffSerializer
from ..message.reflection import enum_pb2


class EnumProtoBuffSerializer(ProtoBuffSerializer):
    def __init__(self, path: str) -> None:
        super().__init__(path)

    def deserialize(self) -> enum_pb2.EnumMessage:
        with open(self._path, "rb") as fin:
            msg = enum_pb2.EnumMessage().FromString(fin.read())

        print(f"deserialized message with `{self.__class__.__name__}`")
        return msg

    def _read_message(self) -> enum_pb2.EnumMessage:
        msg = enum_pb2.EnumMessage()
        msg.id = 234
        msg.day_of_the_week = enum_pb2.SATURDAY  # equal to setting to 6

        return msg
