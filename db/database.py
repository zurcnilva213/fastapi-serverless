import logging
import contextlib

from fastapi import status, HTTPException
from sqlalchemy.exc import (
    IntegrityError, 
    ProgrammingError,
    OperationalError
)
from sqlalchemy.pool import AsyncAdaptedQueuePool
from sqlalchemy import text, MetaData
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.engine.base import Connection

from core.settings import Settings


settings = Settings()
metadata = MetaData()


class DuplicatedDatabaseException(Exception):
    pass


async def init_database():
    # STEP 1: Check for duplication and create database
    dbname = settings.database_name
    database_url = settings.database_url
    database_url = database_url.replace('<database_name>', '')
    engine = create_async_engine(database_url)
    async with engine.connect() as conn:
        sql = (
            "SELECT SCHEMA_NAME "
            "FROM INFORMATION_SCHEMA.SCHEMATA "
            "WHERE SCHEMA_NAME = :db "
        )
        row = await conn.execute(text(sql), {'db': dbname})
        row = row.first() 
        if not row:
            # Create Database
            await conn.execute(text('CREATE DATABASE ' + dbname))
    
    # STEP 2: Generate tables
    database_url = settings.database_url
    database_url = database_url.replace('<database_name>', dbname)
    engine = create_async_engine(database_url, echo=True)
    async with engine.connect() as conn:
        await conn.run_sync(metadata.create_all)

    await engine.dispose()
    return True


@contextlib.asynccontextmanager
async def get_db():
    conn: Connection = None
    engine = None
    try:
        dburl = settings.database_url
        pool_settings = {
            "poolclass": AsyncAdaptedQueuePool,
            "pool_size": 5,
            "pool_pre_ping": True,
            "max_overflow": 45
        }
        engine = create_async_engine(dburl, **pool_settings)
        conn = await engine.connect()
        yield conn
    except (ProgrammingError, IntegrityError, OperationalError) as e:
        if conn:
            await conn.rollback()
        logging.error(str(e))
        raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Unable to connect to server"  # Get a readable error message
            )
    except Exception as e:
        if conn:
            await conn.rollback()
        logging.error(str(e))
        raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Unable to connect to server"  # Get a readable error message
            )
    else:
        if conn:
            await conn.commit()
    finally:
        if conn:
            await conn.close()
        if engine:
            await engine.dispose()


@contextlib.asynccontextmanager
async def get_common_db():
    conn: Connection = None
    engine = None
    try:
        dburl = settings.database_url
        dburl = dburl.replace('<database_name>', 'common')
        pool_settings = {
            "poolclass": AsyncAdaptedQueuePool,
            "pool_size": 5,
            "pool_pre_ping": True,
            "max_overflow": 45
        }
        engine = create_async_engine(dburl, **pool_settings)
        conn = await engine.connect()
        yield conn
    except (ProgrammingError, IntegrityError, OperationalError) as e:
        if conn:
            await conn.rollback()
        logging.error(str(e))
        raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(e.orig.args[1]),  # Get a readable error message
            )
    except Exception as e:
        if conn:
            await conn.rollback()
        logging.error(str(e))
        raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(e),  # Get a readable error message
            )
    else:
        if conn:
            await conn.commit()
    finally:
        if conn:
            await conn.close()
        if engine:
            await engine.dispose()


@contextlib.asynccontextmanager
async def get_db_auth():
    db = settings.database_name_auth
    conn: Connection = None
    engine = None
    try:
        dburl = settings.database_url_auth
        dburl = dburl.replace('<database_name>', db)
        pool_settings = {
            'poolclass': AsyncAdaptedQueuePool,
            'pool_size': 50,
            'pool_pre_ping': True,
            'max_overflow': 50
        }
        engine = create_async_engine(dburl, **pool_settings)
        conn = await engine.connect()
        yield conn
    except (ProgrammingError, IntegrityError, OperationalError) as e:
        if conn:
            await conn.rollback()
        logging.error(str(e))
        raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(e.orig.args[1]),  # Get a readable error message
            )
    except Exception as e:
        if conn:
            await conn.rollback()
        logging.error(str(e))
        raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(e),  # Get a readable error message
            )
    else:
        if conn:
            await conn.commit()
    finally:
        if conn:
            await conn.close()
        if engine:
            await engine.dispose()
