from fastapi import Request


# Creating Middleware

# First Middleware
# async def my_first_middleware(request: Request, call_next):
#   print("2 Middleware: Before processing the request")
#   print(f"Request:{request.method} {request.url}")
  
#   response = await call_next(request)
  
#   print("Middleware: After processing the request, Before returning  the response")
#   print(f"Response status code :{response.status_code}")
  
  
#   return response


# Middleware for User Route
async def user_only_middleware(request: Request, call_next):
  if request.url.path.startswith("/users"):
    print("User Middleware: Before processing the request")
    response = await call_next(request)
    print("User Middleware: After processing the request, Before returning  the response")
    print(f"Response status code :{response.status_code}")
    return response
  else:
    print(f"User Middleware: Skipping middleware for {request.url.path}")
    response = await call_next(request)
    return response
    
    
  
  
  
  


# Second Middleware
# async def my_second_middleware(request: Request, call_next):
#   print("2 Middleware: Before processing the request")
#   print(f"Request:{request.method} {request.url}")
  
#   response = await call_next(request)
  
#   print("Middleware: After processing the request, Before returning  the response")
#   print(f"Response status code :{response.status_code}")
  
  
#   return response
# Second Middleware
async def product_only_middleware(request: Request, call_next):
    if request.url.path.startswith("/products"):
      print("Product Middleware: Before processing the request")
      response = await call_next(request)
      print(" Product Middleware: After processing the request, Before returning  the response")
      print(f"Response status code :{response.status_code}")
      return response
    else:
      print(f"Prdouct Middleware: Skipping middleware for {request.url.path}")
      response = await call_next(request)
      return response