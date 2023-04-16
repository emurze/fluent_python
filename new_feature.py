# from __future__ import annotations
import inspect
from dataclasses import dataclass, field
import random


# @dataclass(eq=True, frozen=True)
# class User:
#     first_name: str
#     last_name: str
#     password: str
#     password_hint: str = field(repr=False)
#     friends: list[str] = field(default_factory=list)
#
#
# def update_user_friends(_user: User, _friends) -> User:
#     friend = _friends.pop(random.randrange(len(_friends)))
#     _user.friends.append(friend)
#     return _user


# if __name__ == '__main__':
#     user = User('Vlad', 'Zama_tev_ski', "qwerty", "Lera")
#     friends = ["Rav_ski", "Mal_ceva"]
#     print(update_user_friends(user, friends))
#     print(inspect.get_annotations(update_user_friends))


# if __name__ == '__main__':
#     from realize_abc import LottoBlower
#
#     machine = LottoBlower[int](range(10))
#
#     print(LottoBlower)
