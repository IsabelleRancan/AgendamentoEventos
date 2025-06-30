from flask import Flask, request, jsonify
from models import init_db
import repository
import message_sender

app = Flask(__name__)

init_db()

@app.route('/events', methods=['GET'])
def get_events():
    events = repository.get_all_events()
    return jsonify(events), 200

@app.route('/events/upcoming', methods=['GET'])
def get_upcoming_events():
    events = repository.get_upcoming_events()
    return jsonify(events), 200

@app.route('/events', methods=['POST'])
def create_event():
    data = request.get_json()

    required_fields = ['title', 'description', 'date', 'max_participants']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing fields'}), 400

    try:
        repository.create_event(data)
        return jsonify({'message': 'Evento criado com sucesso'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/events/<int:event_id>/subscribe', methods=['POST'])
def subscribe(event_id):
    data = request.get_json()
    email = data.get('email')

    if not email:
        return jsonify({'error': 'Email é obrigatório'}), 400

    if repository.is_event_full(event_id):
        return jsonify({'error': 'Evento lotado'}), 400

    try:
        repository.register_participant(event_id, email)
        message_sender.send_email_message(event_id, email)
        return jsonify({'message': 'Inscrição realizada com sucesso'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
