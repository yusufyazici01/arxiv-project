from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text, max_length=130):
    summary = summarizer(text, max_length=max_length, min_length=50, do_sample=False)
    return summary[0]['summary_text']

def create_combined_summary(articles):
    combined_summary = ""
    for article in articles:
        summary = summarize_text(article["abstract"])
        combined_summary += f"**{article['title']}** by {article['authors']} \n\n"
        combined_summary += summary + "\n\n"
    return combined_summary.strip()