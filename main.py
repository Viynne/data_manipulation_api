from fastapi import FastAPI


app = FastAPI()


@app.get("/Dashboard/metrics")
async def dashing() -> dict:
    return {
        "Dashboards": [
            "Sales",
            "Inventory",
            "Procurement"
        ]
    }
