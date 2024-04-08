from fastapi import APIRouter, HTTPException
from typing import Tuple
from ..utils.data_fetcher import fetch_users_posts
from ..utils.data_analyzer import find_user_most_posts, calculate_avg_title_length, find_common_words

router = APIRouter()

# Function to safely fetch users' posts data
async def safely_fetch_users_posts() -> Tuple[list, list]:
    try:
        users, posts = await fetch_users_posts()
        return users, posts
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to fetch data from the external API.")

# Endpoint to retrieve analysis data
@router.get("/analysis")
async def get_analysis():
    # Safely fetch users' posts data
    users, posts = await safely_fetch_users_posts()

    # Check if users or posts data is empty
    if not users or not posts:
        raise HTTPException(status_code=404, detail="Data not found")

    # Find user with the most posts
    user_with_most_posts_id = find_user_most_posts(posts)['id']
    user_with_most_posts = next((user for user in users if user['id'] == user_with_most_posts_id), None)
    
    # Check if user with most posts exists
    if not user_with_most_posts:
        raise HTTPException(status_code=404, detail="User not found")

    # Calculate average title length for the user with the most posts
    average_title_length = calculate_avg_title_length(posts, user_with_most_posts_id)
    
    # Find common words in post titles
    common_words = find_common_words(posts)

    return {
        "user_with_most_posts": user_with_most_posts['name'],
        "average_title_length": average_title_length,
        "common_words": common_words
    }