"""
FastAPI REST API Starter Code
Student Name: [Your Name]
Date: [Today's Date]

This starter code provides a basic structure for building a REST API with FastAPI.
Complete the TODOs to implement all required functionality.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

# Create the FastAPI application instance
app = FastAPI(
    title="My REST API",
    description="A simple REST API built with FastAPI",
    version="1.0.0"
)

# TODO: Define your Pydantic model here
# Example:
# class Item(BaseModel):
#     id: Optional[int] = None
#     name: str
#     description: str
#     price: float
#     in_stock: bool = True


# In-memory storage (replace with database in Task 4)
items_db = []


# TODO: Implement root endpoint
@app.get("/")
async def root():
    """
    Root endpoint - returns a welcome message
    """
    pass


# TODO: Implement CREATE endpoint
@app.post("/items/", status_code=201)
async def create_item():
    """
    Create a new item
    """
    pass


# TODO: Implement READ all items endpoint
@app.get("/items/")
async def get_all_items():
    """
    Retrieve all items
    """
    pass


# TODO: Implement READ single item endpoint
@app.get("/items/{item_id}")
async def get_item(item_id: int):
    """
    Retrieve a single item by ID
    """
    pass


# TODO: Implement UPDATE endpoint
@app.put("/items/{item_id}")
async def update_item(item_id: int):
    """
    Update an existing item
    """
    pass


# TODO: Implement DELETE endpoint
@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    """
    Delete an item by ID
    """
    pass


# Run the application
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
