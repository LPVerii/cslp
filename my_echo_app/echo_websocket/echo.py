import websockets 

async def echo(websocket, path):
    async for message in websocket:
        print ("Received and echoing message: "+message, flush=True)
        await websocket.send(message)
