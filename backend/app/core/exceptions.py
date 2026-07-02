from fastapi import HTTPException, status

class BaseAppException(Exception):
    def __init__(self, message: str, status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)

class OAuthError(BaseAppException):
    def __init__(self, message: str = "OAuth authentication failed"):
        super().__init__(message, status_code=status.HTTP_401_UNAUTHORIZED)

class GmailSyncError(BaseAppException):
    def __init__(self, message: str = "Failed to sync with Gmail"):
        super().__init__(message, status_code=status.HTTP_502_BAD_GATEWAY)

class ClassificationError(BaseAppException):
    def __init__(self, message: str = "Failed to classify email"):
        super().__init__(message, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)

class ActionExecutionError(BaseAppException):
    def __init__(self, message: str = "Failed to execute action"):
        super().__init__(message, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

class RetryExhaustedError(BaseAppException):
    def __init__(self, message: str = "Maximum retry attempts exhausted"):
        super().__init__(message, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
