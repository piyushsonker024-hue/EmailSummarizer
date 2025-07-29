from fetch_emails import connect_email, fetch_emails
from summarize import summarize_email_threads

def main():
    try:
        num = int(input("Enter how many emails you want to summarize (e.g., 5 or 10): "))
    except ValueError:
        print("Invalid input. Using default of 5 emails.")
        num = 5

    mail = connect_email()
    emails = fetch_emails(mail, num_emails=num)

    if not emails:
        print("No emails found.")
        return

    thread_summaries = summarize_email_threads(emails)

    print("\n===== Topic-wise Combined Email Summaries =====\n")
    for subject, summary in thread_summaries.items():
        print(f"\n--- Summary for Topic: {subject} ---\n")
        print(summary)

if __name__ == "__main__":
    main()
