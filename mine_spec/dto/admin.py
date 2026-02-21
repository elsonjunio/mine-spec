from dataclasses import dataclass
from typing import Optional, Dict, List


@dataclass
class GroupMappings:
    group: str
    policies: Optional[List[str]] = None


@dataclass
class ResultGroupMappings:
    timestamp: str
    group_mappings: Optional[List[GroupMappings]] = None


@dataclass
class PolicyInfo:
    policy_name: str
    policy: Optional[Dict] = None
    create_date: Optional[str] = None
    update_date: Optional[str] = None


@dataclass
class GroupMembership:
    name: str
    policies: Optional[List[str]] = None


@dataclass
class User:
    access_key: str
    status: str
    member_of: Optional[List[GroupMembership]] = None


@dataclass
class GroupInfo:
    group_name: str
    status: Optional[str] = None
    members: Optional[List[str]] = None


@dataclass
class GroupList:
    groups: Optional[str] = None


@dataclass
class GroupPolicyMapp:
    result: Optional[ResultGroupMappings] = None


@dataclass
class GroupPolicyDetached:
    group: str
    policies_detached: Optional[List[str]] = None


@dataclass
class GroupPolicyAttached:
    group: str
    policies_attached: Optional[List[str]] = None


@dataclass
class BucketQuota:
    bucket: str
    type: str
    quota_bytes: int


@dataclass
class ListServiceAccounts:
    access_key: str


@dataclass
class CreateServiceAccount:
    status: str
    access_key: str
    secret_key: str
    expiration: str


@dataclass
class Policy:
    policy: str
    is_group: bool
    policy_info: Optional[PolicyInfo] = None


@dataclass
class PolicyAttached:
    user: str
    policies_attached: Optional[List[str]] = None


@dataclass
class PolicyDetached:
    user: str
    policies_detached: Optional[List[str]] = None


# ---
