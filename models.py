import json
from typing import List
from deepdiff import DeepDiff, DeepHash


class User:
    def __init__(
        self, user_id: str, email: str, first_name: str, last_name: str, role: str
    ) -> None:
        self.user_id = user_id
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.role = role

    def __hash__(self) -> int:
        return hash(self.email)

    def __eq__(self, __o: object) -> bool:
        if self.__class__ != __o.__class__:
            return False
        other: User = __o

        return self.email == other.email


class Group:

    GROUP_TYPE_MANAGED_GROUP = "MANAGED_GROUP"
    GROUP_TYPE_USER_DEFINED = ""

    def __init__(
        self,
        name: str,
        tags: List[str] = None,
        group_type: str = None,
        cloud_type: str = None,
        cloud_data: dict = None,
    ) -> None:
        self.name = name
        self.tags = [] if tags is None else tags
        self._tags = tuple() if tags is None else tuple(tags)
        self.group_type = group_type
        self.cloud_type = cloud_type
        self.cloud_data = cloud_data

    def __hash__(self) -> int:
        return hash(self.name)

    def __eq__(self, __o: object) -> bool:
        if self.__class__ != __o.__class__:
            return False
        other: Group = __o

        return self.name == other.name and self._tags == other._tags

    def __str__(self) -> str:
        fields = vars(self)
        del fields["_tags"]
        return json.dumps(fields, indent=4)


class CommunicationSettings:
    def __init__(
        self,
        channel: str,
        enabled: bool,
        filter: dict,
        configuration: dict,
    ) -> None:
        self.channel = channel
        self.enabled = enabled
        self.filter = filter
        self.configuration = configuration
        self._obj = {
            "channel": channel,
            "filter": filter,
            "configuration": configuration,
        }

    def __hash__(self) -> int:
        dh = DeepHash(self._obj)[self._obj]
        return hash(dh)

    def __eq__(self, __o: object) -> bool:
        diff = DeepDiff(self._obj, __o._obj, ignore_order=True)
        return len(diff) == 0

    def __str__(self) -> str:
        fields = vars(self)
        del fields["_obj"]
        return json.dumps(fields, indent=4)
