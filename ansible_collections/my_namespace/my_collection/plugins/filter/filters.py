class FilterModule(object):
    def filters(self):
        return {
            'all_is_mark': self.all_is_mark,
        }
    def all_is_mark(self, name):
        return "MARK"