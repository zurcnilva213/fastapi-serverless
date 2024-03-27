from sqlalchemy import select, func


async def count_total_records(base_query, session):
    base_query_cte = base_query.cte()
    total_query = select(func.count()).select_from(base_query_cte)
    total = (await session.execute(total_query)).scalar()
    return total
