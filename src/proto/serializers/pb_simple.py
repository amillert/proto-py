from .pb_abc import ProtoBuffSerializer
from ..message.reflection import simple_pb2


class SimpleProtoBuffSerializer(ProtoBuffSerializer):
    def __init__(self, path: str) -> None:
        super().__init__(path)

    def get_message(self):
        return self._msg

    def deserialize(self) -> simple_pb2.SimpleMessage:
        with open(self._path, "rb") as fin:
            msg = simple_pb2.SimpleMessage().FromString(fin.read())

        print(f"deserialized message with `{self.__class__.__name__}`")
        return msg

    def _read_message(self) -> simple_pb2.SimpleMessage:
        """
        Uses reflection; therefore, can't really navigate the code freely
        """

        msg = simple_pb2.SimpleMessage()
        msg.id = 123

        # if set to False - it will not display as it's a default value
        msg.is_simple = True
        msg.name = "simple message"

        # repeated is not a list but provides list api on top
        simple_list = msg.sample_list
        simple_list.append(1)
        simple_list.extend([2, 3])

        return msg
