

# with open("text.txt", "r", encoding='utf-8') as f:
#     res = f.read()
#
# print(f.closed, f.encoding)
# print(res)
import sys
from contextlib import contextmanager


class LookingGlass:
    def reversed_write(self, text):
        return self.original_write(text[::-1])

    def __enter__(self):
        self.original_write = sys.stdout.write
        sys.stdout.write = self.reversed_write
        return 1, 2

    def __exit__(self, exp_type, exp_value, traceback):
        sys.stdout.write = self.original_write
        print(sys.exc_info())
        if exp_type is ZeroDivisionError:
            print("Please DON'T divide by zero!")
            return True


with LookingGlass() as (first, second):
    print("Vlad is gay!")
    print(f"{first}{second}")
    print(1 / 0)


# @contextmanager
# def looking_glass():
#     original_write = sys.stdout.write
#
#     def reversed_write(text):
#         return original_write(text[::-1])
#
#     sys.stdout.write = reversed_write
#     msg = ''
#     try:
#         yield "LERKA"
#     except ZeroDivisionError:
#         msg = "Please DON'T divide by zero!"
#     finally:
#         sys.stdout.write = original_write
#         if msg:
#             print(msg)


# @looking_glass()
# def cat():
#     print("VLAD")


# cat()
