import asyncio
import asyncpg


async def main():
    connection = await asyncpg.connect(host='127.0.0.1',
                                       port=5432,
                                       user='postgres',
                                       database='products',
                                       password='1234')

    query = 'SELECT product_id, product_name FROM product'
    async with connection.transaction():
        async for product in connection.cursor(query):
            print(product)
        # res = await connection.fetch(query)
        # print(type(res))
        # print(len(res))
        # print(res)

    await connection.close()


asyncio.run(main())