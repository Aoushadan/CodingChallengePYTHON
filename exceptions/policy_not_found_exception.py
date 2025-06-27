class PolicyNotFoundException(Exception):
    def __init__(self, message="Policy not found"):
        super().__init__(message)
