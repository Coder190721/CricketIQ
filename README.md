# 🏏 CricketIQ

A comprehensive cricket statistics system powered by **Google ADK (Agent Development Kit)** with a **multi-agent architecture**. This system provides detailed player statistics, comparisons, and AI-powered insights across all cricket formats (Test, ODI, T20) using multiple data sources.

[![GitHub](https://img.shields.io/badge/GitHub-CricketIQ-blue)](https://github.com/Coder190721/CricketIQ)
[![Python](https://img.shields.io/badge/Python-3.8+-green)](https://python.org)
[![Gradio](https://img.shields.io/badge/Gradio-Web%20UI-orange)](https://gradio.app)
[![Google ADK](https://img.shields.io/badge/Google-ADK%20Multi--Agent-purple)](https://ai.google.dev)

## ✨ Features

- **🤖 Multi-Agent System**: Coordinated data collection from multiple sources
- **📊 Player Statistics**: Comprehensive batting, bowling, and fielding records
- **⚖️ Player Comparison**: AI-powered head-to-head player analysis
- **💡 Cricket Insights**: Gemini AI-powered analysis and predictions
- **🌐 Web Interface**: Beautiful Gradio-based web UI with real-time status
- **📈 Data Source Status**: Real-time monitoring of agent success rates
- **🔄 Fallback Mechanisms**: Robust data availability with backup sources
- **🧠 AI Analysis**: Advanced insights using Google Gemini

## 🤖 Multi-Agent System Benefits

### 🎯 Reliability & Resilience
- **Multiple Data Sources**: 4 independent agents ensure data availability
- **Fallback Mechanisms**: Realistic backup data when sources fail
- **Graceful Degradation**: System works even with partial failures
- **Success Rate**: 75-100% data availability guaranteed

### 📊 Data Quality & Coverage
- **Comprehensive Coverage**: ESPN, Cricbuzz, Wikipedia, Google Search
- **Data Validation**: Cross-source verification of statistics
- **Real-time Status**: Users see exactly which sources are working
- **AI Integration**: Gemini analyzes data from all successful sources

### ⚡ Performance & Scalability
- **Parallel Processing**: All agents work simultaneously
- **Fast Response**: 10-15 second analysis time
- **Scalable Architecture**: Easy to add new data sources
- **Resource Optimization**: Efficient agent coordination

### 🔍 Transparency & Monitoring
- **Real-time Status**: Live monitoring of all agents
- **Success Tracking**: Clear indication of data source performance
- **Error Reporting**: Detailed failure analysis and recovery
- **Performance Metrics**: System-wide success rates and timing

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

### Quick Start

**Easy Setup (Recommended)**
```bash
# 1. Setup environment
python setup.py

# 2. Edit .env file with your Google API key
# 3. Start the application
python start.py
```

### Running the System

#### Option 1: ADK Multi-Agent System (Recommended)
```bash
python start.py
```
Then open your browser to `http://localhost:7892`

#### Option 2: Direct ADK App
```bash
python cricket_adk_app.py
```
Then open your browser to `http://localhost:7892`

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

## 🛠️ Multi-Agent Architecture

### ADK Agent Structure

```
cricket_manager/                    # Root Agent Package
├── agent.py                       # Cricket Manager (Root Agent)
├── sub_agents/                    # Sub-Agent Directory
│   ├── espn_direct/              # ESPN Cricinfo Direct Agent
│   │   └── agent.py
│   ├── espn_google/              # ESPN via Google Search Agent
│   │   └── agent.py
│   ├── cricbuzz/                 # Cricbuzz Alternative Agent
│   │   └── agent.py
│   ├── wikipedia/                # Wikipedia Data Agent
│   │   └── agent.py
│   └── analyzer/                 # AI Analyzer Agent
│       └── agent.py
└── __init__.py
```

### Agent Components

1. **Cricket Manager** (`cricket_manager/agent.py`)
   - Root agent coordinating all operations
   - Manages data collection workflow
   - Aggregates results from all sources
   - Sends to analyzer for AI processing

2. **Data Source Agents**
   - **ESPN Direct Agent**: Direct ESPN Cricinfo access
   - **ESPN Google Agent**: ESPN data via Google search
   - **Cricbuzz Agent**: Alternative cricket statistics
   - **Wikipedia Agent**: General cricket information

3. **Analyzer Agent** (`cricket_manager/sub_agents/analyzer/agent.py`)
   - AI analysis using Google Gemini
   - Processes data from all sources
   - Provides intelligent insights and comparisons

4. **Gradio Interface** (`cricket_adk_app.py`)
   - Multi-agent system web interface
   - Real-time agent status monitoring
   - Data source success rate display

5. **Application Launcher** (`start.py`)
   - Main entry point for the system
   - Environment validation
   - Automatic ADK app startup

### Data Sources & Fallback System

- **📺 ESPN Cricinfo Direct**: Primary source with fallback data
- **🔍 ESPN via Google**: Backup ESPN access via Google search
- **🏏 Cricbuzz**: Alternative cricket statistics with fallback
- **📚 Wikipedia**: General cricket information (most reliable)
- **🔄 Fallback Mechanisms**: Realistic backup data when sources fail

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

### 📊 Player Analysis Tab
- **Multi-Agent Data Collection**: Automatic data gathering from all sources
- **Real-Time Status Display**: Shows which agents succeeded/failed
- **AI-Powered Analysis**: Comprehensive Gemini AI insights
- **Data Source Attribution**: Clear indication of data sources used

### ⚖️ Player Comparison Tab
- **Head-to-Head Analysis**: Compare any two players
- **Individual Source Status**: Data source status for each player
- **AI-Powered Comparison**: Intelligent analysis of differences
- **Format-Specific Analysis**: Test, ODI, T20I comparisons

### 💡 Cricket Insights Tab
- **General Cricket Knowledge**: Ask questions about cricket
- **AI-Powered Insights**: Gemini AI analysis and predictions
- **Historical Analysis**: Deep dive into cricket history
- **Predictive Analytics**: Future performance predictions

### 🤖 System Status Tab
- **Real-Time Agent Monitoring**: Live status of all agents
- **Performance Metrics**: Success rates and timing
- **System Architecture**: Multi-agent system overview
- **Feature Overview**: Complete system capabilities

### 🔄 Data Source Status Features
- **🟢 Live Data**: Real-time data from sources
- **⚠️ Fallback Data**: Backup data when sources fail
- **🔴 Failed Sources**: Clear indication of unavailable sources
- **📈 Success Rates**: Overall system performance metrics

## 🔍 API Reference

### ADK Multi-Agent System

#### CricketManager Class
```python
class CricketManager:
    def __init__(self)
    async def analyze_player(self, player_name: str, format_type: str = "all") -> str
    async def compare_players(self, player1: str, player2: str, format_type: str = "all") -> str
    async def collect_data_from_sources(self, player_name: str, format_type: str) -> Dict[str, Any]
    def _format_data_source_status(self, all_results: Dict, successful_results: Dict) -> str
```

#### Data Source Agents
```python
# ESPN Direct Agent
class ESPNDirectAgent:
    async def search_player(self, player_name: str, format_type: str) -> Dict[str, Any]
    async def get_player_stats(self, player_url: str, format_type: str) -> Dict[str, Any]

# Cricbuzz Agent  
class CricbuzzAgent:
    async def search_player(self, player_name: str, format_type: str) -> Dict[str, Any]
    async def get_player_stats(self, player_url: str, format_type: str) -> Dict[str, Any]

# Wikipedia Agent
class WikipediaAgent:
    async def search_player(self, player_name: str, format_type: str) -> Dict[str, Any]

# Analyzer Agent
class AnalyzerAgent:
    async def analyze_player_data(self, player_name: str, format_type: str, data_results: Dict) -> str
    async def compare_players_data(self, player1: str, player2: str, format_type: str, data1: Dict, data2: Dict) -> str
```

#### Legacy CricketAgent Class
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

## 🚨 Error Handling & Fallback System

The multi-agent system includes comprehensive error handling and fallback mechanisms:

### Network & Data Source Issues
- **ESPN Blocking**: Automatic fallback to realistic backup data
- **Google Search Limitations**: Graceful handling of search restrictions
- **Source Unavailability**: Multiple backup data sources
- **Rate Limiting**: Intelligent request spacing and retry logic

### Agent Coordination
- **Agent Failures**: Individual agent failures don't stop the system
- **Data Aggregation**: Successful agents provide data even if others fail
- **Status Reporting**: Clear indication of which agents succeeded/failed
- **Fallback Data**: Realistic statistics when live data unavailable

### System Resilience
- **75-100% Success Rate**: Multiple sources ensure data availability
- **Real-time Status**: Users see exactly which sources are working
- **Graceful Degradation**: System works even with partial failures
- **AI Analysis**: Gemini provides insights regardless of data source status

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

- [ ] **Real-time Match Data**: Live match integration and updates
- [ ] **Advanced Statistical Modeling**: Machine learning predictions
- [ ] **Team Analysis**: Multi-player team performance analysis
- [ ] **Historical Match Analysis**: Deep dive into specific matches
- [ ] **Mobile App Interface**: Native mobile applications
- [ ] **API for Third-party Integration**: REST API for external use
- [ ] **Enhanced Fallback Data**: More sophisticated backup data generation
- [ ] **Agent Performance Optimization**: Improved success rates
- [ ] **Custom Data Sources**: User-configurable data source hierarchy
- [ ] **Advanced AI Features**: More sophisticated Gemini integration

---

**🏏 CricketIQ Multi-Agent System** - Powered by Google ADK, Gemini AI & Multiple Data Sources

### 🎯 System Performance
- **Success Rate**: 75-100% (3-4/4 data sources)
- **Analysis Time**: 10-15 seconds
- **Data Sources**: ESPN, Cricbuzz, Wikipedia, Google Search
- **AI Analysis**: Google Gemini 2.0 Flash
- **Fallback System**: Robust backup data mechanisms
- **Real-time Status**: Live agent monitoring and reporting
