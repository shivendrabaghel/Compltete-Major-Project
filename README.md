# YouTube Transcript Summarizer (Flask + Gemini AI)

This project is a **Flask-based web app** that allows users to extract and summarize YouTube video transcripts using **Google Gemini AI**. Simply enter a YouTube video URL, and the app fetches the transcript, then summarizes it using Google's **Gemini-1.5-Pro** model.

---

## 🚀 Features
- Extracts **YouTube video transcripts** (English & Hindi supported).
- Uses **Google Gemini AI** to summarize transcripts.
- Simple **Flask-based web interface**.
- **Streamlit app** for an alternative UI.
- **Error handling** for invalid URLs, missing transcripts, or API issues.
- **Secure API key management** using `.env` file.

---

## 📦 Tech Stack
- **Backend:** Flask, Python
- **AI Model:** Google Gemini API (gemini-1.5-pro)
- **Frontend:** HTML + Bootstrap
- **Alternative UI:** Streamlit
- **Environment Variables:** Python Dotenv

---

## 📂 Project Structure
```
Major-Project/
│── templates/
│   └── template.html
│── .env
│── flask.py
│── streamlit_app.py
│── requirements.txt
│── README.md
```

---

## 🛠 Installation & Setup

### 1️⃣ Clone this repository inside the `Major-Project` folder
```bash
git clone https://github.com/your-username/youtube-transcript-summarizer.git Major-Project/youtube-transcript-summarizer
cd Major-Project/youtube-transcript-summarizer
```

### 2️⃣ Set up a virtual environment (Recommended)
```bash
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Set up `.env` file for API Keys
Create a `.env` file in the project root and add your **Gemini API Key**:
```ini
GEMINI_API_KEY=your_actual_api_key_here
```

> 🔹 Get your Google Gemini API key from [Google AI Studio](https://ai.google.dev/)

### 5️⃣ Run the Flask App
```bash
python flask.py
```
Then open **http://127.0.0.1:5000/** in your browser.

### 6️⃣ Run the Streamlit App (Optional)
```bash
streamlit run streamlit_app.py
```
This will launch an alternative **Streamlit UI** in your browser.

---

## 📝 Usage
1. Open the Flask or Streamlit web app.
2. Enter a **YouTube video URL**.
3. Click on **"Get Transcript"**.
4. The transcript and summarized text will be displayed.

---

## 🔥 Troubleshooting

### ❌ `FileNotFoundError: template.html not found`
✔ Ensure your project structure has a **`templates/`** folder with `template.html` inside it.

### ❌ `Error: models/gemini-1.5-pro not found`
✔ Run this to check available models:
```python
import google.generativeai as genai
genai.configure(api_key="your_gemini_api_key")
models = genai.list_models()
for model in models:
    print(model.name)
```
✔ Use a valid model name from the list.

### ❌ `Error 429: You exceeded your quota`
✔ Check your **Google AI usage limit** [here](https://ai.google.dev/) and upgrade your plan if needed.

---

## 📜 License
This project is open-source under the **MIT License**.

---

## 🙌 Contributing
Feel free to **fork** this repo, create a branch, and submit a **pull request**! 🚀

