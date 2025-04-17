# AI Agents Framework

A versatile framework for building and deploying AI agents for research and task automation using Large Language Models.

## 🚀 Features

- **Research Agent**: Automated research assistant using LangChain, Groq, and multiple search tools
- **Pydantic AI Agents**: Modular agents built with the Pydantic-AI framework
- **Multi-Component Protocol (MCP)**: Advanced agent capabilities with MCP server integration
- **Robust Logging**: Integrated Logfire for comprehensive monitoring and debugging

## 📋 Requirements

- Python 3.8+
- API keys for Groq, Logfire, and Mistral

## 🔧 Installation

1. Clone the repository:

```bash
git clone https://github.com/SohamChaudhari2004/AI-Agents.git
cd "AI Agents"
```

2. Install required dependencies:

```bash
pip install -r requirements.txt
```

3. Set up environment variables:

```bash
cp .env.example .env
```

4. Update the `.env` file with your API keys:

```
GROQ_API_KEY = your_groq_api_key
LOGFIRE_TOKEN = your_logfire_token
MISTRAL_API_KEY = your_mistral_api_key
```

## 🔍 Research Agent

The Research Agent leverages LangChain, Wikipedia, and DuckDuckGo to conduct automated research on topics.

### Usage

```bash
cd ResearchAgent
python main.py
```

When prompted, enter your research query. The agent will:

1. Search the web for relevant information
2. Summarize findings
3. Save results to a structured text file
4. Provide sources for further exploration

## 🤖 Pydantic AI Agents

Two agent implementations are provided using the Pydantic-AI framework:

### Basic Agent

```bash
cd PydanticAIAgents
python agent.py
```

### Advanced Agent with MCP

```bash
cd PydanticAIAgents
python agent_with_mcp.py
```

## 📁 Project Structure

```
AI Agents/
├── .env.example           # Example environment variables
├── requirements.txt       # Project dependencies
├── ResearchAgent/
│   ├── main.py            # Research agent entry point
│   ├── tools.py           # Search and utility tools
│   └── research_results.txt # Saved research results
└── PydanticAIAgents/
    ├── agent.py           # Basic Pydantic AI agent
    ├── agent_with_mcp.py  # Advanced agent with MCP
    ├── config.py          # Configuration loader
    └── utils/
        ├── groq_model.py  # Groq LLM configuration
        ├── logfire_config.py # Logging setup
        └── mcp_server.py  # MCP server configuration
```

## ⚙️ Configuration

The project uses environment variables for configuration. Key variables include:

- `GROQ_API_KEY`: API key for Groq LLM services
- `LOGFIRE_TOKEN`: Token for Logfire logging
- `MISTRAL_API_KEY`: API key for Mistral AI (alternative LLM)


## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.
