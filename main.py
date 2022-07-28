from helper import send_index

print('started')

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/index")
async def give_recommendation(index:int=0):
	rs=send_index(index)
	import json
	return {"result":rs}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

