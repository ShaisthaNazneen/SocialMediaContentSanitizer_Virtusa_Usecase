#Social Media Content Sanitizer
##  Project Overview
This project is a **Content Moderation System** designed for a safe social media platform.
It automatically scans user posts, detects inappropriate content, masks banned words, extracts links, and generates reports.
---
## Problem Statement
Build a system that:
* Detects banned/offensive words in posts
* Cleans or blocks posts based on violations
* Extracts URLs for security checking
* Tracks user-wise violations
* Generates reports
---
## Features
* Word masking using `replace()`
* Case handling (lowercase, uppercase, capitalized)
* Link extraction (`http://`, `https://`)
* User-wise violation tracking
* Post classification:

  * SAFE (0 issues)
  * CLEANED (1–3 issues)
  * BLOCKED (>3 issues)
* File handling (input + output reports)
---
##  Technologies Used
* Python
* File Handling
* Lists & Dictionaries
* String Processing
---
## Project Structure
```
📁 SocialMediaContent
│
├── posts.txt                # Input posts
├── main.py                  # Main Python script
├── links_found.txt          # Extracted links
├── violations.txt           # Violation logs
├── cleaned_posts.txt        # Cleaned/blocked posts
├── user_report.txt          # User-wise report
└── README.md                # Project documentation
---
## How It Works

1. Load posts from file
2. Check each post for banned words
3. Count violations
4. Clean or block the post
5. Extract links
6. Store results in files
7. Generate final report
---
## Output Files

* **links_found.txt** → All extracted URLs
* **violations.txt** → User + issues + status
* **cleaned_posts.txt** → Final processed posts
* **user_report.txt** → Total violations per user
---
## How to Run
```bash
python main.py
```
---

## Example Output

```
User: Mahira
Post: I *** when app crashes https://github.com
Status: CLEANED
---
## Author
Shaistha Nazneen
---
