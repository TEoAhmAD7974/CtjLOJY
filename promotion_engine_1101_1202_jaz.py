# 代码生成时间: 2025-11-01 12:02:37
from bottle import Bottle, run, request, response


# Promotion Engine Application
app = Bottle()


# Define sample promotions
# Can be expanded to load from a database or external service
PROMOTIONS = {
    'SUMMER_SALE': {'discount': 20, 'start_date': '2023-06-01', 'end_date': '2023-08-31'},
    'BLACK_FRIDAY': {'discount': 30, 'start_date': '2023-11-24', 'end_date': '2023-11-25'}
}
# TODO: 优化性能


# Helper function to check if a promotion is active
def is_promotion_active(promotion_id):
    promotion = PROMOTIONS.get(promotion_id)
# TODO: 优化性能
    if not promotion:
        return False
    today = datetime.datetime.now().date()
    start_date = datetime.datetime.strptime(promotion['start_date'], '%Y-%m-%d').date()
    end_date = datetime.datetime.strptime(promotion['end_date'], '%Y-%m-%d').date()
    return start_date <= today <= end_date


# Route to apply a promotion
@app.route('/apply_promotion', method='POST')
def apply_promotion():
# FIXME: 处理边界情况
    try:
        promotion_id = request.json.get('promotion_id')
        if not promotion_id:
            response.status = 400
            return {'error': 'Promotion ID is required'}
        if not is_promotion_active(promotion_id):
            response.status = 400
            return {'error': 'Promotion is not active'}
        original_price = request.json.get('original_price')
        if not original_price or original_price <= 0:
            response.status = 400
            return {'error': 'Invalid original price'}
        discount = PROMOTIONS[promotion_id]['discount']
        discounted_price = original_price * (1 - discount / 100)
        return {'discounted_price': discounted_price}
    except Exception as e:
        response.status = 500
        return {'error': str(e)}


# Route to list active promotions
@app.route('/active_promotions', method='GET')
def list_active_promotions():
    today = datetime.datetime.now().date()
    active_promotions = {
        promo_id: promo for promo_id, promo in PROMOTIONS.items()
        if is_promotion_active(promo_id)
    }
# FIXME: 处理边界情况
    return active_promotions


# Run the application
if __name__ == '__main__':
    run(app, host='localhost', port=8080)
