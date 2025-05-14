# Graph-Based Skill Matching System

A sophisticated graph-based system for matching candidates to job roles based on skills and experience. This system uses graph theory to model relationships between candidates, skills, and experience levels, enabling intelligent candidate matching with support for skill substitution and experience proximity.

## Features

- Graph-based modeling of candidate skills and experience
- Support for skill substitution and transferable skills
- Experience-based weighting of skill matches
- Visual representation of the skill matching graph
- Configurable similarity thresholds for skill matching

## Installation

1. Clone this repository
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

```python
from skill_matcher import SkillMatcher

# Initialize the skill matcher
matcher = SkillMatcher()

# Add candidates with their skills and experience
matcher.add_candidate("candidate1", {
    "Python": 8,
    "Machine Learning": 5,
    "Data Analysis": 6
})

# Set skill similarities
matcher.set_skill_similarity("Python", "R", 0.8)

# Define required skills for a role
required_skills = {
    "Python": 5,
    "Machine Learning": 3
}

# Find matching candidates
matches = matcher.find_matching_candidates(required_skills)

# Visualize the graph
matcher.visualize_graph("skill_graph.png")
```

## How It Works

1. **Graph Construction**
   - Candidates and skills are represented as nodes
   - Edges connect candidates to their skills
   - Edge weights are inversely proportional to years of experience

2. **Skill Matching**
   - Direct matches are found for required skills
   - Similar skills are considered based on similarity scores
   - Experience levels are weighted in the matching process

3. **Visualization**
   - The system generates a visual representation of the skill graph
   - Candidates and skills are color-coded
   - Edge thickness represents experience level

## Testing

Run the test suite:
```bash
pytest test_skill_matcher.py
```

## Requirements

- Python 3.7+
- NetworkX
- Pandas
- NumPy
- Matplotlib
- Pytest (for testing)

## License

MIT License 