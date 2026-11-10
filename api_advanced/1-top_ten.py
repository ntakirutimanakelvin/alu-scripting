cat > 1-top_ten.py << 'EOF'
#!/usr/bin/python3
"""Query Reddit API for top ten hot posts of a subreddit."""

import requests


def top_ten(subreddit):
    """Print titles of the first 10 hot posts for a subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) alu-scripting/1.0"}
    params = {"limit": 10}
    try:
        response = requests.get(
            url, headers=headers, params=params,
            allow_redirects=False, timeout=10
        )
        if response.status_code != 200:
            print(None)
            return
        children = response.json().get("data", {}).get("children", [])
    except (requests.RequestException, ValueError):
        print(None)
        return
    for child in children[:10]:
        print(child.get("data", {}).get("title"))
EOF
chmod +x 1-top_ten.py
python3 1-main.py programming
python3 1-main.py this_is_a_fake_subreddit
