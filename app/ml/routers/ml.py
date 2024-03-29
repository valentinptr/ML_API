from enum import Enum

import numpy as np
from fastapi import APIRouter, Depends, status
from tensorflow import keras
from pydantic import BaseModel

from .. import database, schemas, oauth2

router = APIRouter(
    prefix="/ml",
    tags=['Access to model']
)

get_db = database.get_db
saved_model = keras.models.load_model('ml/model/model2.h5')


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
    if choice == "Rock":
        return 0
    elif choice == "Paper":
        return 1
    else:
        return 2


class Decision(BaseModel):
    choice: str


@router.post("/predict")
async def predict_game(decision: Decision):
    player_choice = str_to_int(decision.choice)

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

    return {"Prediction": int_to_str(choixIA), "Result": output}
