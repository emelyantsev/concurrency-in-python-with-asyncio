from aiohttp import web
from datetime import datetime
from aiohttp.web_request import Request
from aiohttp.web_response import Response

import os
import threading

routes = web.RouteTableDef()


@routes.get('/info')  
async def info(request: Request) -> Response:
    today = datetime.today()

    pid = os.getpid()
    tid = threading.get_native_id()

    result = { 'date' : {
                        'month': today.month,
                        'day': today.day,
                        'time': str(today.time())
                },

                'pid' : pid,
                'tid' : tid
    }

    return web.json_response(result)  


async def my_web_app():
        
    app = web.Application()  
    app.add_routes(routes)
    return app
