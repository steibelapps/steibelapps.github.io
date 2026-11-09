#!/usr/bin/env python3
"""The blog's line of posts, one a week, Sundays at 10 AM Eastern.

  python3 tools/queue.py              list what is queued and when each goes up
  python3 tools/queue.py add FILE     put a draft (from _drafts/) at the end of the line
  python3 tools/queue.py next         show the next post in line

A queued post is a file in _posts/ named with its Sunday, dated 10:00 that morning. GitHub
only shows it once that time has passed (see .github/workflows/sunday-post.yml)."""
import datetime as dt, os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
POSTS = os.path.join(ROOT, "_posts")

def queued():
    out = []
    for f in sorted(os.listdir(POSTS)):
        m = re.match(r"(\d{4}-\d{2}-\d{2})-(.+)\.md$", f)
        if m:
            title = re.search(r'^title:\s*"?(.*?)"?\s*$', open(os.path.join(POSTS, f)).read(), re.M)
            out.append((dt.date.fromisoformat(m.group(1)), f, title.group(1) if title else m.group(2)))
    return out

def next_free_sunday():
    today = dt.date.today()
    taken = {d for d, _, _ in queued()}
    d = today + dt.timedelta(days=(6 - today.weekday()) % 7 or 7)
    while d in taken: d += dt.timedelta(days=7)
    return d

def add(path):
    text = open(path).read()
    text = re.sub(r"<!--.*?-->\s*", "", text, flags=re.S)            # drop notes to Joe
    day = next_free_sunday()
    fm = f"date: {day.isoformat()} 10:00:00"   # Eastern time, from timezone in _config.yml
    text = re.sub(r"^---\n", "---\n" + fm + "\n", text, count=1)
    slug = re.sub(r"^building-with-ai-\d+-", "", os.path.basename(path))
    dest = os.path.join(POSTS, f"{day.isoformat()}-{slug}")
    open(dest, "w").write(text)
    print("queued for Sunday", day.strftime("%B %-d, %Y"), "->", os.path.relpath(dest, ROOT))

if __name__ == "__main__":
    os.makedirs(POSTS, exist_ok=True)
    if len(sys.argv) > 2 and sys.argv[1] == "add": add(sys.argv[2])
    elif len(sys.argv) > 1 and sys.argv[1] == "next":
        q = [x for x in queued() if x[0] >= dt.date.today()]
        print(q[0] if q else "nothing queued")
    else:
        for d, f, t in queued(): print(d.strftime("%a %b %-d"), "|", t, "|", f)
