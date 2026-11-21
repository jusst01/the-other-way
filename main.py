import os
import sys

text = "The bag was packed. The door stood open. I turned the key the other way, hung my coat back on its hook, and stayed, not because I could not leave, but because leaving is not the only brave direction."

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)
with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(text)
