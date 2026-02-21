from abc import ABC, abstractmethod
from typing import List, Dict, Optional, Any

from mine_spec.dto.object import (
    ObjectListResult,
    ObjectVersion,
    ObjectMetadata,
    BucketInfo,
    BucketUsage,
)


class ObjectStorageAdapter(ABC):
    # --------------------------------------------------------
    # Lifecycle
    # --------------------------------------------------------
    @abstractmethod
    def setup(self) -> None:
        pass

    @abstractmethod
    def list_objects(
        self,
        bucket: str,
        prefix: Optional[str],
        limit: int,
        continuation_token: Optional[str],
    ) -> ObjectListResult:
        pass

    @abstractmethod
    def delete_object(self, bucket: str, key: str) -> None:
        pass

    @abstractmethod
    def copy_object(
        self,
        source_bucket: str,
        source_key: str,
        dest_bucket: str,
        dest_key: str,
    ) -> None:
        pass

    @abstractmethod
    def generate_upload_url(
        self,
        bucket: str,
        key: str,
        expires_in: int,
        content_type: Optional[str] = None,
    ) -> str:
        pass

    @abstractmethod
    def generate_download_url(
        self,
        bucket: str,
        key: str,
        expires_in: int,
        response_content_type: Optional[str] = None,
        response_content_disposition: Optional[str] = None,
    ) -> str:
        pass

    @abstractmethod
    def list_object_versions(
        self,
        bucket: str,
        key: str,
    ) -> List[ObjectVersion]:
        pass

    @abstractmethod
    def delete_object_version(
        self,
        bucket: str,
        key: str,
        version_id: str,
    ) -> None:
        pass

    @abstractmethod
    def restore_object_version(
        self,
        bucket: str,
        key: str,
        version_id: str,
    ) -> None:
        pass

    @abstractmethod
    def get_object_metadata(
        self,
        bucket: str,
        key: str,
    ) -> ObjectMetadata:
        pass

    @abstractmethod
    def update_object_metadata(
        self,
        bucket: str,
        key: str,
        metadata: Dict[str, str],
    ) -> None:
        pass

    @abstractmethod
    def get_object_tags(
        self,
        bucket: str,
        key: str,
    ) -> Dict[str, str]:
        pass

    @abstractmethod
    def update_object_tags(
        self,
        bucket: str,
        key: str,
        tags: Dict[str, str],
    ) -> None:
        pass

    # Buckets
    @abstractmethod
    def list_buckets(self) -> List[BucketInfo]:
        pass

    @abstractmethod
    def create_bucket(self, name: str) -> None:
        pass

    @abstractmethod
    def delete_bucket(self, name: str) -> None:
        pass

    @abstractmethod
    def set_bucket_versioning(
        self,
        name: str,
        enabled: bool,
    ) -> None:
        pass

    @abstractmethod
    def get_bucket_usage(self, name: str) -> BucketUsage:
        pass

    @abstractmethod
    def get_bucket_policy(
        self,
        bucket: str,
    ) -> Optional[Dict[str, Any]]:
        pass

    @abstractmethod
    def put_bucket_policy(
        self,
        bucket: str,
        policy: Dict[str, Any],
    ) -> None:
        pass

    @abstractmethod
    def delete_bucket_policy(
        self,
        bucket: str,
    ) -> None:
        pass

    @abstractmethod
    def get_bucket_lifecycle(
        self,
        bucket: str,
    ) -> Optional[Dict[str, Any]]:
        pass

    @abstractmethod
    def put_bucket_lifecycle(
        self,
        bucket: str,
        lifecycle: Dict[str, Any],
    ) -> None:
        pass

    @abstractmethod
    def delete_bucket_lifecycle(
        self,
        bucket: str,
    ) -> None:
        pass

    @abstractmethod
    def get_bucket_events(
        self,
        bucket: str,
    ) -> Dict[str, Any]:
        pass

    @abstractmethod
    def put_bucket_events(
        self,
        bucket: str,
        config: Dict[str, Any],
    ) -> None:
        pass

    @abstractmethod
    def delete_bucket_events(
        self,
        bucket: str,
    ) -> None:
        pass
