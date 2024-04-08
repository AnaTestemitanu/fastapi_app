import pytest
from app.utils.data_analyzer import find_user_most_posts, calculate_avg_title_length, find_common_words

# Test case for finding the user with the most posts
def test_find_user_most_posts():
    # Sample posts data
    posts = [
        {"userId": 1, "id": 1, "title": "Post 1", "body": "Body 1"},
        {"userId": 1, "id": 2, "title": "Post 2", "body": "Body 2"},
        {"userId": 2, "id": 3, "title": "Post 3", "body": "Body 3"},
    ]
    # Expected result for the user with the most posts
    expected = {"id": 1, "post_count": 2}
    # Assert the function output matches the expected result
    assert find_user_most_posts(posts) == expected

# Test case for calculating the average title length
def test_calculate_avg_title_length():
    # Sample posts data
    posts = [
        {"userId": 1, "id": 1, "title": "Short", "body": "Body 1"},
        {"userId": 1, "id": 2, "title": "A bit longer title", "body": "Body 2"},
        {"userId": 1, "id": 3, "title": "An even longer title than before", "body": "Body 3"},
    ]
    # Expected average title length
    # Average length = (5 + 18 + 32) / 3 = 18.333...
    expected = 18.333333333333332
    # Assert the calculated average title length matches the expected value with pytest.approx
    assert calculate_avg_title_length(posts, 1) == pytest.approx(expected)

# Test case for finding the common words in post titles
def test_find_common_words():
    # Sample posts data
    posts = [
        {"userId": 1, "id": 1, "title": "hello world", "body": "Body 1"},
        {"userId": 1, "id": 2, "title": "hello again", "body": "Body 2"},
        {"userId": 2, "id": 3, "title": "goodbye world hello", "body": "Body 3"},
    ]
    # Expected common words
    expected = ["hello", "world", "again", "goodbye"]
    # Get the common words from the function
    common_words = find_common_words(posts)
    # Ensure all expected words are present in the result
    assert all(word in common_words for word in expected), f"Expected {expected} to be in {common_words}"
    # Additionally, check if the length of the common words list matches the expected length
    assert len(common_words) == len(expected), f"Expected {len(expected)} words, got {len(common_words)}"
