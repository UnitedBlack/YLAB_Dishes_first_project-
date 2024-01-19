from fastapi import APIRouter, Depends, Response
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from database import get_db
from services import service_menu as RestaurantService
from dto import dto_menu as RestaurantDTO
from uuid import UUID
from models.models_restaurant import Menu

router = APIRouter()
database_service = RestaurantService.DbService(Menu)


@router.post("/menus", tags=["menu_getter"])
async def create_menu(data: RestaurantDTO.Menu = None, db: Session = Depends(get_db)):
    menu_creation = database_service.create_menu(data, db)
    if not menu_creation:
        return Response(content="Failed to create menu", status_code=400)
    json_compatible_item_data = jsonable_encoder(menu_creation)
    return JSONResponse(content=json_compatible_item_data, status_code=201)


@router.get("/menus/{id}", tags=["specified_menu"])
async def get_menu(id: UUID, db: Session = Depends(get_db)):
    specified_menu = database_service.get_value_menu(id, db)
    if not specified_menu:
        return JSONResponse(content={"detail": "menu not found"}, status_code=404)
    return specified_menu


@router.get("/menus", tags=["all_menus"])
async def get_all_menus(db: Session = Depends(get_db)):
    return database_service.get_all_menus(db)


@router.patch("/menus/{id}", tags=["change_menu_data"])
async def change_menu_data(
    id: UUID, data: RestaurantDTO.Menu = None, db: Session = Depends(get_db)
):
    update_menu = database_service.update_menu(data, db, id)
    json_compatible_item_data = jsonable_encoder(update_menu)
    return JSONResponse(content=json_compatible_item_data, status_code=200)


@router.delete("/menus/{id}", tags=["delete_menus"])
async def delete(id: UUID, db: Session = Depends(get_db)):
    return database_service.remove_menu(db, id)
