class NonPositiveError(Exception):
    pass


class PositiveList(list):

    def append(self, value):
        if value > 0:
            list.append(self, value)
        else:
            raise NonPositiveError()
