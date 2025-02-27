from fastapi import FastAPI

app = FastAPI()

toggle_flag = {"toggle": False}

@app.get("/show")
def show():
    current_status = toggle_flag["toggle"]
    response = {"toggle": current_status}
    toggle_flag["toggle"] = False
    return response

@app.get("/edit")
def edit():
    toggle_flag["toggle"] = not toggle_flag["toggle"]
    return {"toggle": toggle_flag["toggle"]}

@app.get("/")
def show_no_change():
    return {"toggle": toggle_flag["toggle"]}
