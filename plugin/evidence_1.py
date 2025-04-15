from plugin.collect_evidence import collect_evidence_1

def print_evidence_1(client):
    e1 = collect_evidence_1(client)
    print("\n=== Evidence E1 ===")
    for key, value in e1.items():
        print(f"{key}: {value}")