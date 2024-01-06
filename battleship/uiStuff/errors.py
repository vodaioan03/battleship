class ErrorException(Exception):
    pass


class InvalidCommand(ErrorException):
    def __init__(self,):
        super().__init__("Invalid Command! Type again.")


class InvalidPlayer(ErrorException):
    def __init__(self,):
        super().__init__('Invalid Player! Type <player> or <computer>.')
class GameStaredError(ErrorException):
    def __init__(self,):
        super().__init__("Can't use this command after game started!")
        
class GameNotStarted(ErrorException):
    def __init__(self,):
        super().__init__("Can't use this command before game started!")
class ParamsNumbersError(ErrorException):
    def __init__(self,):
        super().__init__(("Params needs to be numbers."))   
        
        