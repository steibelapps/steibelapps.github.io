#!/usr/bin/env python3
"""The blog's line of posts, one a week, Sundays at 10 AM Eastern.

  python3 tools/queue.py              list what is queued and when each goes up
  python3 tools/queue.py add FILE     put a draft (from _drafts/) at the end of its app's line

Weeks alternate from November 22, 2026: Daily Brief, then Periodic, then Daily Brief...
A post says which app it is about with "app: daily-brief" or "app: periodic" in its front
matter (default daily-brief), and goes to the next free Sunday of that app's weeks.
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

START = dt.date(2026, 11, 22)   # a Daily Brief week; the next Sunday is Periodic's

def app_of_week(d):
    return "daily-brief" if ((d - START).days // 7) % 2 == 0 else "periodic"

def next_free_sunday(app="daily-brief"):
    today = dt.date.today()
    taken = {d for d, _, _ in queued()}
    d = today + dt.timedelta(days=(6 - today.weekday()) % 7 or 7)
    while d in taken or (d >= START and app_of_week(d) != app): d += dt.timedelta(days=7)
    return d

def add(path):
    text = open(path).read()
    text = re.sub(r"<!--.*?-->\s*", "", text, flags=re.S)            # drop notes to Joe
    m = re.search(r"^app:\s*(\S+)", text, re.M)
    day = next_free_sunday(m.group(1) if m else "daily-brief")
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
        for d, f, t in queued(): print(d.strftime("%a %b %-d"), "|", app_of_week(d) if d >= START else "intro", "|", t, "|", f)
