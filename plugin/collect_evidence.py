def collect_evidence_1(client):
    """
    E1 - Collect the authenticated user details.
    """
    data = client.get("/auth/me")
    if not data:
        print("Failed to fetch authenticated user details.")
        return None
    return data


def collect_evidence_2(client):
    """
    E2 - Collect a list of 60 posts.
    """
    data = client.get("/posts", params={"limit": 60})
    if not data or "posts" not in data:
        print("Failed to fetch posts.")
        return []
    return data["posts"]


def collect_evidence_3(client):
    """
    E3 - Collect a list of 60 posts, including comments.
    """
    posts = collect_evidence_2(client)
    post_comments_map = {}

    for post in posts:
        post_id = post["id"]
        comments_data = client.get(f"/posts/{post_id}/comments")
        comments = comments_data.get("comments", []) if comments_data else []

        post_comments_map[post_id] = {
            "post": post,
            "comments": comments
        }

    return post_comments_map