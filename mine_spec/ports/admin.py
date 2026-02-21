from abc import ABC, abstractmethod
from typing import List, Dict

from mine_spec.dto.admin import (
    User,
    GroupInfo,
    GroupList,
    GroupPolicyMapp,
    GroupPolicyDetached,
    GroupPolicyAttached,
    BucketQuota,
    ListServiceAccounts,
    CreateServiceAccount,
    Policy,
    PolicyAttached,
    PolicyDetached,
)


class UserAdminPort(ABC):

    # --------------------------------------------------------
    # Setup alias
    # --------------------------------------------------------
    @abstractmethod
    def setup(self):
        pass

    # --------------------------------------------------------
    # Bucket quota
    # --------------------------------------------------------
    @abstractmethod
    def set_bucket_quota(self, bucket: str, quota: str) -> List[BucketQuota]:
        pass

    @abstractmethod
    def get_bucket_quota(self, bucket: str) -> List[BucketQuota]:
        pass

    # --------------------------------------------------------
    # Users
    # --------------------------------------------------------

    @abstractmethod
    def list_users(self) -> List[User]:
        pass

    @abstractmethod
    def get_user(self, username: str) -> List[User]:
        pass

    @abstractmethod
    def create_user(self, username: str, password: str) -> List[User]:
        pass

    @abstractmethod
    def delete_user(self, username: str) -> List[User]:
        pass

    @abstractmethod
    def enable_user(self, username: str) -> List[User]:
        pass

    @abstractmethod
    def disable_user(self, username: str) -> List[User]:
        pass

    # --------------------------------------------------------
    # Group
    # --------------------------------------------------------
    @abstractmethod
    def list_groups(self) -> List[GroupList]:
        pass

    @abstractmethod
    def group_info(self, name: str) -> List[GroupInfo]:
        pass

    @abstractmethod
    def create_group(self, name: str, users: list[str]) -> List[GroupInfo]:
        pass

    @abstractmethod
    def remove_group(self, name: str) -> List[GroupInfo]:
        pass

    @abstractmethod
    def remove_users_from_group(
        self, name: str, users: list[str]
    ) -> List[GroupInfo]:
        pass

    @abstractmethod
    def add_users_to_group(
        self, name: str, users: list[str]
    ) -> List[GroupInfo]:
        pass

    @abstractmethod
    def enable_group(self, name: str) -> List[GroupInfo]:
        pass

    @abstractmethod
    def disable_group(self, name: str) -> List[GroupInfo]:
        pass

    # --------------------------------------------------------
    # Policies
    # --------------------------------------------------------
    @abstractmethod
    def list_policies(self) -> List[Policy]:
        pass

    @abstractmethod
    def get_policy(self, name: str) -> List[Policy]:
        pass

    @abstractmethod
    def create_policy(self, name: str, file_path: str) -> List[Policy]:
        pass

    @abstractmethod
    def delete_policy(self, name: str) -> List[Policy]:
        pass

    @abstractmethod
    def attach_policy(
        self, policy: str, username: str
    ) -> List[PolicyAttached]:
        pass

    @abstractmethod
    def detach_policy(
        self, policy: str, username: str
    ) -> List[PolicyDetached]:
        pass

    @abstractmethod
    def attach_policy_to_group(
        self, policy: str, group: str
    ) -> List[GroupPolicyAttached]:
        pass

    @abstractmethod
    def detach_policy_from_group(
        self, policy: str, group: str
    ) -> List[GroupPolicyDetached]:
        pass

    @abstractmethod
    def get_policy_from_group(self, group: str) -> List[GroupPolicyMapp]:
        pass

    # --------------------------------------------------------
    # Service Accounts
    # --------------------------------------------------------

    @abstractmethod
    def list_service_accounts(
        self, username: str
    ) -> List[ListServiceAccounts]:
        pass

    @abstractmethod
    def create_service_account(
        self,
        username: str,
        policy: str | None = None,
        expiration: str | None = None,
    ) -> List[CreateServiceAccount]:
        pass

    @abstractmethod
    def delete_service_account(
        self, access_key: str
    ) -> List[ListServiceAccounts]:
        pass

    # --------------------------------------------------------
    # Notification Targets
    # --------------------------------------------------------

    @abstractmethod
    def add_notification_target(
        self,
        target_type: str,
        identifier: str,
        config: dict,
    ) -> List[Dict]:
        pass

    @abstractmethod
    def remove_notification_target(
        self,
        target_type: str,
        identifier: str,
    ) -> List[Dict]:
        pass

    @abstractmethod
    def list_notification_targets(
        self, target_type: str | None = None
    ) -> List[Dict]:
        pass
