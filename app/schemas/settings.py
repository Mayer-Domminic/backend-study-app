from pydantic import BaseModel

class SettingCreate(BaseModel):
    user_id: int
    grind: int
    problems_per_day: int
    noti_time: int
    days_of_week: str
    