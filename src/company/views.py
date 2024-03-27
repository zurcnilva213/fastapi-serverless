from fastapi import APIRouter, Depends, HTTPException, Query, Body
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from db.config import get_session, auth_required
from models import Company
from .schemas import CompanyBase
from typing import Optional, List

from .service import apply_filter, apply_sort, apply_search
from .types import SortBy, FilterBy, OrderBy
from utils.query import count_total_records

router = APIRouter(prefix="/company", tags=["Company"], dependencies=[Depends(auth_required)],
                   responses={404: {"description": "Not found"}})


@router.post("")
async def create_company(obj: CompanyBase, session: AsyncSession = Depends(get_session)):
    company = Company(**obj.dict())
    session.add(company)
    await session.commit()
    return company


@router.patch("")
async def list_companies(
        page: int = Query(1, ge=1),
        page_size: int = Query(10, ge=1, le=100),
        search: Optional[str] = Query(None),
        sort_by: Optional[SortBy] = Query(None),
        order_by: Optional[OrderBy] = Query(None),
        filter_by: Optional[List[FilterBy]] = Body(None),
        session: AsyncSession = Depends(get_session)):
    offset = (page - 1) * page_size
    query = select(Company)
    if filter_by:
        for filter_item in filter_by:
            if filter_item.field and filter_item.value:
                query = apply_filter(query, filter_item.field, filter_item.value)
    if search:
        query = apply_search(query, search)

    total_count = await count_total_records(query, session)

    if sort_by:
        query = apply_sort(query, sort_by, order_by)
    # Get the total count

    query = query.offset(offset).limit(page_size)
    companies = (await session.execute(query)).scalars().all()
    return {"total_count": total_count, "data": companies}


@router.get("/{company_id}")
async def get_company(company_id: int, session: AsyncSession = Depends(get_session)):
    company = await session.get(Company, company_id)
    if company is None:
        raise HTTPException(status_code=404, detail="Company not found")
    return company


# Update a company by ID
@router.put("/{company_id}")
async def update_company(company_id: int, obj: CompanyBase, session: AsyncSession = Depends(get_session)):
    company = await session.get(Company, company_id)
    if company is None:
        raise HTTPException(status_code=404, detail="Company not found")
    for field, value in obj.dict().items():
        setattr(company, field, value)
    await session.commit()
    return company


# Delete a company by ID
@router.delete("/{company_id}")
async def delete_company(company_id: int, session: AsyncSession = Depends(get_session)):
    company = await session.get(Company, company_id)
    if company is None:
        raise HTTPException(status_code=404, detail="Company not found")
    await session.delete(company)
    await session.commit()
    return {"message": "Company deleted successfully"}
