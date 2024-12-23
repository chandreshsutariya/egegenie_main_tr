from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from src.pdfengine.setup.genie import Genie


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://your-domain.com",
]

# Add CORSMiddleware to the FastAPI app.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allows all origin
    allow_credentials=True,  # Allow credentials (cookies, authorization headers)
    allow_methods=["*"],     # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],     # Allows all custom headers
)

a=""
m="gpt-4o-mini"
G = Genie(open_api_key_=a, \
            model_=m, \
            file_path="/Users/apple/cjs/egegenie_main/libraries/test_10_12_24.pdf"
)

class Message(BaseModel):
    user_says: str


rc = G.prepare_chain()
# i = input("egeGenie: ")


def remove_stars(ans:str):
    return ans.replace("*", "")
    


@app.post("/chat")
async def chat_with_genie(message: Message):
    i = message.user_says
    response = G.genies_responses(i, rc)
    answer = response['answer']
    print(remove_stars(answer))

    return {"genie": remove_stars(answer)}