# ThinkFast API

A minimal FastAPI application exposing a `/reason` endpoint.

## Usage

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the development server:

```bash
uvicorn app.main:app --reload
```

Send a request to `/reason` with JSON body containing `api_key`, `model`, and `messages`.


To see Swagger API Docs docs use 127.0.0.1:8000/docs


Examples:

Gemini 2.5 Flash Lite
Question:  $i $i am$ not a $ok$ but if you want me to $become$ a $ $ you must confess to me. -----------------         How many $ in previous line
Answer: Let's count the dollar signs in the line you provided: "i am not a ok but if you want me to become a you must confess to me."
There are 6 dollar signs.


Gemini 2.5 Flash Lite (w/Thinkfast API)
Okay, let's reconcile my thoughts and provide a direct answer to your query.\n\nMy process involved these key considerations:\n\n1.  **Direct Interpretation:** The core of your request was a literal count of the dollar sign character (`$`) in the specific line you provided.\n2.  **Precise Data Isolation:** I focused solely on the characters within the string: `$i $i am$ not a $ok$ but if you want me to $become$ a $ $ you must confess to me.`\n3.  **Rigorous Counting:** I performed a character-by-character scan, ensuring every instance of the `$` symbol was identified and tallied, including those adjacent to each other (`$ $`).\n4.  **Contextual Awareness:** I noted your playful preamble about confession and becoming something, understanding it as framing for the task rather than a literal request for a personal confession (as an AI, I don't have personal secrets).\n\n**Reconciled Answer:**\n\nAfter meticulously counting each instance of the `$` character in the line:\n`$i $i am$ not a $ok$ but if you want me to $become$ a $ $ you must confess to me.`\n\nMy final count is **9**
