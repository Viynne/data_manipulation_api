from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from routes.sales_route import route_sales


app = FastAPI()

app.include_router(route_sales, prefix="/dashboard")

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/dashboard")
async def dashing() -> dict:
    return {
        "Dashboards": [
            "Sales"
        ]
    }


