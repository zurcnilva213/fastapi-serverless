from pydantic import BaseModel
from enum import Enum
from typing import Optional, Union, List


class SortBy(str, Enum):
    ID = "id"
    NAME = "name"
    EMAIL = "email"
    TYPE = "type"
    TYPE_OF_OFFER = "type_of_offer"
    PHONE = "phone"
    TIME_ZONE = "time_zone"
    OPERATION_START = "operation_start"
    OPERATION_END = "operation_end"
    ACTIVE = "active"
    CREATED_AT = "createdAt"
    UPDATED_AT = "updatedAt"
    DECLINE_SERVICE = "decline_service"


class OrderBy(str, Enum):
    ASC = "asc"
    DESC = "desc"


class FilterField(str, Enum):
    NAME = "name"
    EMAIL = "email"
    TYPE = "type"
    WORKING_DAYS = "working_days"
    OPERATION_START = "operation_start"
    OPERATION_END = "operation_end"
    AFTER_HOURS = "after_hours"
    TYPE_OF_OFFER = "type_of_offer"
    PHONE = "phone"
    TIME_ZONE = "time_zone"
    ACTIVE = "active"
    CREATED_AT = "createdAt"
    UPDATED_AT = "updatedAt"
    DECLINE_SERVICE = "decline_service"


class FilterBy(BaseModel):
    field: Optional[FilterField]
    value: Optional[Union[str, List[str], bool]]
