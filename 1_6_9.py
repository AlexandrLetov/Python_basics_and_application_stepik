class LoggableList(list, Loggable):
    def append(self, value):
        list.append(self, value)
        Loggable.log(self, value)
