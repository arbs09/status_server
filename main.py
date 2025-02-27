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
    global toggle_flag
    toggle_flag["toggle"] = True
    return {"toggle": toggle_flag["toggle"]}

@app.get("/")
def show_no_change():
    return {"toggle": toggle_flag["toggle"]}
