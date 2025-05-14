# Skill Matching System

A graph-based skill matching system for recruitment that uses NetworkX to analyze and visualize skill relationships.

## About NetworkX

NetworkX is a Python library used for the creation, manipulation, and study of complex networks (graphs) of nodes and edges. In this project, we use NetworkX for:



## Project Features

1. **Skill Management**
   - Add candidate skills with experience levels
   - Define skill similarities
   - Set minimum experience requirements

2. **Matching Algorithm**
   - Graph-based skill matching
   - Weighted similarity calculations
   - Experience level consideration

3. **Visualization**
   - Interactive skill graph
   - Match percentage display
   - Candidate ranking

## Requirements

- Python 3.x
- NetworkX
- Flask
- Matplotlib
- Bootstrap 5

## Installation

1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the application:
```bash
python app.py
```

2. Open your browser and navigate to:
```
http://localhost:5000
```

3. Use the interface to:
   - Add candidates and their skills
   - Set skill similarities
   - Find matches for job requirements

## How It Works

1. **Skill Graph Creation**
   - Each skill is a node in the graph
   - Similarities between skills are edges
   - Edge weights represent similarity scores

2. **Matching Process**
   - Job requirements are matched against candidate skills
   - NetworkX algorithms calculate match scores
   - Results are ranked by match percentage

3. **Visualization**
   - Skills and their relationships are displayed as a graph
   - Match results show candidate rankings
   - Interactive graph exploration

## Contributing

Feel free to submit issues and enhancement requests! 