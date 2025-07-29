
# Email Summarizer using Transformers

This Python project connects to your Gmail inbox, fetches the latest emails, and generates concise summaries using a pretrained transformer-based summarization model.

## Features

- Secure login with IMAP and App Password  
- Fetches the latest N emails based on user input  
- Groups emails by subject to identify conversation threads  
- Summarizes long email threads in approximately 5–6 lines using the `bart-large-cnn-samsum` model  
- Modular structure with separate files for fetching, summarizing, and main execution

## Project Structure

```
emailsummarizer/
│
├── fetch_emails.py       # Connects to Gmail and fetches emails
├── summarize.py          # Summarizes grouped emails using Transformers
├── main.py               # Entry point, takes input and runs the process
├── config.py             # Contains email credentials (not to be pushed)
└── README.md             # Project documentation
```

## Installation

1. Clone the repo
```bash
git clone https://github.com/yourusername/emailsummarizer.git
cd emailsummarizer
```

2. Create a virtual environment (optional but recommended)
```bash
python -m venv venv
venv\Scripts\activate   # Windows
# OR
source venv/bin/activate   # macOS/Linux
```

3. Install required libraries
```bash
pip install -r requirements.txt
```

**Contents of `requirements.txt`:**
```
transformers
torch
```

## Setup Gmail IMAP Access

1. Enable IMAP access in your [Gmail settings](https://mail.google.com/mail/u/0/#settings/fwdandpop).
2. [Generate an App Password](https://myaccount.google.com/apppasswords) for Gmail if you have 2FA enabled.
3. Create a `config.py` file in the project folder:

```python
# config.py
EMAIL = "your-email@gmail.com"
PASSWORD = "your-app-password"
IMAP_SERVER = "imap.gmail.com"
```

Note: Add `config.py` to your `.gitignore` to prevent exposing credentials.

## Usage

Run the project:

```bash
python main.py
```

You'll be prompted to enter the number of emails to summarize (e.g., 5, 10).

## Model Used

- `philschmid/bart-large-cnn-samsum`: A fine-tuned BART model trained for dialogue and conversational summarization.

## Security Note

Do not commit or push `config.py` with your credentials. Always keep sensitive information private.

## Example Output

```
Enter how many emails you want to summarize: 5

===== Topic-wise Combined Email Summaries =====

--- Summary for Topic: Meeting Agenda ---

The team discussed updates on the Q3 roadmap, finalized deadlines for upcoming sprints, and confirmed key responsibilities. Follow-ups are scheduled for next Monday.
```

## Future Improvements

- GUI with Tkinter or Flask interface  
- Multi-label categorization of emails  
- Export summaries to PDF or Markdown

## License

This project is licensed under the MIT License.
