
class InvalidInputException(Exception):
    def __init__(self, args:object) -> None:
        self.invalid_input = args

class NotFoundException(Exception):
    def __init__(self, args: object) -> None:
        self.not_found = args

class ConflictException(Exception):
    def __init__(self,args:object) -> None:
        self.conflict_input = args