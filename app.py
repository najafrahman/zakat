from flask import Flask, request, jsonify

app = Flask(__name__)

# Nisab thresholds
gold_nisab = 87.48  # grams of gold
silver_nisab = 612.36  # grams of silver
gold_price_per_gram = 60  # Example, replace with live data
silver_price_per_gram = 0.75  # Example, replace with live data

@app.route('/calculate-zakat', methods=['POST'])
def calculate_zakat():
    data = request.json
    wealth = data.get('wealth', 0)  # Wealth input from user
    asset_type = data.get('asset_type', 'gold')  # gold or silver
    
    # Calculate the Nisab in currency value
    if asset_type == 'gold':
        nisab_value = gold_nisab * gold_price_per_gram
    elif asset_type == 'silver':
        nisab_value = silver_nisab * silver_price_per_gram
    else:
        return jsonify({"error": "Invalid asset type. Use 'gold' or 'silver'."}), 400

    # Check if wealth exceeds Nisab
    if wealth < nisab_value:
        return jsonify({"eligible_for_zakat": False, "message": "Wealth is below Nisab threshold."}), 200

    # Calculate Zakat
    zakat = wealth * 0.025  # 2.5% of the wealth
    return jsonify({"eligible_for_zakat": True, "zakat_amount": zakat, "nisab_value": nisab_value}), 200

if __name__ == '__main__':
    app.run(debug=True)
