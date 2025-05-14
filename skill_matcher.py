import networkx as nx
import pandas as pd
from typing import Dict, List, Set, Tuple
import matplotlib.pyplot as plt

class SkillMatcher:
    def __init__(self):
        """Initialize the skill matching system with an empty graph."""
        self.graph = nx.Graph()
        self.skill_similarity = {}  # Dictionary to store skill similarity scores
        
    def add_candidate(self, candidate_id: str, skills: Dict[str, float]) -> None:
        """
        Add a candidate to the graph with their skills and experience.
        
        Args:
            candidate_id: Unique identifier for the candidate
            skills: Dictionary mapping skill names to years of experience
        """
        # Add candidate node
        self.graph.add_node(candidate_id, type='candidate')
        
        # Add skill nodes and edges
        for skill, years in skills.items():
            if skill not in self.graph:
                self.graph.add_node(skill, type='skill')
            # Add edge with weight inversely proportional to years of experience
            # (shorter edge = more experience)
            self.graph.add_edge(candidate_id, skill, weight=1/years, years=years)
    
    def set_skill_similarity(self, skill1: str, skill2: str, similarity: float) -> None:
        """
        Set similarity score between two skills.
        
        Args:
            skill1: First skill name
            skill2: Second skill name
            similarity: Similarity score between 0 and 1
        """
        if skill1 not in self.skill_similarity:
            self.skill_similarity[skill1] = {}
        if skill2 not in self.skill_similarity:
            self.skill_similarity[skill2] = {}
            
        self.skill_similarity[skill1][skill2] = similarity
        self.skill_similarity[skill2][skill1] = similarity
    
    def find_matching_candidates(self, 
                               required_skills: Dict[str, float],
                               min_similarity: float = 0.7) -> List[Tuple[str, float]]:
        """
        Find candidates matching the required skills, considering skill substitution.
        
        Args:
            required_skills: Dictionary mapping required skills to minimum years of experience
            min_similarity: Minimum similarity score for skill substitution (0-1)
            
        Returns:
            List of tuples containing (candidate_id, match_score)
        """
        candidates = []
        
        for candidate in [n for n, d in self.graph.nodes(data=True) if d['type'] == 'candidate']:
            match_score = 0
            total_required = len(required_skills)
            
            for req_skill, req_years in required_skills.items():
                # Check direct skill match
                if self.graph.has_edge(candidate, req_skill):
                    years = self.graph[candidate][req_skill]['years']
                    if years >= req_years:
                        match_score += 1
                    else:
                        match_score += years / req_years
                else:
                    # Check for similar skills
                    best_similar_score = 0
                    for skill in self.graph.neighbors(candidate):
                        if skill in self.skill_similarity and req_skill in self.skill_similarity[skill]:
                            similarity = self.skill_similarity[skill][req_skill]
                            if similarity >= min_similarity:
                                years = self.graph[candidate][skill]['years']
                                score = similarity * (years / req_years)
                                best_similar_score = max(best_similar_score, score)
                    match_score += best_similar_score
            
            if match_score > 0:
                candidates.append((candidate, match_score / total_required))
        
        return sorted(candidates, key=lambda x: x[1], reverse=True)
    
    def visualize_graph(self, filename: str = 'skill_graph.png') -> None:
        """
        Create a visualization of the skill matching graph.
        
        Args:
            filename: Name of the output file
        """
        plt.figure(figsize=(12, 8))
        pos = nx.spring_layout(self.graph)
        
        # Draw candidate nodes
        candidate_nodes = [n for n, d in self.graph.nodes(data=True) if d['type'] == 'candidate']
        nx.draw_networkx_nodes(self.graph, pos, nodelist=candidate_nodes, 
                             node_color='lightblue', node_size=500, label='Candidates')
        
        # Draw skill nodes
        skill_nodes = [n for n, d in self.graph.nodes(data=True) if d['type'] == 'skill']
        nx.draw_networkx_nodes(self.graph, pos, nodelist=skill_nodes,
                             node_color='lightgreen', node_size=300, label='Skills')
        
        # Draw edges with weights
        edge_weights = [self.graph[u][v]['weight'] * 2 for u, v in self.graph.edges()]
        nx.draw_networkx_edges(self.graph, pos, width=edge_weights)
        
        # Add labels
        nx.draw_networkx_labels(self.graph, pos)
        
        plt.legend()
        plt.title('Skill Matching Graph')
        plt.axis('off')
        plt.savefig(filename)
        plt.close() 