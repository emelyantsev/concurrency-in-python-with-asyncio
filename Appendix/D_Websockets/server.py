import aiohttp
from aiohttp import web

async def testhandle(request):
    return web.Response(text='Test handle')

async def websocket_handler(request):

    print('Websocket connection starting')
    ws = web.WebSocketResponse()
    
    await ws.prepare(request)
    print('Websocket connection ready')

    async for msg in ws:
        print(msg)
        if msg.type == aiohttp.WSMsgType.TEXT:
            print(msg.data)
            if msg.data == 'close':
                await ws.close()
            else:
                await ws.send_str(msg.data + '/answer')

    print('Websocket connection closed')
    return ws


def main():

    app = aiohttp.web.Application()
    app.router.add_route('GET', '/', testhandle)
    app.router.add_route('GET', '/ws', websocket_handler)
    aiohttp.web.run_app(app, host='0.0.0.0', port=8080)


if __name__ == '__main__':
    main()