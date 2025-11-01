from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# --- Safe arithmetic operations ---
def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b):
    if b == 0:
        raise ValueError('Division by zero')
    return a / b
def power(a, b): return a ** b
def mod(a, b):
    if b == 0:
        raise ValueError('Modulo by zero')
    return a % b

OPERATIONS = {
    'add': add, 'plus': add, 'sum': add,
    'subtract': sub, 'minus': sub, 'difference': sub,
    'multiply': mul, 'times': mul, 'product': mul,
    'divide': div, 'divided': div,
    'power': power, 'to_the_power': power,
    'mod': mod, 'modulo': mod, 'remainder': mod,
}

# --- Homepage route ---
@app.route('/')
def home():
    return render_template('index.html')  # HTML must be in 'templates' folder

# --- Compute API route ---
@app.route('/compute', methods=['POST'])
def compute():
    data = request.get_json() or {}
    op = data.get('operation')
    a = data.get('a')
    b = data.get('b')

    # Validate input
    if op is None or a is None or b is None:
        return jsonify({'error': 'operation, a and b are required'}), 400
    if op not in OPERATIONS:
        return jsonify({'error': f'unsupported operation: {op}'}), 400

    try:
        a = float(a)
        b = float(b)
    except:
        return jsonify({'error': 'operands must be numbers'}), 400

    # Compute result
    try:
        result = OPERATIONS[op](a, b)
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# --- Run the app ---
if __name__ == '__main__':
    app.run(debug=True)
