from typing import TypedDict, Any, cast


class BookDict(TypedDict):  # useless
    isbn: int
    title: str
    author: str
    page_count: int


def loads(*args) -> Any:
    return 1


def test(data: str) -> BookDict:
    whatever: BookDict = loads()
    return whatever


if __name__ == '__main__':
    # book = BookDict(isbn=4, title="War and Piece",
    #                 author="Vlad", page_count=684)
    # print(book)
    # NOT_BOOK_JSON = """
    #     {"title": "Andromeda Strain",
    #     "flavor": "pistachio",
    #     "authors": true}
    # """
    #
    # book1 = test(NOT_BOOK_JSON)
    # print(book1["flavor"])

    _list: list[int] = [1, 2]
    _tuple: tuple = cast(tuple[int], _list)

    _tuple.append(4)
    print(_tuple)
