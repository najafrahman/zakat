from flask import request, jsonify
from app import app
from app.utils import calculate_zakat, nisab_values

@app.route('/calculate_zakat', methods=['POST'])
def calculate_zakat_api():
    data = request.get_json()
    wealth = data.get('wealth')
    wealth_type = data.get('wealth_type')

    if wealth_type not in ['gold', 'silver']:
        return jsonify({'error': 'Invalid wealth type. Use gold or silver.'}), 400
    
    nisab_value = nisab_values.get(wealth_type)
    if wealth < nisab_value:
        return jsonify({'message': 'You are not eligible to pay Zakat.'}), 200
    
    zakat = calculate_zakat(wealth)
    return jsonify({'zakat': zakat, 'nisab_value': nisab_value})


