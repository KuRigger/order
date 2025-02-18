from aiogram.fsm.state import StatesGroup, State

class UserForm(StatesGroup):
    name = State()
    email = State()
    birth_year = State()
    contact = State()
    
class AdminPanel(StatesGroup):
    auth = State()
    main = State()
    review = State()