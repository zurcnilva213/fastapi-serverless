from sqlalchemy import func, or_
from models import Company, Podium
from src.company.types import SortBy, OrderBy, FilterField


def apply_search(query, search):
    search_filters = []
    search_filters.append(Company.name.ilike(f"%{search}%"))
    search_filters.append(Company.type.ilike(f"%{search}%"))
    search_filters.append(Company.email.ilike(f"%{search}%"))
    search_filters.append(Company.free_service.ilike(f"%{search}%"))
    search_filters.append(Company.service_type.ilike(f"%{search}%"))
    search_filters.append(Company.type_of_offer.ilike(f"%{search}%"))
    search_filters.append(Company.about_us.ilike(f"%{search}%"))
    search_filters.append(Company.phone.ilike(f"%{search}%"))
    search_filters.append(Company.time_zone.ilike(f"%{search}%"))
    search_filters.append(Company.operation_end.ilike(f"%{search}%"))
    search_filters.append(Company.operation_start.ilike(f"%{search}%"))
    search_filters.append(Company.working_days.ilike(f"%{search}%"))
    search_filters.append(Company.zip_codes.ilike(f"%{search}%"))
    search_filters.append(Company.notes.ilike(f"%{search}%"))
    search_filters.append(Company.id.ilike(f"%{search}%"))
    search_filters.append(Company.decline_service.ilike(f"%{search}%"))
    query = query.filter(or_(*search_filters))
    return query


def apply_filter(query, filter_by, filter_value):
    if filter_by == FilterField.NAME:
        query = query.filter(func.lower(Company.name).contains(func.lower(filter_value)))
    if filter_by == FilterField.EMAIL:
        query = query.filter(func.lower(Company.email).contains(func.lower(filter_value)))
    if filter_by == FilterField.TYPE:
        query = query.filter(func.lower(Company.type).contains(func.lower(filter_value)))
    if filter_by == FilterField.AFTER_HOURS:
        filter_value = filter_value == 'True'
        query = query.filter(Company.after_hours == filter_value)
    if filter_by == FilterField.OPERATION_START:
        query = query.filter(func.lower(Company.operation_start).contains(func.lower(filter_value)))
    if filter_by == FilterField.OPERATION_END:
        query = query.filter(func.lower(Company.operation_end).contains(func.lower(filter_value)))
    if filter_by == FilterField.WORKING_DAYS:
        query = query.filter(func.lower(Company.working_days).contains(func.lower(filter_value)))
    if filter_by == FilterField.TYPE_OF_OFFER:
        query = query.filter(func.lower(Company.type).contains(func.lower(filter_value)))
    if filter_by == FilterField.PHONE:
        query = query.filter(func.lower(Company.phone).contains(func.lower(filter_value)))
    if filter_by == FilterField.TIME_ZONE:
        query = query.filter(func.lower(Company.time_zone).contains(func.lower(filter_value)))
    if filter_by == FilterField.DECLINE_SERVICE:
        query = query.filter(func.lower(Company.decline_service).contains(func.lower(filter_value)))
    if filter_by == FilterField.ACTIVE:
        filter_value = filter_value == 'True'
        query = query.filter(Company.active == filter_value)
    if filter_by == FilterField.CREATED_AT:
        query = query.filter(Company.createdAt == filter_value)
    if filter_by == FilterField.CREATED_AT:
        query = query.filter(Company.updatedAt == filter_value)

    return query


def apply_sort(query, sort_by, order_by):
    if sort_by == SortBy.ID:
        if order_by == OrderBy.ASC:
            query = query.order_by(Company.id.asc())
        else:
            query = query.order_by(Company.id.desc())

    if sort_by == SortBy.NAME:
        if order_by == OrderBy.ASC:
            query = query.order_by(Company.name.asc())
        else:
            query = query.order_by(Company.name.desc())

    if sort_by == SortBy.EMAIL:
        if order_by == OrderBy.ASC:
            query = query.order_by(Company.email.asc())
        else:
            query = query.order_by(Company.email.desc())

    if sort_by == SortBy.TYPE:
        if order_by == OrderBy.ASC:
            query = query.order_by(Company.type.asc())
        else:
            query = query.order_by(Company.type.desc())

    if sort_by == SortBy.TYPE_OF_OFFER:
        if order_by == OrderBy.ASC:
            query = query.order_by(Company.type_of_offer.asc())
        else:
            query = query.order_by(Company.type_of_offer.desc())

    if sort_by == SortBy.PHONE:
        if order_by == OrderBy.ASC:
            query = query.order_by(Company.phone.asc())
        else:
            query = query.order_by(Company.phone.desc())

    if sort_by == SortBy.DECLINE_SERVICE:
        if order_by == OrderBy.ASC:
            query = query.order_by(Company.decline_service.asc())
        else:
            query = query.order_by(Company.decline_service.desc())

    if sort_by == SortBy.OPERATION_START:
        if order_by == OrderBy.ASC:
            query = query.order_by(Company.operation_start.asc())
        else:
            query = query.order_by(Company.operation_start.desc())

    if sort_by == SortBy.OPERATION_END:
        if order_by == OrderBy.ASC:
            query = query.order_by(Company.operation_end.asc())
        else:
            query = query.order_by(Company.operation_end.desc())

    if sort_by == SortBy.ACTIVE:
        if order_by == OrderBy.ASC:
            query = query.order_by(Company.active.asc())
        else:
            query = query.order_by(Company.active.desc())

    if sort_by == SortBy.CREATED_AT:
        if order_by == OrderBy.ASC:
            query = query.order_by(Company.createdAt.asc())
        else:
            query = query.order_by(Company.createdAt.desc())

    if sort_by == SortBy.UPDATED_AT:
        if order_by == OrderBy.ASC:
            query = query.order_by(Company.updatedAt.asc())
        else:
            query = query.order_by(Company.updatedAt.desc())

    return query
