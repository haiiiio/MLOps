from fastapi import FastAPI

app = FastAPI()

def mock_score(surface: int):
    #scorer fct logic goes here
    return 1


@app.get("/features/{surface}")
def calculate_surface(surface: int):
    score = mock_score(surface)
    return {"Square Footage": surface, "Score": score}

@app.get("/")
def home():
    return {"Welcome"}
