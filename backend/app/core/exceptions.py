class DatasetError(Exception):
    """Base exception for dataset processing failures."""


class InvalidDatasetError(DatasetError):
    """Raised when a dataset cannot be parsed or validated."""


class DatasetNotFoundError(DatasetError):
    """Raised when a temporary dataset id is unknown."""
