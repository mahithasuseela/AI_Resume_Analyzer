# 🤖 AI Resume Analyzer

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![AI](https://img.shields.io/badge/AI%20Powered-6E40C9?style=for-the-badge&logo=anthropic&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

**An AI-powered tool that analyzes resumes and provides smart, actionable feedback to help job seekers land their dream job.**

[Features](#-features) • [Demo](#-demo) • [Installation](#-installation) • [Usage](#-usage) • [Contributing](#-contributing)

</div>

---

## ✨ Features

- 📄 **Resume Parsing** — Extracts key information from PDF/text resumes
- 🤖 **AI Analysis** — Uses AI to evaluate content, structure, and keywords
- 💡 **Smart Feedback** — Gives specific, actionable improvement suggestions
- 🎯 **Job Match Score** — Rates how well resume matches a job description
- 📊 **Skills Gap Analysis** — Identifies missing skills for target roles

---

## 🖥️ Demo

```
Input:  Upload your resume (PDF or text)
Output: Detailed AI feedback with score and suggestions
```

---

## ⚙️ Installation

### Prerequisites
- Python 3.8+
- pip

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/mahithasuseela/AI_Resume_Analyzer.git

# 2. Navigate to project folder
cd AI_Resume_Analyzer

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up environment variables
cp .env.example .env
# Add your API key to .env file

# 5. Run the application
python app.py
```

---

## 🚀 Usage

```python
# Example usage
from analyzer import ResumeAnalyzer

analyzer = ResumeAnalyzer()
result = analyzer.analyze("path/to/resume.pdf")

print(result.score)        # Overall score out of 100
print(result.feedback)     # Detailed feedback
print(result.suggestions)  # List of improvements
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Language | Python 3.8+ |
| AI Model | OpenAI / Claude API |
| PDF Parsing | PyPDF2 / pdfplumber |
| Backend | Flask |
| Frontend | HTML, CSS, JavaScript |

---

## 📁 Project Structure

```
AI_Resume_Analyzer/
├── app.py              # Main application entry point
├── analyzer.py         # Core AI analysis logic
├── requirements.txt    # Python dependencies
├── .env.example        # Environment variables template
├── templates/
│   └── index.html      # Frontend UI
├── static/
│   ├── style.css       # Styling
│   └── script.js       # Frontend logic
└── README.md
```

---

## 🤝 Contributing

Contributions are welcome! Here's how:

```bash
# 1. Fork the repo
# 2. Create a feature branch
git checkout -b feat/your-feature-name

# 3. Commit your changes
git commit -m "feat: add your feature"

# 4. Push and open a Pull Request
git push origin feat/your-feature-name
```

---

## 📜 License

This project is licensed under the MIT License — see [LICENSE](LICENSE) for details.

---

<div align="center">

Made with ❤️ by [Mahitha Suseela](https://github.com/mahithasuseela)

⭐ **Star this repo if you found it helpful!**

</div>
