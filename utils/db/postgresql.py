from typing import Union

import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool

from data import config


class Database:
    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create(self):
        self.pool = await asyncpg.create_pool(
            user=config.DB_USER,
            password=config.DB_PASS,
            host=config.DB_HOST,
            database=config.DB_NAME,
        )

    async def execute(
            self,
            command,
            *args,
            fetch: bool = False,
            fetchval: bool = False,
            fetchrow: bool = False,
            execute: bool = False,
    ):
        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
                return result

# ============================= KLINIKALAR JADVALI =============================
    async def create_table_company(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Company (
        id SERIAL PRIMARY KEY,
        created_at DATE DEFAULT CURRENT_NOW(),
        fullname VARCHAR(1000) NULL,
        address VARCHAR(1000) NULL,
        landmark VARCHAR(1000) NULL,
        work_day VARCHAR(255) NULL,
        work_time VARCHAR(255) NULL,
        latitude FLOAT NULL,
        longitude FLOAT NULL,
        image FILE NULL,
        description VARCHAR(4000)
        phone_one VARCHAR(50)
        phone_two VARCHAR(50)
        );
        """
        await self.execute(sql, execute=True)

# ============================= MUTAXASSISLIK VA HIZMATLAR JADVALI =============================
    async def create_table_referring_and_services(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Doctors_Services (
        id SERIAL PRIMARY KEY,
        created_at DATE DEFAULT CURRENT_NOW(),
        referring VARCHAR(255) NULL,
        services VARCHAR(255) NULL,
        company VARCHAR(255) NULL,
        region VARCHAR(255) NULL,
        city VARCHAR(255) NULL,
        district VARCHAR(255) NULL        
        );
        """
        await self.execute(sql, execute=True)

# ============================= KLINIKA HODIMLARI JADVALI =============================
    async def create_table_employees(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Employees (
        id SERIAL PRIMARY KEY,
        created_at DATE DEFAULT CURRENT_NOW(),
        username VARCHAR(255) NULL,
        fullname VARCHAR(255) NULL,
        phone_one VARCHAR(20) NULL,
        phone_two VARCHAR(20) NULL,
        gender VARCHAR(20) NULL,
        age INTEGER NULL,
        job VARCHAR(100) NULL,
        role VARCHAR(100) NULL        
        );
        """
        await self.execute(sql, execute=True)

    # ============================= FOYDALANUVCHILAR JADVALI =============================
    async def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Users (
        id SERIAL PRIMARY KEY,
        created_at DATE DEFAULT CURRENT_NOW(),
        telegram_id BIGINT NOT NULL UNIQUE,
        username VARCHAR(50) NULL,
        fullname VARCHAR(50) NULL,
        phone_one VARCHAR(20) NULL,
        phone_two VARCHAR(20) NULL,
        gender VARCHAR(20) NULL,
        age INTEGER NULL,
        latitude FLOAT NULL,
        longitude FLOAT NULL        
        );
        """
        await self.execute(sql, execute=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join(
            [f"{item} = ${num}" for num, item in enumerate(parameters.keys(), start=1)]
        )
        return sql, tuple(parameters.values())

    async def add_user(self, telegram_id):
        sql = "INSERT INTO Users (telegram_id) VALUES($1) returning *"
        return await self.execute(sql, telegram_id, fetchrow=True)

    async def select_all_users(self):
        sql = "SELECT * FROM Users"
        return await self.execute(sql, fetch=True)

    async def select_user(self, telegram_id):
        sql = "SELECT * FROM Users WHERE telegram_id=$1"
        return await self.execute(sql, telegram_id, fetchrow=True)

    async def count_users(self):
        sql = "SELECT COUNT(*) FROM Users"
        return await self.execute(sql, fetchval=True)

    async def delete_user(self, telegram_id):
        await self.execute("DELETE FROM Users WHERE telegram_id=$1", telegram_id, execute=True)

    async def delete_users(self):
        await self.execute("DELETE FROM Users WHERE TRUE", execute=True)

    async def drop_table_users(self):
        await self.execute("DROP TABLE Users", execute=True)
