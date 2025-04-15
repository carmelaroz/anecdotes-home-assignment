from plugin.collect_evidence import collect_evidence_3

def print_evidence_3(client):
    e3 = collect_evidence_3(client)
    print("\n=== Evidence E3 ===")
    for post_id, data in e3.items():
        post = data['post']
        comments = data['comments']

        print(f"\n--- Post ID: {post_id} ---")
        print(f"Title: {post['title']}")
        print("Comments:")

        if not comments:
            print("- (No comments)")
        else:
            for comment in comments:
                print(f"- {comment['body']}")