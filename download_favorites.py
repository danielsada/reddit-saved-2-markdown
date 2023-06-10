import praw
from dotenv import load_dotenv
import os

load_dotenv()

# Set up the Reddit API credentials
reddit = praw.Reddit(
    client_id=os.getenv('CLIENT_ID'),
    client_secret=os.getenv('CLIENT_SECRET'),
    user_agent=os.getenv('USER_AGENT'),
    username=os.getenv('USERNAME'),
    password=os.getenv('PASSWORD')
)

def download_saved_posts(username):
    user = reddit.redditor(username)
    saved_posts = user.saved(limit=None)
    number_of_saved_posts = 0
    with open("saved.md", "w+") as s:
        for post in saved_posts:
           
            if isinstance(post, praw.models.Submission):
                # Download submission
                s.write(download_submission(post))
            elif isinstance(post, praw.models.Comment):
                # Download comment
                s.write(download_comment(post))
            
            number_of_saved_posts += 1
            if number_of_saved_posts % 10 == 0:
                print(f"Saved {number_of_saved_posts} to markdown.")

def download_submission(submission):
    # Extract relevant information
    title = submission.title
    url = submission.url

    # Generate Markdown content
    markdown_content = f"# {title}\n\n{url}\n\n---\n\n"
    return markdown_content

def download_comment(comment):
    # Extract relevant information
    body = comment.body

    # Generate Markdown content
    markdown_content = f"> {body}\n\n---\n\n"

    return markdown_content

# Call the function with the username
username = os.getenv('USERNAME')
download_saved_posts(username)
