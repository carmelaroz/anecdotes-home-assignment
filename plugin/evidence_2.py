from plugin.collect_evidence import collect_evidence_2

def print_evidence_2(client):
    e2 = collect_evidence_2(client)
    print("\n=== Evidence E2 ===")
    for post in e2:
        print(f"\n--- Post ID: {post['id']} ---")
        print(f"Title    : {post['title']}")
        print(f"Author ID: {post['userId']}")
        print(f"Views    : {post['views']}")
        print(f"Reactions: 👍 {post['reactions']['likes']} | 👎 {post['reactions']['dislikes']}")
        print(f"Tags     : {', '.join(post['tags'])}")
        print(f"Body     : {post['body']}")