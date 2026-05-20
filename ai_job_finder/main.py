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

Search the web for 10 newly posted Fall 2026 Cybersecurity, IT, or network engineering internships within 400 miles of New York, NY. 
Target postings strictly within the last 3 days. Focus heavily on low-applicant-volume sectors such as defense contractors, local public sector, BOCES, and regional government.

Provide exactly 10 jobs (or as many as you can find). For each job, provide ONLY:
- Link
- Title
- Company
- 1-sentence summary

Do not provide any conversational filler, greetings, or commentary. Output the results as a clean, plain-text list.

CRITICAL INSTRUCTION:
Below is the history of jobs you have already found in previous days. You must read through these and absolutely DO NOT include any of these companies or roles in your new output today.

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


