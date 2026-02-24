from fastapi import FastAPI
from fastapi.responses import FileResponse

from models import CalcRequest, User, UserAge, Feedback

app = FastAPI()


# 1.2

@app.get("/")
def index():
    return FileResponse("index.html")

# 1.1 
@app.get("/json")
def root_json():
    return {"message": "Добро пожаловать в моё приложение FastAPI!"}
    

# 1.3
@app.post("/calculate")
def calculate(data: CalcRequest):
    return {"result": data.num1 + data.num2}

# 1.4 
user = User(name="Ваше Имя и Фамилия", id=1)

@app.get("/users")
def get_user():
    return user

# 1.5
@app.post("/user")
def user_is_adult(u: UserAge):
    return {"name": u.name, "age": u.age, "is_adult": u.age >= 18}

# 2.1 + 2.2*
feedbacks: list[Feedback] = []

@app.post("/feedback")
def create_feedback(data: Feedback):
    feedbacks.append(data)
    return {"message": f"Спасибо, {data.name}! Ваш отзыв сохранён."}