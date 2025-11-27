from fastapi import FastAPI
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.middleware.cors import CORSMiddleware
# from app.middlewares import my_first_middleware, my_second_middleware
from app.middlewares import user_only_middleware, product_only_middleware


app = FastAPI()

# Custom Middleware
# app.middleware("http")(product_only_middleware)
# app.middleware("http")(user_only_middleware)

# Built-In Middleware
app.middleware("http")(HTTPSRedirectMiddleware)

app.add_middleware(TrustedHostMiddleware, allowed_hosts=["localhost", "127.0.0.1"])

@app.get("/users")
async def get_users():
  print("Endpoint :  Inside get_users endpoint")
  return {"data": "All Users data"}

@app.get("/products")
async def get_users():
  print("Endpoint :  Inside get_users endpoint")
  return {"data": "All Products data"}
  