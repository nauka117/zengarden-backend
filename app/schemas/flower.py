from pydantic import BaseModel
from typing import Optional

class TemperatureRange(BaseModel):
    min: Optional[float] = None
    max: Optional[float] = None

class FlowerBase(BaseModel):
    name: str
    watering_intensity: Optional[str] = None
    light_level: Optional[str] = None
    temperature_range: Optional[TemperatureRange] = None
    comment: Optional[str] = None

class FlowerCreate(FlowerBase):
    pass

class FlowerUpdate(FlowerBase):
    pass

class Flower(FlowerBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True 