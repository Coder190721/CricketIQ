# 🏏 CricketIQ

A comprehensive cricket statistics agent powered by Google ADK (Agent Development Kit) and ESPN Cricinfo data. This agent provides detailed player statistics, comparisons, and insights across all cricket formats (Test, ODI, T20).

[![GitHub](https://img.shields.io/badge/GitHub-CricketIQ-blue)](https://github.com/Coder190721/CricketIQ)
[![Python](https://img.shields.io/badge/Python-3.8+-green)](https://python.org)
[![Gradio](https://img.shields.io/badge/Gradio-Web%20UI-orange)](https://gradio.app)

## ✨ Features

- **📊 Player Statistics**: Get comprehensive batting, bowling, and fielding records
- **⚖️ Player Comparison**: Compare statistics between any two players
- **💡 Cricket Insights**: AI-powered analysis and predictions
- **💬 Interactive Chat**: Natural language interface for cricket queries
- **🌐 Web Interface**: Beautiful Gradio-based web UI
- **🔧 MCP Server**: Model Context Protocol server for integration

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Google API Key (for Gemini AI)
- Internet connection for data fetching

### Installation

1. **Clone this repository**
```bash
git clone https://github.com/Coder190721/CricketIQ.git
cd CricketIQ
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Set up environment variables**
```bash
# Copy the example environment file
cp env_example.txt .env

# Edit .env and add your Google API key
export GOOGLE_API_KEY="your-google-api-key-here"
```

4. **Get your Google API Key**
   - Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Create a new API key
   - Add it to your `.env` file

### Running the Agent

#### Option 1: Web Interface (Recommended)
```bash
python cricket_gradio_demo.py
```
Then open your browser to `http://localhost:7860`

#### Option 2: Command Line Interface
```bash
python cricket_agent.py
```

#### Option 3: MCP Server Only
```bash
python cricket_mcp_server.py
```

## 🎯 Usage Examples

### Player Analysis
```python
# Analyze Virat Kohli's Test statistics
result = agent.analyze_player("Virat Kohli", "Test")
```

### Player Comparison
```python
# Compare Sachin Tendulkar and Brian Lara in ODI cricket
result = agent.compare_players("Sachin Tendulkar", "Brian Lara", "ODI")
```

### Cricket Insights
```python
# Get insights about best all-rounders
result = agent.get_cricket_insights("Who are the best all-rounders in T20 cricket?")
```

### Interactive Chat
```python
# Chat with the agent
response = agent.chat("Tell me about the highest individual scores in Test cricket")
```

## 🛠️ Architecture

### Components

1. **Cricket Agent** (`cricket_agent.py`)
   - Main agent class using Google ADK
   - Integrates with Gemini AI for analysis
   - Manages MCP server communication

2. **MCP Server** (`cricket_mcp_server.py`)
   - Model Context Protocol server
   - ESPN Cricinfo data scraping
   - Statsguru integration
   - Comprehensive statistics extraction

3. **Gradio Demo** (`cricket_gradio_demo.py`)
   - Web-based user interface
   - Interactive player analysis
   - Real-time chat functionality

### Data Sources

- **ESPN Cricinfo**: Primary source for player statistics
- **Statsguru**: Advanced analytics and historical data
- **Google Search**: Player discovery and additional data

## 📊 Available Statistics

### Batting Statistics
- Matches, Innings, Runs, Average
- Strike Rate, Hundreds, Fifties
- Highest Score, Career Summary

### Bowling Statistics
- Matches, Innings, Balls, Runs
- Wickets, Average, Economy Rate
- Strike Rate, Best Figures

### Fielding Statistics
- Catches, Stumpings, Dismissals
- Fielding efficiency metrics

## 🔧 Configuration

### Environment Variables

```bash
# Required
GOOGLE_API_KEY=your_google_api_key_here

# Optional
GEMINI_MODEL=gemini-2.5-flash
GEMINI_TEMPERATURE=0.7
GEMINI_MAX_TOKENS=8192
LOG_LEVEL=INFO
```

### Model Configuration

The agent uses Google's Gemini model with the following default settings:
- Model: `gemini-2.5-flash`
- Temperature: `0.7` (balanced creativity/accuracy)
- Max Tokens: `8192`

## 🎨 Web Interface Features

### Player Analysis Tab
- Input player name and format
- Get comprehensive statistical analysis
- AI-powered insights and recommendations

### Player Comparison Tab
- Compare any two players
- Side-by-side statistical comparison
- Format-specific analysis

### Cricket Insights Tab
- Ask questions about cricket
- Get AI-powered insights
- Historical analysis and predictions

### Chat Interface
- Natural language conversation
- Context-aware responses
- Multi-turn conversations

## 🔍 API Reference

### CricketAgent Class

```python
class CricketAgent:
    def __init__(self, config: AgentConfig = None)
    async def analyze_player(self, player_name: str, format_type: str = "all") -> str
    async def compare_players(self, player1: str, player2: str, format_type: str = "all") -> str
    async def get_cricket_insights(self, query: str) -> str
    async def chat(self, user_input: str) -> str
```

### MCP Server Tools

```python
@mcp.tool()
def get_player_comprehensive_stats(player_name: str, format_type: str = "all") -> Dict[str, Any]

@mcp.tool()
def search_players(query: str, limit: int = 10) -> List[Dict[str, Any]]

@mcp.tool()
def get_player_batting_stats(player_name: str, format_type: str = "all") -> Dict[str, Any]

@mcp.tool()
def get_player_bowling_stats(player_name: str, format_type: str = "all") -> Dict[str, Any]

@mcp.tool()
def get_player_fielding_stats(player_name: str, format_type: str = "all") -> Dict[str, Any]

@mcp.tool()
def compare_players(player1: str, player2: str, format_type: str = "all") -> Dict[str, Any]
```

## 🚨 Error Handling

The agent includes comprehensive error handling for:
- Network connectivity issues
- Invalid player names
- Missing data on ESPN Cricinfo
- API rate limiting
- Model generation errors

## 📝 Example Queries

### Player Analysis
- "Analyze Virat Kohli's Test career"
- "Tell me about Sachin Tendulkar's ODI statistics"
- "What are Brian Lara's batting records?"

### Player Comparison
- "Compare Sachin Tendulkar and Brian Lara"
- "Who's better: Virat Kohli or Steve Smith in T20?"
- "Compare the bowling records of Wasim Akram and Glenn McGrath"

### Cricket Insights
- "Who has the highest Test average?"
- "Best all-rounders in cricket history"
- "Most successful T20 batsmen"
- "Greatest bowling performances"

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License. See the LICENSE file for details.

## ⚠️ Disclaimer

This tool scrapes data from public websites (ESPN Cricinfo). The authors are not responsible for any misuse or violation of website terms of service. Use responsibly and ensure compliance with applicable terms and conditions.

## 🆘 Support

If you encounter any issues:
1. Check the error messages in the console
2. Verify your Google API key is correct
3. Ensure you have internet connectivity
4. Check the ESPN Cricinfo website is accessible

## 🔮 Future Enhancements

- [ ] Real-time match data integration
- [ ] Advanced statistical modeling
- [ ] Player performance predictions
- [ ] Team analysis capabilities
- [ ] Historical match analysis
- [ ] Mobile app interface
- [ ] API for third-party integration

---

**🏏 Cricket Statistics Agent** - Powered by Google ADK & ESPN Cricinfo
