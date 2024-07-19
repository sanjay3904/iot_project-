from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)
DATABASE = 'temperature_data.db'

def get_last_temperature():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT timestamp, temperature FROM temperature_data ORDER BY timestamp DESC LIMIT 1")
    row = cursor.fetchone()
    conn.close()
    if row:
        return {'timestamp': row[0], 'temperature': row[1]}
    return {'timestamp': None, 'temperature': None}

@app.route('/temperature', methods=['GET'])
def temperature():
    data = get_last_temperature()
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

