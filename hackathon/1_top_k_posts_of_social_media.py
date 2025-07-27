import heapq


# Define the scoring function
def relevance_score(post):
    likes_weight = 2.0
    recency_weight = 1.5
    comments_weight = 1.2
    shares_weight = 1.3
    media_boost = 10
    friend_score_weight = 15
    length_penalty = 0.05

    score = 0
    score += post["likes"] * likes_weight
    score += post["recency"] * recency_weight
    score += post.get("comments", 0) * comments_weight
    score += post.get("shares", 0) * shares_weight
    score += media_boost if post.get("has_media", False) else 0
    score += post.get("friend_score", 0) * friend_score_weight

    text_length = len(post.get("text", ""))
    if text_length > 300:
        score -= length_penalty * text_length

    return score


# Function to find top K posts
def get_top_k_posts(posts, k):
    min_heap = []

    for post in posts:
        score = relevance_score(post)
        if len(min_heap) < k:
            heapq.heappush(min_heap, (score, post))
        else:
            if score > min_heap[0][0]:
                heapq.heappushpop(min_heap, (score, post))

    # Sort top K by score in descending order
    return [post for score, post in sorted(min_heap, reverse=True)]


# Sample posts
posts = [
    {
        "id": 1,
        "likes": 100,
        "recency": 10,
        "comments": 30,
        "shares": 10,
        "has_media": True,
        "friend_score": 0.9,
        "text": "A beautiful sunset over the hills.",
    },
    {
        "id": 2,
        "likes": 80,
        "recency": 15,
        "comments": 10,
        "shares": 5,
        "has_media": False,
        "friend_score": 0.5,
        "text": "Don't forget to vote today!",
    },
    {
        "id": 3,
        "likes": 200,
        "recency": 5,
        "comments": 60,
        "shares": 20,
        "has_media": True,
        "friend_score": 0.3,
        "text": "Check out this cool tech!",
    },
    {
        "id": 4,
        "likes": 50,
        "recency": 20,
        "comments": 5,
        "shares": 2,
        "has_media": False,
        "friend_score": 1.0,
        "text": "See you all at the event tomorrow.",
    },
    {
        "id": 5,
        "likes": 120,
        "recency": 8,
        "comments": 15,
        "shares": 10,
        "has_media": True,
        "friend_score": 0.7,
        "text": "Throwback to last weekend’s party!",
    },
]

# Top K posts
top_k_posts = get_top_k_posts(posts, k=3)

# Print the top posts with their scores
for post in top_k_posts:
    print(
        f"Post ID: {post['id']}, Score: {relevance_score(post):.2f}, Text: {post['text']}"
    )
