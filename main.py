import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

# Initialize fast-api
app = FastAPI()

# We gonna creates some basic CRUD option,
# here we define a list, which will contain list of nerds people ;)
nerds = []


# Define a class for reading post request
class People(BaseModel):
    name: str
    age: str
    address: str
    isNerd = False


# A sample of http request
@app.get('/')
def index():
    return {'root': 'project is started'}


@app.get('/nerd')
def list():
    return nerds


@app.post('/nerd')
def create(nerd: People):
    nerds.append(nerd.dict())
    return {'success': 'Nerd is created!'}


@app.delete('/nerd/{nerd_id}')
def delete(nerd_id: int):
    nerds.pop(nerd_id - 1)
    return {"success": f'Successfully deleted ::  {nerd_id}'}


# Run applications
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
