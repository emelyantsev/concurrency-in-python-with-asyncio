import asyncpg
import asyncio


async def main():

    connection = await asyncpg.connect(host='127.0.0.1',
                                       port=5432,
                                       user='postgres',
                                       database='sample_db',
                                       password='1234')
    
    version = connection.get_server_version()
    
    print(f'Connected! Postgres version is {version}')
    
    await connection.close()


asyncio.run(main())