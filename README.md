# 📺 YouTube Video Summarizer (Powered by Gemini AI)

An AI-powered application that automatically generates concise summaries and key takeaways from YouTube videos. Built with **Python** and **Streamlit**, utilizing Google's **Gemini Pro** model to process video transcripts.

## 🚀 Features

* **Instant Summaries:** Extracts transcripts from YouTube videos and generates bullet-point summaries.
* **Time-Saving:** Converts long educational or informational videos into quick-read notes.
* **Visual Interface:** User-friendly web UI built with Streamlit.
* **Thumbnail Integration:** Fetches and displays the video thumbnail for verification.

## 🛠️ Tech Stack

* **Language:** Python 3.10+
* **Frontend:** Streamlit
* **AI Model:** Google Gemini Pro (via `google-generativeai`)
* **Libraries:**
    * `youtube-transcript-api` (Data Extraction)
    * `python-dotenv` (Environment Management)

## 📂 Project Structure

```bash
/Youtube-Video-Summarizer
│
├── app.py              # Main application logic
├── requirements.txt    # Project dependencies
├── .env.example        # Template for API keys
└── README.md           # Documentation
