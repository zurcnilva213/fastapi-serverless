from core.schemas import DefaultModel
from typing import List, Optional


class CompanyBase(DefaultModel):
    name: str
    email: str
    type: str
    type_of_offer: str
    free_service: str
    service_type: str
    service_area: str
    about_us: str
    phone: str
    time_zone: str
    working_days: List[str]
    zip_codes: List[str]
    operation_start: str
    operation_end: str
    after_hours: bool
    after_hours: Optional[bool]
    same_day_appointment: bool
    auto_reply: bool
    active: bool
    notes: str
    decline_service: Optional[str]
