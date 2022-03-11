import simple_pb2


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


def serialize_proto(msg: simple_pb2.SimpleMessage, path: str) -> None:
    with open(path, "wb") as fout:
        str_bytes: bytes = msg.SerializeToString()
        fout.write(str_bytes)


def deserialize_proto(path: str) -> simple_pb2.SimpleMessage:
    with open(path, "rb") as fin:
        # there seems to be no intermediate bytes representation involved
        # simple_message: simple_pb2.SimpleMessage = simple_pb2.SimpleMessage()
        # msg: simple_pb2.SimpleMessage = simple_message.FromString(fin.read())

        msg = simple_pb2.SimpleMessage().FromString(fin.read())

    return msg


def simple_message() -> None:
    msg = read_simple_message()
    _path = "src/simple.bin"

    serialize_proto(msg, _path)
    assert msg == deserialize_proto(_path), "deserialization unsuccessful"


if __name__ == "__main__":
    simple_message()
