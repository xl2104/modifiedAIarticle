from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from test_gpt import sum_chi_article

# Create a FastAPI instance
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
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
    return {"modified_article": modified_text}
