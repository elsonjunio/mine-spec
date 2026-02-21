# mine-spec

Provider-agnostic storage specification contracts for object storage systems.

`mine-spec` defines typed domain contracts (Ports), DTOs and provider-neutral exceptions for object storage and storage administration layers.

This package does not implement any provider logic.
It exists purely as a stable contract between backend services and storage drivers.

---

### 🎯 Purpose

The goal of this package is to:

 - Provide strongly typed interfaces for storage drivers
 - Enforce architectural boundaries (Clean Architecture)
 - Decouple business logic from provider implementations (MinIO, S3, Azure, etc.)
 - Standardize domain exceptions
 - Enable multi-provider support without coupling

This package is intended for internal usage across services and driver implementations.

---

### 🏗 Architectural Role

This package represents the Domain Contract Layer.

It defines:

 - **Ports (Protocols)** → Interfaces implemented by drivers
 - **DTOs** → Typed input/output models
 - **Exceptions** → Provider-agnostic domain errors
 - **Capabilities** → Optional feature discovery support

It does NOT contain:

 - Network calls
 - CLI execution
 - Provider SDK usage
 - Infrastructure logic
 - Persistence
 - IO operations

```bash
📦 Package Structure
mine-spec/
└── src/mine_spec/
    ├── dto/
    │   ├── admin.py
    │   └── object.py
    ├── exceptions/
    │   └── base.py
    ├── ports/
    │   ├── admin.py
    │   └── object_storage.py
    └── capabilities.py
```

### 🔌 Ports (Protocols)

Ports define the contract that storage drivers must implement.

Example:
```python
from typing import Protocol
from mine_spec.dto.admin import CreateUserInput, UserDTO

class UserAdminPort(ABC):
    @abstractmethod
    def set_bucket_quota(self, bucket: str, quota: str) -> List[BucketQuota]:
        pass

    @abstractmethod
    def get_bucket_quota(self, bucket: str) -> List[BucketQuota]:
        pass
```

Drivers implement these contracts:

```python
class S3AdminAdapter(UserAdminPort):
    ...
```

Using `Protocol` enables:

 - Structural typing
 - Strong mypy strict validation
 - Flexible adapter implementations
 - Clean Architecture compliance

---

### 📄 DTOs

DTOs are immutable typed models used as input/output boundaries.

Example:
```python
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class CreateUserInput:
    username: str
    password: str
```
DTOs are:

 - Immutable
 - Strongly typed
 - Provider-agnostic

---

### ⚠️ Exceptions

All exceptions are domain-level and provider-neutral.

Example hierarchy:

```python
class StorageError(Exception): ...
class AuthenticationError(StorageError): ...
class AuthorizationError(StorageError): ...
class ResourceAlreadyExists(StorageError): ...
class ResourceNotFound(StorageError): ...
class ConflictError(StorageError): ...
class ProviderUnavailable(StorageError): ...
class ProviderTimeout(StorageError): ...
```

Drivers are responsible for mapping provider-specific errors into these domain exceptions.
---

### 🧠 Capability Discovery (Optional)

Providers may support different features.

The package optionally defines capability enums to allow runtime discovery:

```python
class Capability(Enum):
    USERS = auto()
    GROUPS = auto()
    POLICIES = auto()
    NOTIFICATIONS = auto()
```

Drivers can expose:

```python
def supported_capabilities(self) -> set[Capability]:
    ...
```

This enables dynamic feature handling in higher layers.

---

### 📥 Installation

This package is not published to PyPI.

Install directly from GitHub using Poetry:

```TOML
mine-spec = { git = "https://github.com/<your-org>/mine-spec.git", tag = "v0.1.0" }
```

Or using pip with a release wheel:

```bash
pip install https://github.com/<your-org>/mine-spec/releases/download/v0.1.0/mine_spec-0.1.0-py3-none-any.whl
🔖 Versioning Policy
```

This package follows Semantic Versioning:
 - MAJOR → Breaking interface changes
 - MINOR → New capabilities or non-breaking additions
 - PATCH → Documentation or internal improvements

⚠️ Any signature change in a Port requires a MAJOR version bump.

---

### 🧪 Type Safety

The project is designed for:

 - Python 3.11+
 - mypy --strict
 - Strong typing guarantees across service-driver boundaries

---

### 🛡 License

MIT License

This package is intended for internal use but distributed under MIT.



