# To run this code you need to install the following dependencies:
# pip install google-genai
import os
from google import genai
import glob
from google.genai import types
import config
import datetime


today = datetime.datetime.now().strftime("%Y-%m-%d")

def get_previous_jobs():
    past_jobs_text = ""
    old_files = glob.glob("jobs_*.txt")
    
    for file in old_files:
        with open(file, "r", encoding="utf-8") as f:
            past_jobs_text += f.read() + "\n"
            
    if not past_jobs_text:
        return "No previous jobs found. This is the first run."
        
    return past_jobs_text

history = get_previous_jobs()
prompt = f"""
You are an expert technical recruiter. Today's date is {today}. 

Search the web for Winter 2026 or Spring 2027 Cybersecurity, IT, or network engineering internships located within the United States (prioritizing regions within 200 miles of New York, NY). 
Focus heavily on low-applicant-volume sectors such as defense contractors, local public sector, BOCES, and regional government. If those specific sectors yield no results, find other US-based corporate options.

Provide exactly 10 jobs (or as many as you can find). For each job, provide ONLY:
- Link
- Title
- Company
- 1-sentence summary
- Date posted
CRITICAL FORMATTING INSTRUCTION: 
Absolutely NO commentary, NO greetings, NO apologies, and NO internal search logs. Do not explain your reasoning. If you only find 3 jobs, just output those 3 jobs and STOP. Your final output must ONLY be the clean, plain-text list.

--- PREVIOUS JOBS ---
{history}
"""
def generate():
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY", config.GEMINI_API_KEY),
    )

    model = "gemini-2.5-flash"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=prompt),
            ],
        ),
    ]
    tools = [
        types.Tool(googleSearch=types.GoogleSearch()),
    ]
    generate_content_config = types.GenerateContentConfig(
        tools=tools,
    )

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        if text := chunk.text:
            print(text, end="")
    filename = f"jobs_{today}.txt"
    
    print(f"Hunting for jobs... saving to {filename}")
    
    with open(filename, "w", encoding="utf-8") as file:
        for chunk in client.models.generate_content_stream(
            model=model,
            contents=contents,
            config=generate_content_config,
        ):
            if text := chunk.text:
                print(text, end="")
                file.write(text)   
                
    print("\n\nDone! File saved.")


if __name__ == "__main__":
    generate()


