import collections


def _upper(key):
    return key.upper() if key.isupper() else key


class UpperCaseMixin:
    def __setitem__(self, key, value):
        return super().__setitem__(_upper(key), value)  # type: ignore

    def __getitem__(self, item):
        return super().__getitem__(item)  # type: ignore

    def get(self, key, default=None):
        return super().get(_upper(key), default)  # type: ignore

    def __contains__(self, key):
        return super().__contains__(_upper(key))  # type: ignore


class UpperDict(UpperCaseMixin, collections.UserDict):
    """Specialized Dict, that save all keys if str then UpperCase"""


if __name__ == '__main__':
    d1 = UpperDict()
    d1["a"] = "b"
    print(d1.get("a"))
    print(d1)
    print("a" in d1)
