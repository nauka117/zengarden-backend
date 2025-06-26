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

    @classmethod
    def from_orm(cls, obj):
        # Собираем temperature_range из полей ORM-модели
        temperature_range = None
        if hasattr(obj, 'temperature_min') and hasattr(obj, 'temperature_max'):
            if obj.temperature_min is not None or obj.temperature_max is not None:
                temperature_range = TemperatureRange(
                    min=obj.temperature_min,
                    max=obj.temperature_max
                )
        return cls(
            id=obj.id,
            owner_id=obj.owner_id,
            name=obj.name,
            watering_intensity=obj.watering_intensity,
            light_level=obj.light_level,
            temperature_range=temperature_range,
            comment=obj.comment
        )

    class Config:
        from_attributes = True 