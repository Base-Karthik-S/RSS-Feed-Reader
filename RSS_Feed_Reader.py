import requests
import feedparser

def fetch_rss_feed(feed_url):
    try:
        response = requests.get(feed_url)
        response.raise_for_status()

        feed = feedparser.parse(response.text)
        return feed
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching the feed: {e}")
        return None

def read_rss_feed(feed_url):
    feed = fetch_rss_feed(feed_url)
    if feed:
        print(f"Title: {feed.feed.title}")
        print(f"Description: {feed.feed.description}")
        print("Entries:")

        for entry in feed.entries:
            print("\nTitle:", entry.title)
            print("Link:", entry.link)
            print("Published Date:", entry.published)
            print("\nSummary:")
            print(entry.summary)
            print("\n" + "-" * 50)

if __name__ == "__main__":
    rss_feed_url = input("Enter the RSS feed URL: ")
    read_rss_feed(rss_feed_url)
