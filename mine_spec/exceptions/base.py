class StorageException(Exception):
    """Base exception for storage layer."""

    pass


class BucketNotFound(StorageException):
    pass


class BucketAlreadyExists(StorageException):
    pass


class ObjectNotFound(StorageException):
    pass


class AccessDenied(StorageException):
    pass


class InvalidConfiguration(StorageException):
    pass


class NotSupported(StorageException):
    pass


class ConflictError(StorageException):
    pass


class InternalStorageError(StorageException):
    pass
