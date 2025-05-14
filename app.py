from flask import Flask, render_template, request, jsonify
from skill_matcher import SkillMatcher
import json

app = Flask(__name__)
matcher = SkillMatcher()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add_candidate', methods=['POST'])
def add_candidate():
    try:
        data = request.get_json()
        candidate_id = data.get('candidate_id')
        skills = data.get('skills')
        
        if not candidate_id or not skills:
            return jsonify({'error': 'Missing candidate_id or skills'}), 400
            
        matcher.add_candidate(candidate_id, skills)
        return jsonify({'message': f'Candidate {candidate_id} added successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/delete_candidate', methods=['POST'])
def delete_candidate():
    try:
        data = request.get_json()
        candidate_id = data.get('candidate_id')
        
        if not candidate_id:
            return jsonify({'error': 'Missing candidate_id'}), 400
            
        # Remove the candidate from the graph
        if candidate_id in matcher.graph:
            matcher.graph.remove_node(candidate_id)
            return jsonify({'message': f'Candidate {candidate_id} deleted successfully'})
        else:
            return jsonify({'error': f'Candidate {candidate_id} not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/set_similarity', methods=['POST'])
def set_similarity():
    try:
        data = request.get_json()
        skill1 = data.get('skill1')
        skill2 = data.get('skill2')
        similarity = data.get('similarity')
        
        if not all([skill1, skill2, similarity]):
            return jsonify({'error': 'Missing skill1, skill2, or similarity'}), 400
            
        matcher.set_skill_similarity(skill1, skill2, float(similarity))
        return jsonify({'message': f'Similarity set between {skill1} and {skill2}'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/find_matches', methods=['POST'])
def find_matches():
    try:
        data = request.get_json()
        required_skills = data.get('required_skills')
        min_similarity = data.get('min_similarity', 0.7)
        
        if not required_skills:
            return jsonify({'error': 'Missing required_skills'}), 400
            
        matches = matcher.find_matching_candidates(required_skills, float(min_similarity))
        
        # Generate graph visualization
        matcher.visualize_graph('static/skill_graph.png')
        
        return jsonify({
            'matches': matches,
            'graph_url': '/static/skill_graph.png'
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True) 