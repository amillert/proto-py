from abc import ABC, abstractmethod


class ProtoBuffSerializer(ABC):
    def __init__(self, path: str) -> None:
        super().__init__()
        self._path = path
        self._msg = self._read_message()

    # api:
    def get_message(self):
        return self._msg

    def serialize(self) -> None:
        with open(self._path, "wb") as fout:
            str_bytes: bytes = self._msg.SerializeToString()
            fout.write(str_bytes)

        print(f"serialized message with `{self.__class__.__name__}`")

    @abstractmethod
    def deserialize(self):
        pass

    # private:
    @abstractmethod
    def _read_message(self):
        pass
