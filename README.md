<div align="center">

# 🤖 LabPiPe AI Agents Framework

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Ollama](https://img.shields.io/badge/Ollama-compatible-green)](https://ollama.ai/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Stars](https://img.shields.io/github/stars/marouandoulahiane/LabPiPe?style=social)](https://github.com/marouandoulahiane/LabPiPe/stargazers)

**Run powerful AI agents locally with your own models - No API keys, no cloud dependency, full privacy**

[Features](#-features) • 
[Why LabPiPe?](#-why-labpipe-ai-agents) • 
[Installation](#-installation) • 
[Quick Start](#-quick-start) • 
[Documentation](#-documentation) • 
[Contributing](#-contributing)

</div>

## 🌟 Features

- **🏠 100% Local Execution**: All processing happens on your machine - no data leaves your system
- **🧠 LLM Flexibility**: Use any Ollama-compatible model (Mistral, Llama2, Phi, etc.)
- **🔌 Modular Architecture**: Easily add new tools and extend functionality
- **🛠️ Built-in Tools**:
  - 🧮 **Calculator Engine**: Perform mathematical operations with natural language
  - 🔄 **Text Utilities**: String reversal and manipulation tools
  - 📊 **System Monitor**: Track CPU, memory and disk usage in real-time
- **🔍 Task Routing**: Smart delegation to appropriate tools based on user input
- **🖥️ Terminal Interface**: Clean, color-coded outputs for improved readability

## 🔍 Why LabPiPe AI Agents?

While cloud-based AI solutions dominate the market, LabPiPe takes a different approach:

| Feature | LabPiPe | Cloud-based AI Services |
|---------|---------|-------------------------|
| Privacy | ✅ 100% local processing | ❌ Data sent to third parties |
| Cost | ✅ Free, no usage limits | ❌ Pay-per-token or subscription |
| Customization | ✅ Add your own tools easily | ❌ Limited to provided APIs |
| Connection | ✅ Works offline | ❌ Requires internet |
| Control | ✅ Choose your models & parameters | ❌ Black box implementations |

Perfect for developers who want to:
- Build AI assistants without cloud dependencies
- Learn how AI agent architectures work
- Create specialized tools for specific domains
- Ensure complete data privacy

## 📋 Requirements

- Python 3.8+
- [Ollama](https://ollama.ai/) installed and running
- 4GB+ RAM (8GB+ recommended for larger models)
- Sufficient disk space for LLM models (typically 4-8GB per model)

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/marouandoulahiane/simple_ai_agent.git
cd LabPiPe
```

### 2. Create and activate virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r simple_ai_agent/requirements.txt
```

### 4. Install and start Ollama

Follow instructions at [ollama.ai](https://ollama.ai/) to install Ollama for your platform.

Pull your preferred model (Mistral recommended for best results):
```bash
ollama pull mistral
```

Start the Ollama server:
```bash
ollama serve
```



## 🏁 Quick Start

Run the main script:

```bash
python -m simple_ai_agent.main
```

### Example interactions:

```
Ask me anything: Calculate 15 plus 7
The answer is: 22

Ask me anything: Reverse the word 'hello world'
The reversed string is: dlrow olleh

Ask me anything: What is the current CPU usage?
{
    "cpu_usage": 32.5,
    "memory_usage": 68.2,
    "disk_usage": 45.7,
    "top_processes": [
        {
            "name": "firefox",
            "pid": 1234,
            "cpu_usage": 12.3
        },
        {
            "name": "python",
            "pid": 5678,
            "cpu_usage": 8.7
        }
    ]
}
```

## 🧩 Extending with Custom Tools

LabPiPe is designed to be easily extendable. Add your own tools in 3 simple steps:

1. Create your tool function in `simple_ai_agent/toolboxs/tools/`
2. Add proper docstrings (essential for the agent to understand the tool)
3. Import and add your tool to the list in `main.py`

Example of a custom tool:

```python
def translate_text(input_dict):
    """
    Translates text from one language to another.
    
    Parameters:
    input_dict (dict): Dictionary with 'text' and 'target_language' keys
    
    Returns:
    str: The translated text
    """
    # Your translation implementation here
    return f"Translated: {result}"
```

## 📚 Documentation

For detailed documentation on:
- [Architecture Overview](docs/architecture.md)
- [Creating Custom Tools](docs/custom_tools.md)
- [Supported Models](docs/models.md)
- [Advanced Configuration](docs/configuration.md)

Visit our [Wiki](https://github.com/marouandoulahiane/LabPiPe/wiki) for tutorials and examples.

## 👥 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Ollama](https://ollama.ai/) for making local LLMs accessible
- [Vipra Singh](https://medium.com/@vipra_singh/ai-agents-build-an-agent-from-scratch-part-2-7ae11840c93a) for the excellent tutorial and guidance on building AI agents from scratch
- All the contributors and the open source community
- You, for checking out this project!

---

<div align="center">
    <p><b>Star this repo if you found it useful!</b></p>
    <p>
        <a href="https://github.com/marouandoulahiane/LabPiPe/issues">Report Bug</a> •
        <a href="https://github.com/marouandoulahiane/LabPiPe/issues">Request Feature</a>
    </p>
</div>
