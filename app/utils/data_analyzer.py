from collections import Counter

# Function to find the user with the most posts
def find_user_most_posts(posts):
    post_count = Counter(post['userId'] for post in posts)
    user_id, _ = post_count.most_common(1)[0]
    return {"id": user_id, "post_count": _}

# Function to calculate the average title length for a user
def calculate_avg_title_length(posts, user_id):
    titles = [post['title'] for post in posts if post['userId'] == user_id]
    avg_length = sum(len(title) for title in titles) / len(titles)
    return avg_length

# Function to find the most common words in post titles
def find_common_words(posts):
    words = Counter(word.lower() for post in posts for word in post['title'].split())
    common_words = [word for word, count in words.most_common(5)]
    return common_words