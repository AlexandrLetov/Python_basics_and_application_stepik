class Buffer:
    def __init__(self):
        self.lst = []

    def add(self, *a):
        for item in a:
            self.lst.append(item)
            if len(self.lst) == 5:
                print(sum(self.lst))
                self.lst = self.lst[5:]

    def get_current_part(self):
        return self.lst
