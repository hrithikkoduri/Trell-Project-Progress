# Content Creation Crew

<div align="center">

[![Python](https://img.shields.io/badge/PYTHON_3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/)
[![CrewAI](https://img.shields.io/badge/CREWAI_0.86+-FF6B6B?style=for-the-badge&logo=robot&logoColor=white)](https://crewai.com)
[![OpenAI](https://img.shields.io/badge/OPENAI_API-412991?style=for-the-badge&logo=openai&logoColor=white)](https://openai.com/)
[![Pydantic](https://img.shields.io/badge/PYDANTIC_2.9+-E92063?style=for-the-badge&logo=pydantic&logoColor=white)](https://docs.pydantic.dev/)
[![FastAPI](https://img.shields.io/badge/FASTAPI_0.115-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![LangChain](https://img.shields.io/badge/LANGCHAIN_0.3+-000000?style=for-the-badge&logo=chainlink&logoColor=white)](https://www.langchain.com/)
[![PyTorch](https://img.shields.io/badge/PYTORCH_2.5-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)](https://pytorch.org/)
[![Trello](https://img.shields.io/badge/TRELLO_API-0052CC?style=for-the-badge&logo=trello&logoColor=white)](https://developer.atlassian.com/cloud/trello/)
[![License MIT](https://img.shields.io/badge/LICENSE_MIT-yellow?style=for-the-badge&logo=license&logoColor=white)](https://opensource.org/licenses/MIT)

</div>

A powerful multi-agent AI system built with [crewAI](https://crewai.com) that helps automate content creation and project analysis workflows. This system leverages multiple AI agents working together to collect data, perform analysis, and generate comprehensive reports.

## 🌟 Features

- Automated data collection from Trello boards
- Intelligent project analysis and blocker identification
- Comprehensive report generation in Markdown format
- Multi-agent collaboration for complex tasks
- Configurable agents and tasks through YAML files

## 🚀 Getting Started

### Prerequisites

- Python (>=3.10, <=3.13)
- [UV Package Manager](https://docs.astral.sh/uv/)

### Installation

1. Install UV if you haven't already:
```bash
git clone <repository-url>
cd content-creation-crew
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Configuration

1. Create a `.env` file in the root directory and add your API keys:
```bash
OPENAI_API_KEY=your_openai_api_key
TRELLO_API_KEY=your_trello_api_key
TRELLO_API_SECRET=your_trello_api_secret
TRELLO_BOARD_ID=your_board_id

```

2. Customize your agents and tasks:
- Modify `src/content_creation_crew/config/agents.yaml` for agent configurations
- Modify `src/content_creation_crew/config/tasks.yaml` for task definitions
- Update `src/content_creation_crew/crew.py` for custom logic and tools
- Adjust `src/content_creation_crew/main.py` for specific inputs

## 🎮 Usage

Run the crew from the project root:
```bash
crew run
```

This will start the crew and execute the tasks defined in your YAML files.

Additional commands:
Train the crew
```bash
crewai train <iterations> <filename>
```

Replay a specific task
```bash
crewai replay <task_id>
```

Run tests
```bash
crewai test <iterations> <openai_model_name>
```


## 🤖 Agent Roles

1. **Data Collection Agent**
   - Specializes in gathering project data from Trello
   - Equipped with custom tools for board and card data fetching

2. **Analysis Agent**
   - Analyzes collected data for insights
   - Identifies blockers, delays, and progress
   - Generates comprehensive reports

## 📊 Output

The system generates a detailed `report.md` file containing:
- Sprint Overview
- Task Summary
- Identified Issues and Blockers
- Progress Analysis
- Team Performance Metrics
- Action Items and Recommendations

## 🛠️ Project Structure

```
content-creation-crew/
├── src/
│   └── content_creation_crew/
│       ├── config/
│       │   ├── agents.yaml
│       │   └── tasks.yaml
│       ├── tools/
│       │   └── custom_tool.py
│       ├── crew.py
│       └── main.py
├── .env
├── pyproject.toml
└── README.md
```

For more detailed information, refer to the [crewAI documentation](https://crewai.com/docs).

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a PR.

## 📚 Documentation

For more detailed information, refer to the [crewAI documentation](https://crewai.com/docs).

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.