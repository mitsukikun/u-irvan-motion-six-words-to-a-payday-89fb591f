import os

LINE = "First paycheck cleared. I finally exist."

try:
    os.makedirs("/output", exist_ok=True)
except Exception:
    pass

with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
