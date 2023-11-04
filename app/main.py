from fastapi import FastAPI, Request

from app.tokenFeature import preprocess  # Docker

# from tokenFeature import preprocess  # Local

app = FastAPI()

@app.get('/hello')
def hello():
      return {"name":"TOCK"}


@app.get('/api/cleantext')
async def read_str(request : Request):
      item = await request.json()
      item_str = item['text']
      text = preprocess(item_str)

      return {
                  "text":text
             }