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

# ============================= KLINIKALAR VA TIBBIY MARKAZLAR JADVALI =============================
    async def create_table_company(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Company (
        id SERIAL PRIMARY KEY,
        created_at DATE DEFAULT CURRENT_DATE,
        name VARCHAR(1000) NULL,
        address VARCHAR(1000) NULL,
        landmark VARCHAR(1000) NULL,
        work_day VARCHAR(255) NULL,
        work_time VARCHAR(255) NULL,
        latitude FLOAT NULL,
        longitude FLOAT NULL,
        image TEXT NULL,
        description VARCHAR(4000) NULL,
        phone_one VARCHAR(50) NULL,
        phone_two VARCHAR(50) NULL 
        );
        """
        await self.execute(sql, execute=True)

    async def add_company(self, name, image):
        sql = "INSERT INTO Company (name, image) VALUES($1, $2) returning *"
        return await self.execute(sql, name, image, fetchrow=True)

    async def select_all_clinics(self):
        sql = "SELECT * FROM Company ORDER BY name"
        return await self.execute(sql, fetch=True)

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
        telegram_id BIGINT NOT NULL UNIQUE,
        username VARCHAR(50) NULL,
        fullname VARCHAR(50) NULL,
        phone_one VARCHAR(20) NULL,
        phone_two VARCHAR(20) NULL,
        gender VARCHAR(20) NULL,
        age INTEGER NULL,
        latitude FLOAT NULL,
        longitude FLOAT NULL,
        get_doctor TEXT NULL,
        complaint VARCHAR(4000) NULL        
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

    # ============================= FOYDALANUVCHILAR SHIKOYATLARI JADVALI =============================
    async def create_table_complaint(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Complaint (
        id SERIAL PRIMARY KEY,
        checked_date DATE DEFAULT CURRENT_DATE,                   
        telegram_id BIGINT NOT NULL UNIQUE,        
        gender_doctor TEXT NULL,
        type_doctor TEXT NULL,        
        complaint VARCHAR(4000) NULL        
        );
        """
        await self.execute(sql, execute=True)

    async def add_complaint(self, telegram_id, gender_doctor):
        sql = "INSERT INTO Complaint (telegram_id, gender_doctor) VALUES($1, $2) returning id"
        return await self.execute(sql, telegram_id, gender_doctor, fetchrow=True)

    async def update_doctor_complaint(self, type_doctor, id_):
        sql = "UPDATE Complaint SET type_doctor=$1 WHERE id=$2"
        return await self.execute(sql, type_doctor, id_, execute=True)

    async def update_user_complaint(self, complaint, id_):
        sql = "UPDATE Complaint SET complaint=$1 WHERE id=$2"
        return await self.execute(sql, complaint, id_, execute=True)

    async def select_complaint_by_id(self, id_):
        sql = f"SELECT * FROM Complaint WHERE id='{id_}'"
        return await self.execute(sql, fetchrow=True)

    async def delete_complaint_by_id(self, id_):
        await self.execute(f"DELETE FROM Complaint WHERE id='{id_}'", execute=True)

    async def drop_table_complaint(self):
        await self.execute("DROP TABLE Complaint", execute=True)
