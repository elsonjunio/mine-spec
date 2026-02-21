from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Dict, List


@dataclass(slots=True)
class StorageObject:
    key: str
    size: int
    last_modified: datetime
    etag: str
    storage_class: Optional[str] = None


@dataclass(slots=True)
class ObjectListResult:
    objects: List[StorageObject]
    is_truncated: bool
    next_continuation_token: Optional[str]


@dataclass(slots=True)
class ObjectVersion:
    version_id: str
    is_latest: bool
    last_modified: datetime
    size: int


@dataclass(slots=True)
class ObjectVersionListResult:
    versions: List[ObjectVersion]


@dataclass(slots=True)
class ObjectMetadata:
    size: int
    etag: str
    last_modified: datetime
    content_type: Optional[str]
    metadata: Dict[str, str]


@dataclass(slots=True)
class BucketInfo:
    name: str
    creation_date: datetime


@dataclass(slots=True)
class BucketUsage:
    objects: int
    size_bytes: int
