from transformers import pipeline, logging
from collections import defaultdict

logging.set_verbosity_error()

# Initialize the summarization model
summarizer = pipeline("summarization", model="philschmid/bart-large-cnn-samsum")

def summarize_large_text(text, max_chunk_len=1000):
    summaries = []
    start = 0
    while start < len(text):
        chunk = text[start:start + max_chunk_len]
        summary = summarizer(
            chunk,
            max_length=200,  # Around 5–6 lines
            min_length=60,
            do_sample=False
        )[0]['summary_text']
        summaries.append(summary)
        start += max_chunk_len
    return " ".join(summaries)

def summarize_email_threads(emails):
    subject_threads = defaultdict(list)
    for email_item in emails:
        subject_threads[email_item['subject']].append(email_item['body'])
    
    thread_summaries = {}
    for subject, bodies in subject_threads.items():
        print(f"\nSummarizing thread for subject: {subject}")
        combined_body = "\n\n".join(bodies)
        summary = summarize_large_text(combined_body)
        thread_summaries[subject] = summary
    return thread_summaries
