from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from tensorflow import keras
from enum import Enum
import numpy as np
from app.ml import database, schemas
from app.ml.repository import user

router = APIRouter(
    prefix="/user",
    tags=['Users']
)

get_db = database.get_db
saved_model = keras.models.load_model('app/ml/model/model2.h5')

def rule(player, ia):
    if player == ia:  # 'Tie'
        return 'Tie'

    elif player == 0 and ia == 1:  # "IA Won"
        return "IA Won"

    elif player == 1 and ia == 2:  # "IA Won"
        return "IA Won"

    elif player == 2 and ia == 0:  # "IA Won"
        return "IA Won"

    else:  # "Player Won"
        return "Player Won"


def int_to_str(choice):
    if choice == 0:
        return 'Rock'
    elif choice == 1:
        return 'Paper'
    else:
        return 'Scissor'


def str_to_int(choice):
    if choice is Decision.rock:
        return 0
    elif choice is Decision.paper:
        return 1
    else:
        return 2


class Decision(str, Enum):
    rock = "Rock"
    paper = "Paper"
    scissor = "Scissor"

@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)


@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    return user.show(id, db)

@router.post("/predict")
async def predict_game(decision: Decision):
    player_choice = str_to_int(decision)

    mean_x = np.array([0.95, 0.32])
    std_x = np.array([0.83, 0.47])

    my_data = ([player_choice, 1] - mean_x) / std_x

    my_data = np.array(my_data).reshape(1, 2)

    predictions = saved_model(my_data)

    if predictions <= 0.66666666:
        choixIA = 0
    elif (predictions > 0.66666666) and (predictions <= 1.33333332):
        choixIA = 1
    else:
        choixIA = 2

    output = rule(player_choice, choixIA)

    return {"Prediction : ", int_to_str(choixIA), "Result : ", output}
