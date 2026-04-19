print("Social Media Content Sanitizer")
# Load posts from file
def load_posts(posts_file):
    posts=[]
    file=open(posts_file, "r")
    for line in file:
        line=line.strip() 
        if "|" in line:       
            parts = line.split("|")
            user = parts[0]
            content = parts[1]
            posts.append((user, content))
    file.close()
    return posts
def is_banned(word, banned_words):
    for bw in banned_words:
        if word.startswith(bw):   # handles words like badly, hateful
            return True
    return False
def clean_text(content, banned_words):
    for word in banned_words:
        content = content.replace(word, "***")
        content = content.replace(word.capitalize(), "***")
        content=content.replace(word.upper(),"***")
    return content
def count_issues(content, banned_words):
    words=content.lower().split()  
    count=0
    for w in words:
        if is_banned(w,banned_words):
            count += 1

    return count
def extract_links(content):
    words=content.split()
    links=[]
    for word in words:
        if word.startswith("http://") or word.startswith("https://"):
            links.append(word)
    return links
def save_to_file(filename, data):
    with open(filename,"w") as f:
        for line in data:
            f.write(line +"\n")
def process(posts, banned_words):
    total=0
    cleaned_count=0
    blocked_count=0
    all_links=[]
    user_issues={}
    violation_log=[]
    cleaned_posts_output=[]
    for user, content in posts:
        total+=1
        if user not in user_issues:   #shaistha 
            user_issues[user]=0
        # Count issues
        issues=count_issues(content, banned_words)
        user_issues[user] += issues
        # Clean post
        cleaned_post=clean_text(content, banned_words)
        # Decide status
        if issues==0:
            status="SAFE"
            final_post=cleaned_post
        elif issues<=3:
            status="CLEANED"
            cleaned_count+=1
            final_post=cleaned_post
        else:
            status="BLOCKED"
            blocked_count+=1
            final_post="POST REMOVED"
        # Extract links
        links=extract_links(content)
        all_links.extend(links)
        # Store logs
        violation_log.append(f"{user} | Issues: {issues} | Status: {status}")
        cleaned_posts_output.append(f"{user} | {final_post} | {status}")
        print("\nUser:", user)
        print("Post:", final_post)
        print("Status:", status)
    return total,cleaned_count,blocked_count,all_links,user_issues,violation_log,cleaned_posts_output
def main():
    banned_words=[
    "bad", "toxic", "hate", "ugly", "stupid",
    "angry", "annoy", "dirty", "evil", "fake",
    "fraud", "spam", "scam", "abuse", "harsh",
    "nasty", "rude", "mean", "offensive", "violent",
    "threat", "curse", "damn", "trash", "worst",
    "pathetic", "idiot", "fool", "loser", "jerk"]
    posts = load_posts("posts.txt")
    total, cleaned, blocked, links, user_issues, violation_log, cleaned_posts_output = process(posts, banned_words)
    save_to_file("links_found.txt", links)
    save_to_file("violations.txt", violation_log)
    save_to_file("cleaned_posts.txt", cleaned_posts_output)
    # User report
    user_report = []
    print("\n--------User Report---------")
    for user, count in user_issues.items():
        line=f"{user}: {count}"
        print(line)
        user_report.append(line)
    save_to_file("user_report.txt", user_report)
    print("\n=== Final Report ===")
    print(f"Total Posts: {total}")
    print(f"Cleaned: {cleaned}")
    print(f"Blocked: {blocked}")
    print(f"Total Links Found: {len(links)}")
main()
