# Anecdotes Home Assignment

### Overview
This project implements a simple client that interacts with the DummyJSON API to authenticate, collect user data, fetch posts, and retrieve post comments.

### Assignment Structure
- **client.py**: Contains the DummyJsonClient class, which is responsible for connecting to the API and making authenticated requests to fetch data.

- **collect_evidence.py**: Contains functions to collect different sets of evidence (data) from the API, such as user details, posts, and post comments.

- **evidence_1.py, evidence_2.py, evidence_3.py**: These files contain functions to print the data collected by the functions in collect_evidence.py.

- **main.py**: The main entry point of the program, which initiates the client, connects to the API, and prints the collected evidence.

### Steps to Run:
1. Clone or download the repository.

2. Navigate to the project directory.

3. Install dependencies:
`pip install requests`

4. Run the main program:
`python main.py`

### Example Output

```
Connected successfully.

=== Evidence E1 ===
id: 12345
username: emilys
email: emily@example.com
...

=== Evidence E2 ===
--- Post ID: 1 ---
Title    : Post Title 1
Author ID: 101
Views    : 1000
Reactions: 👍 200 | 👎 50
Tags     : tag1, tag2
Body     : This is the body of the post...

--- Post ID: 2 ---
Title    : Post Title 2
Author ID: 102
Views    : 1500
Reactions: 👍 300 | 👎 100
Tags     : tag3, tag4
Body     : This is the body of the post...

...

=== Evidence E3 ===
--- Post ID: 1 ---
Title: Post Title 1
Comments:
- Great post!
- Very informative.

--- Post ID: 2 ---
Title: Post Title 2
Comments:
- I agree with this.
```