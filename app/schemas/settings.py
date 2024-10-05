from pydantic import BaseModel
from typing import Optional

class SettingBase(BaseModel):
    user_id: int
    grind: int
    problems_per_day: int
    noti_time: int
    days_of_week: str

class SettingCreate(SettingBase):
    pass

class Setting(SettingBase):
    setting_id: int

    class Config:
        orm_mode = True
