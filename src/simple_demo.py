import simple_pb2
import enum_pb2


def read_simple_message() -> simple_pb2.SimpleMessage:
    """
    Uses reflection; therefore, can't really navigate the code freely
    """

    simple_message = simple_pb2.SimpleMessage()
    simple_message.id = 123

    # if set to False - it will not display as it's a default value
    simple_message.is_simple = True
    simple_message.name = "simple message"

    # repeated is not a list but provides list api on top
    simple_list = simple_message.sample_list
    simple_list.append(1)
    simple_list.extend([2, 3])

    return simple_message


def serialize_proto_simple(msg: simple_pb2.SimpleMessage, path: str) -> None:
    with open(path, "wb") as fout:
        str_bytes: bytes = msg.SerializeToString()
        fout.write(str_bytes)


def deserialize_proto_simple(path: str) -> simple_pb2.SimpleMessage:
    with open(path, "rb") as fin:
        # there seems to be no intermediate bytes representation involved
        # simple_message: simple_pb2.SimpleMessage = simple_pb2.SimpleMessage()
        # msg: simple_pb2.SimpleMessage = simple_message.FromString(fin.read())

        msg = simple_pb2.SimpleMessage().FromString(fin.read())

    return msg


def simple_message() -> None:
    msg = read_simple_message()
    _path = "src/simple.bin"

    serialize_proto_simple(msg, _path)
    assert msg == deserialize_proto_simple(_path), "deserialization unsuccessful"


def read_enum_message() -> enum_pb2.EnumMessage:
    enum_message = enum_pb2.EnumMessage()
    enum_message.id = 234
    enum_message.day_of_the_week = enum_pb2.SATURDAY  # equal to setting to 6

    return enum_message


def serialize_proto_enum(msg: enum_pb2.EnumMessage, path: str) -> None:
    with open(path, "wb") as fout:
        str_bytes: bytes = msg.SerializeToString()
        fout.write(str_bytes)


def deserialize_proto_enum(path: str) -> enum_pb2.EnumMessage:
    with open(path, "rb") as fin:
        msg = enum_pb2.EnumMessage().FromString(fin.read())

    return msg


def enum_message() -> None:
    msg = read_enum_message()
    _path = "src/enum.bin"

    serialize_proto_enum(msg, _path)
    assert msg == deserialize_proto_enum(_path), "deserialization unsuccessful"


if __name__ == "__main__":
    simple_message()
    enum_message()
