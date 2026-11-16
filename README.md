# 🤖 Multi-Agent AI Research System

An AI-powered research system built with **LangChain, OpenAI, Tavily, and Web Scraping** that searches the internet, extracts information from relevant webpages, and generates detailed research summaries.
The system uses multiple AI agents to automate the research process and collect information from reliable web sources.

## 🖥️ Application Preview

<img width="1917" height="972" alt="image" src="https://github.com/user-attachments/assets/0d7ca70c-569c-4e67-9500-fd4d92ef62b7" />

## 🌐 Live Application

🚀 **Live Demo:** [Click here to use the Multi-Agent AI Research System](https://multi-agent-ai-research-system-u6gv539zu4yqiyage9kgyc.streamlit.app/)

## 🚀 Features

- 🔍 **Automated Web Search** – Search for recent and relevant information using Tavily.
- 🌐 **Web Scraping** – Extract webpage content using BeautifulSoup.
- 🤖 **Multi-Agent Architecture** – Divide research tasks between specialized AI agents.
- 🧠 **AI-Powered Analysis** – Analyze collected information using OpenAI models.
- 📚 **Detailed Research Summaries** – Generate structured and informative research reports.
- 🔗 **Source References** – Include article titles and URLs for further reading.
- ⚡ **LangChain Integration** – Build intelligent agent workflows using LangChain.

## 🛠️ Tech Stack

| Technology         | Purpose                             |
| ------------------ | ----------------------------------- |
| Python             | Core programming language           |
| LangChain          | Agent development and orchestration |
| LangGraph          | Agent workflow management           |
| OpenAI GPT-4o mini | Language model                      |
| Tavily             | Web search                          |
| BeautifulSoup      | Web scraping                        |
| Requests           | HTTP requests                       |
| Python-dotenv      | Environment variable management     |

## 🏗️ How It Works

```text
          User Research Query
                  |
                  ▼
          Search Agent
                  |
                  ▼
           Tavily Search
                  |
                  ▼
       Collect Relevant URLs
                  |
                  ▼
          Web Scraping
                  |
                  ▼
       Extract Webpage Content
                  |
                  ▼
          Research Agent
                  |
                  ▼
        Analyze Information
                  |
                  ▼
         Final Research Report
```

## 📂 Project Structure

```text
Multi-Agent-AI-Research-System/
│
├── app.py
├── tools.py
├── agents.py
├── requirements.txt
├── example.txt
├── pipeline.py
├── .gitignore
│
└── README.md
```

*Note: Adjust the filenames according to your actual project structure.*

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the project directory

```bash
cd Multi-Agent-AI-Research-System
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure API keys

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_openai_api_key
TAVILY_API_KEY=your_tavily_api_key
```

Get your API keys:

- [OpenAI API](https://platform.openai.com/api-keys)
- [Tavily API](https://app.tavily.com/)

**Important:** Never share or upload your API keys to GitHub.

### 6. Run the project

```bash
python app.py
```

## 💡 Example Research Queries

- Impact of war on global stock markets.
- Latest developments in Artificial Intelligence.
- Future of Generative AI.
- Applications of Machine Learning in healthcare.
- Global economic trends and their impact.

## 🎯 Project Goal

The main goal of this project is to explore how multiple AI agents can collaborate to perform automated research, retrieve information from the web, analyze sources, and generate meaningful research reports.

## 👨‍💻 Author

**Swopnil Biswas**

- GitHub: [@swopnil676](https://github.com/swopnil676)
- LinkedIn: [Swopnil Biswas](https://www.linkedin.com/in/swopnilbiswas/)

---

⭐ If you find this project interesting, consider giving it a star!
