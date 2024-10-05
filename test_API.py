from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# from fastapi.middleware.cors import CORSMiddleware
# from starlette.responses import JSONResponse
# from starlette.requests import Request

from pydantic import BaseModel
from test_gpt import sum_chi_article

# Create a FastAPI instance
app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
]

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
    max_age=86400
)


# Define a Pydantic model to handle the input

class ArticleInput(BaseModel):
    text: str

# Define a function to modify the article


def modify_article(article: str) -> str:
    # Simple modification: convert to uppercase (you can replace this with any logic)
    summary = sum_chi_article(article)
    # return article.upper()
    return summary

# Define a POST endpoint


@app.post("/modify-article/")
async def modify_article_endpoint(input: ArticleInput):
    # Modify the article using the modify_article function
    modified_text = modify_article(input.text)
    # Return the modified article
    return {"original article": input.text,
            "modified_article": modified_text}


# @app.options("/modify-article/")
# async def preflight_handler(request: Request):
#     return JSONResponse(status_code=200)
