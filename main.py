from plugin.client import DummyJsonClient
from plugin.evidence_1 import print_evidence_1
from plugin.evidence_2 import print_evidence_2
from plugin.evidence_3 import print_evidence_3

def main():
    client = DummyJsonClient(username="emilys", password="emilyspass")

    if not client.connect():
        print("Connectivity test failed.")
        return

    print("Connected successfully.")

    print_evidence_1(client)
    print_evidence_2(client)
    print_evidence_3(client)

if __name__ == "__main__":
    main()