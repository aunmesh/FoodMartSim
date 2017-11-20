#Comma seperated Value Logger
class logger(object):

    def __init__(self, name, heading, max_unflush=1):
        self.name = name
        self.handle = open(self.name, 'wb')
        self.heading = heading
        self.num_fields = len(self.heading)
        self.handle.write(self.make_string(heading))
        self.unlogged = 0
        self.max_unflush = max_unflush

    def make_string(self, fields):
        fields = [str(x) for x in fields]
        return ','.join(fields)+'\n'

    def log(self, values):
        assert(len(values) == self.num_fields), len(values)
        self.handle.write(self.make_string(values))
        self.unlogged += 1
        if self.unlogged == self.max_unflush:
            self.handle.flush()
            self.unlogged = 0
