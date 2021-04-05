from typing import Optional

import fastapi
import uvicorn
from pydantic.error_wrappers import error_dict

api = fastapi.FastAPI()


@api.get('/')
def index():
    body = "<html>" \
           "<body style='padding: 10px;'>" \
           "<h1>Welcome to the API</h1>" \
           "<div>" \
           "Try it: <a href='/api/calculate?x=7&y=11'>/api/calculate?x=7&y=11</a>" \
           "</div>" \
           "</body>" \
           "</html>"

    return fastapi.responses.HTMLResponse(content=body)


@api.get('/api/calculate')
def calculate(x: int = 0, y: int = 0, z: Optional[int] = None):
    if z == 0 or z is None:
        # return fastapi.Response(content='{"error" :"Error: z cannot be zero."}',
        #                         media_type='application/json',
        #                         status_code=400, )

        # media_type='application/json' as a default at:
        return fastapi.responses.JSONResponse(content={"error": "Error: z cannot be zero."},
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
