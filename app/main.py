from fastapi import FastAPI
# from app.middlewares import my_first_middleware, my_second_middleware
from app.middlewares import user_only_middleware, product_only_middleware


app = FastAPI()

app.middleware("http")(product_only_middleware)
app.middleware("http")(user_only_middleware)



@app.get("/users")
async def get_users():
  print("Endpoint :  Inside get_users endpoint")
  return {"data": "All Users data"}

@app.get("/products")
async def get_users():
  print("Endpoint :  Inside get_users endpoint")
  return {"data": "All Products data"}
  