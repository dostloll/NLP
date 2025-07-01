from fetcher import fetch_comments
from cleaner import clean_comment
from analyzer import analyze_comments

if __name__ == "__main__":
    raw_comments = fetch_comments()
    cleaned_comments = [clean_comment(c) for c in raw_comments]
    results = analyze_comments(cleaned_comments)

    print(f"Total comments: {len(cleaned_comments)}")
    for sentiment, count in results.items():
        print(f"{sentiment.capitalize()}: {count}")
