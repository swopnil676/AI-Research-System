# 🤖 Multi-Agent AI Research System

An AI-powered research assistant built with **Python, LangChain, Groq, Tavily, and Streamlit** that automates the research process — from searching the web and extracting relevant information to generating structured research reports and evaluating their quality.

The system combines AI-powered workflows with web search and scraping to transform research queries into informative, source-backed reports.

## 🖥️ Application Preview

<img width="1917" height="972" alt="Screenshot 2026-11-04 213712" src="https://github.com/user-attachments/assets/7d51565a-b1ba-4702-8960-a89f76d9d6a9" />

## 🌐 Live Application

🚀 **Live Demo:** [Try the Multi-Agent AI Research System](https://ai-research-system-6gg23ngynkanpldfcynmtt.streamlit.app/)

## ✨ Key Features

- 🔍 **Automated Web Search** – Retrieve recent and relevant information using the Tavily Search API.
- 🌐 **Intelligent Web Scraping** – Extract meaningful webpage content using BeautifulSoup.
- 🤖 **AI-Powered Research Workflow** – Organize research into specialized processing stages.
- 🧠 **Research Report Generation** – Generate detailed, structured, and informative reports using an LLM.
- 📝 **AI-Powered Critic** – Evaluate generated reports, identify weaknesses, and provide improvement suggestions with a score.
- 🔗 **Source References** – Include source titles and URLs for transparency and further reading.
- ⚡ **Interactive Streamlit UI** – Explore the research workflow through a clean web interface.
- 📥 **Report Export** – Download generated research reports.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| LangChain | LLM integration and AI workflows |
| Groq | Fast LLM inference |
| Tavily | Real-time web search |
| BeautifulSoup | Webpage content extraction |
| Requests | HTTP requests and webpage access |
| Streamlit | Interactive web application |
| Python-dotenv | Local environment variable management |

## 🏗️ System Architecture

The system follows a multi-stage research workflow:

```text
             User Research Query
                     |
                     ▼
              Search Stage
                     |
                     ▼
              Tavily Search
                     |
                     ▼
          Collect Relevant Sources
                     |
                     ▼
               Scraping Stage
                     |
                     ▼
          Extract Webpage Content
                     |
                     ▼
              Writer Stage
                     |
                     ▼
          Generate Research Report
                     |
                     ▼
               Critic Stage
                     |
                     ▼
       Evaluate Report & Assign Score
                     |
                     ▼
             Final Research Report
```

## 📂 Project Structure

```text
Multi-Agent-AI-Research-System/
│
├── app.py                  # Streamlit application
├── agents.py               # LLM, writer and critic chains
├── tools.py                # Web search and scraping tools
├── pipeline.py             # Research pipeline
├── requirements.txt        # Project dependencies
├── example.txt             # Example research content
├── .gitignore              # Git ignored files
│
└── README.md
```

*Note: Update the project structure if your actual repository contains different files.*

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the Project Directory

```bash
cd Multi-Agent-AI-Research-System
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure API Keys

Create a `.env` file in the project root directory:

```env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

Get your API keys:

- [Groq API](https://console.groq.com/keys)
- [Tavily API](https://app.tavily.com/)

**For Streamlit Cloud deployment:** Add the same keys under your application's **Settings → Secrets** using TOML format:

```toml
GROQ_API_KEY = "your_groq_api_key"
TAVILY_API_KEY = "your_tavily_api_key"
```

🔐 **Security:** Never commit `.env` or `.streamlit/secrets.toml` to GitHub. Add both to `.gitignore`.

### 6. Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

## 💡 Example Research Queries

Try researching topics such as:

- Impact of geopolitical conflicts on global stock markets.
- Latest developments in Artificial Intelligence.
- Future of Generative AI and autonomous AI agents.
- Applications of Machine Learning in healthcare.
- Global economic trends and their potential impact.
- Advancements in Large Language Models.

## 🎯 Project Objectives

The main objective of this project is to explore how AI-powered workflows can automate complex research tasks.

Through this project, I explored:

- Building AI workflows using LangChain.
- Integrating LLMs with external tools and APIs.
- Automating web search and content extraction.
- Generating structured research reports.
- Implementing AI-based report evaluation.
- Deploying an AI-powered application using Streamlit Cloud.

## 🚀 Future Improvements

- Multi-source fact verification and cross-referencing.
- Improved citation accuracy and source validation.
- Research history and report management.
- More advanced agent collaboration.
- PDF report generation and export.
- Enhanced evaluation with more detailed scoring criteria.

## 👨‍💻 Author

**Swopnil Biswas**  
Python Developer | AI/ML Engineer

- **GitHub:** [@swopnil676](https://github.com/swopnil676)
- **LinkedIn:** [Swopnil Biswas](https://www.linkedin.com/in/swopnilbiswas/)

---

⭐ If you find this project interesting, consider giving it a star!

*Built with Python, AI, and a passion for learning and innovation.*
