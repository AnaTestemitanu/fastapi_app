from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from app.routers import analysis

# Create FastAPI instance
app = FastAPI()

# Include analysis router
app.include_router(analysis.router)

# Exception handler for HTTPExceptions
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    # Return JSONResponse with appropriate status code and message
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail},
    )