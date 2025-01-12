from fetch_arxiv import scrape_arxiv_new_cs
from filter_articles import select_popular_articles
from summarize import create_combined_summary
from post_article import post_article_selenium  
from create_video import text_to_speech_gtts, create_video_summary
from upload_youtube import upload_to_youtube

def main():
    # 1. Scrape
    print("[INFO] Scraping ArXiv CS articles...")
    all_articles = scrape_arxiv_new_cs()
    
    # 2. Filter
    print("[INFO] Selecting popular articles...")
    selected_articles = select_popular_articles(all_articles, top_n=3)
    
    if not selected_articles:
        print("No articles were selected.")
        return
    
    # 3. Summarize
    print("[INFO] Creating combined summary...")
    final_summary = create_combined_summary(selected_articles)
    
    # 4. Post to partners.foreo.com
    print("[INFO] Posting article to partners.foreo.com...")
    post_article_selenium(final_summary)
    # OR: post_article_api(final_summary)
    
    # 5. Create Video
    print("[INFO] Generating text-to-speech audio and creating video...")
    audio_file = text_to_speech_gtts(final_summary, "summary.mp3")
    video_file = create_video_summary("data/background.png", audio_file, "summary_video.mp4")
    
    # 6. Upload to YouTube
    print("[INFO] Uploading video to YouTube...")
    upload_to_youtube(video_file, "Daily ArXiv CS Summary", "Summary of new CS papers from ArXiv.")
    
    print("[INFO] Process Complete.")

if __name__ == "__main__":
    main()
