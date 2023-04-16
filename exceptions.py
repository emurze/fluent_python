class RangeListIsEmpty(Exception):
    """Occur when range is empty."""

    def __init__(self, *args) -> None:
        super().__init__(*args)
