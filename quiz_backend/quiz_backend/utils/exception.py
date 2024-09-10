
class InvalidInputException(Exception):
    def __init__(self, args:object):
        self.invalid_input = args

class NotFoundException(Exception):
    def __init__(self, args: object):
        self.not_found = args

class ConflictException(Exception):
    def __init__(self,args:object):
        self.conflict_input = args