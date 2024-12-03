from dataclasses import dataclass


@dataclass(frozen=True)
class IEntity:
    id: int
