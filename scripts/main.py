import json
import datetime
import random
import subprocess

today = datetime.date.today().isoformat()

# Load festival data
with open("data/festivals_2026.json") as f:
    festivals = json.load(f)

# Load fallback occasions
with open("data/master_heritage.json") as f:
    occasions = json.load(f)

# Decide today's occasion
if today in festivals:
    occasion = festivals[today]
else:
    occasion = random.choice(occasions)["name"]

# AI prompt (STRICT BRAND CONTROL)
prompt = f"""
Create a premium Telugu cultural post for: {occasion}

Rules:
- Very emotional
- Divine + traditional tone
- Short (3–5 lines max)
- Should feel like temple / wedding vibe

Must include:
- Nadaswaram
- Dolu
- Saxophone
- Drum

End with:
Book Vidhwaan artists
pellimelam.vidhwaan.com
"""

# Run Ollama
result = subprocess.run(
    ["ollama", "run", "llama3", prompt],
    capture_output=True,
    text=True
)

caption = result.stdout.strip()

# Save output
with open("scripts/output.txt", "w") as f:
    f.write(caption)

print("Generated:", caption)
