import asyncio
import websockets
import os
from echo import echo

if __name__=='__main__':
    start_server = websockets.serve(echo, "", 1234)

    print("WebSockets echo server starting", flush=True)
    asyncio.get_event_loop().run_until_complete(start_server)

    print("WebSockets echo server running", flush=True)
    asyncio.get_event_loop().run_forever()