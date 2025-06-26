# ThinkFast API

> **Blazing fast API layer to add artifical reason tokens on any OpenRouter Call to improve response accuracy and mimic reasoning with ultra low latency**

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg?style=for-the-badge)](LICENSE)

## 🎯 Overview

ThinkFast API is a FastAPI-based service that uses a multi-pass reasoning system. It generates multiple reasoning paths in parallel, then reconciles them into a single, more thoughtful response.

## 🧠 How It Works Under the Hood

### The Multi-Pass Reasoning Mechanism

1. **Initial Query Processing**: When you send a request to the `/reason` endpoint, ThinkFast intercepts your messages and enhances them with a specialized reasoning prompt.

2. **Parallel Reasoning Generation**: The system spawns **3 concurrent requests** to a ultra low latency non-reasoning model (Gemini 2.5 Flash Lite by default) with instructions to think deeply about the problem from different angles.

3. **Reasoning Collection**: All three reasoning paths are collected and combined into a comprehensive thought process.

4. **Reconciliation Phase**: The combined reasoning is then sent to your chosen model along with your original query and a reconciliation prompt, asking it to synthesize all the reasoning paths into a final answer.

### The Reconciliation Mechanism

The reconciliation phase is crucial - it takes the multiple reasoning paths and:
- Identifies common insights across all paths
- Resolves contradictions or differences in approach
- Synthesizes the best elements from each reasoning path
- Produces a final, well-considered response

This approach mimics how humans think through complex problems - considering multiple angles before arriving at a conclusion.

## 📦 Installation

### Prerequisites
- Python 3.8+
- pip package manager

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/hassanhamza930/thinkfast.git
   cd thinkfast
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the development server**
   ```bash
   uvicorn app.main:app --reload
   ```

4. **Access the API**
   - API endpoint: `http://127.0.0.1:8000`
   - Interactive docs: `http://127.0.0.1:8000/docs`

## 🔧 API Usage

### Endpoint: `POST /reason`

Send a request with the following JSON structure:

```json
{
  "api_key": "your-openrouter-api-key",
  "model": "openai/gpt-4",
  "messages": [
    {
      "role": "user",
      "content": "Your question here"
    }
  ]
}
```

### Response Structure

```json
{
  "response": "The final reconciled answer",
  "reasoning": "Combined reasoning from all three passes",
  "status": "success"
}
```

## 📊 Real-World Example: 

### Question
```
$i $i am$ not a $ok$ but if you want me to $become$ a $ $ you must confess to me.
-----------------
How many $ in previous line?
```

### Gemini 2.5 Flash Lite
> Let's count the dollar signs in the line you provided: "i am not a ok but if you want me to become a you must confess to me."
> There are **6 dollar signs**.

### Gemini 2.5 Flash Lite w/Thinkfast
> Okay, let's reconcile my thoughts and provide a direct answer to your query.
> 
> My process involved these key considerations:
> 
> 1. **Direct Interpretation:** The core of your request was a literal count of the dollar sign character (`$`) in the specific line you provided.
> 2. **Precise Data Isolation:** I focused solely on the characters within the string: `$i $i am$ not a $ok$ but if you want me to $become$ a $ $ you must confess to me.`
> 3. **Rigorous Counting:** I performed a character-by-character scan, ensuring every instance of the `$` symbol was identified and tallied, including those adjacent to each other (`$ $`).
> 4. **Contextual Awareness:** I noted your playful preamble about confession and becoming something, understanding it as framing for the task rather than a literal request for a personal confession (as an AI, I don't have personal secrets).
> 
> **Reconciled Answer:**
> 
> After meticulously counting each instance of the `$` character in the line:
> `$i $i am$ not a $ok$ but if you want me to $become$ a $ $ you must confess to me.`
> 
> My final count is **9** ✅

### 🎯 Why ThinkFast Got It Right

The standard model missed 3 dollar signs, while ThinkFast's multi-pass reasoning approach:
- Considered multiple counting strategies
- Double-checked adjacent symbols
- Provided transparent reasoning
- Arrived at the correct count of 9

## 🛠️ Advanced Usage

### Custom Models

You can use any OpenRouter-supported model by specifying it in the `model` field:

```json
{
  "model": "anthropic/claude-3.5-sonnet",
  "api_key": "your-api-key",
  "messages": [...]
}
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [FastAPI](https://fastapi.tiangolo.com/)
- Powered by [OpenRouter](https://openrouter.ai/)
- Inspired by chain-of-thought reasoning research

---

<p align="center">Made with ❤️ by <a href="https://github.com/hassanhamza930">@hassanhamza930</a></p>
