from typing import Optional

import fastapi
import uvicorn

api = fastapi.FastAPI()


@api.get('/api/calculate')
def calculate(x: int = 0, y: int = 0, z: Optional[int] = None):
    if z == 0:
        return fastapi.Response(content='{"error" :"Error: z cannot be zero."}',
                                media_type='application/json',
                                status_code=400, )
        v = x + y

        if z is not None:
            v += z

        return {
            'x': x,
            'y': y,
            'z': z,
            'value': v
        }

    # print("hello fastapi")


uvicorn.run(api, port=8000, host='127.0.0.3')
