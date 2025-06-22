from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.security import get_current_user
from app.db.database import get_db
from app.models.models import User, Flower
from app.schemas.flower import FlowerCreate, FlowerUpdate, Flower as FlowerSchema

router = APIRouter()

@router.post("/", response_model=FlowerSchema)
async def create_flower(
    flower: FlowerCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    if not flower.name:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Flower name is required"
        )
    
    db_flower = Flower(
        name=flower.name,
        watering_intensity=flower.watering_intensity,
        light_level=flower.light_level,
        temperature_min=flower.temperature_range.min if flower.temperature_range else None,
        temperature_max=flower.temperature_range.max if flower.temperature_range else None,
        comment=flower.comment,
        owner_id=current_user.id
    )
    db.add(db_flower)
    db.commit()
    db.refresh(db_flower)
    return db_flower

@router.put("/{flower_id}", response_model=FlowerSchema)
async def update_flower(
    flower_id: int,
    flower: FlowerUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    if not flower.name:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Flower name is required"
        )
    
    db_flower = db.query(Flower).filter(Flower.id == flower_id).first()
    if not db_flower:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Flower not found"
        )
    
    if db_flower.owner_id != current_user.id:  # type: ignore
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to update this flower"
        )
    
    # Update attributes using setattr to avoid type issues
    setattr(db_flower, 'name', flower.name)
    setattr(db_flower, 'watering_intensity', flower.watering_intensity)
    setattr(db_flower, 'light_level', flower.light_level)
    setattr(db_flower, 'temperature_min', flower.temperature_range.min if flower.temperature_range else None)
    setattr(db_flower, 'temperature_max', flower.temperature_range.max if flower.temperature_range else None)
    setattr(db_flower, 'comment', flower.comment)
    
    db.commit()
    db.refresh(db_flower)
    return db_flower

@router.delete("/{flower_id}")
async def delete_flower(
    flower_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    db_flower = db.query(Flower).filter(Flower.id == flower_id).first()
    if not db_flower:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Flower not found"
        )
    
    if db_flower.owner_id != current_user.id:  # type: ignore
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to delete this flower"
        )
    
    db.delete(db_flower)
    db.commit()
    return {"message": "Flower deleted successfully"}

@router.get("/", response_model=List[FlowerSchema])
async def get_flowers(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    flowers = db.query(Flower).filter(Flower.owner_id == current_user.id).all()
    return flowers 