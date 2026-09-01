"""
Custom exception hierarchy for order data synchronization and file validation.
"""

class SyncError(Exception):
    """Base exception for all synchronizer-related errors."""
    pass


class CorruptedFileError(SyncError):
    """Raised when an uploaded file cannot be parsed or opened as a valid Excel workbook."""
    pass


class InsufficientDataError(SyncError):
    """Raised when a sheet contains insufficient rows or lacks actual data beyond headers."""
    pass


class MissingColumnsError(SyncError):
    """Raised when required column coordinates are out of bounds in the uploaded sheet."""
    pass


class SwappedFilesError(SyncError):
    """Raised when heuristics indicate the template and system export files were swapped."""
    pass


class NoMatchingOrdersError(SyncError):
    """Raised when zero orders match between the DATA sheet and WorkDataNew export."""
    pass