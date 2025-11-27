from fastapi import Request


# Creating Middleware

# First Middleware
async def my_first_middleware(request: Request, call_next):
  print("2 Middleware: Before processing the request")
  print(f"Request:{request.method} {request.url}")
  
  response = await call_next(request)
  
  print("Middleware: After processing the request, Before returning  the response")
  print(f"Response status code :{response.status_code}")
  
  
  return response


# Second Middleware
async def my_second_middleware(request: Request, call_next):
  print("2 Middleware: Before processing the request")
  print(f"Request:{request.method} {request.url}")
  
  response = await call_next(request)
  
  print("Middleware: After processing the request, Before returning  the response")
  print(f"Response status code :{response.status_code}")
  
  
  return response