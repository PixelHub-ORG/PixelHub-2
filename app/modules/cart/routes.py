from flask import jsonify, render_template, request
from flask_login import current_user, login_required

from app.modules.cart import cart_bp
from app.modules.cart.forms import CartCreateDatasetForm
from app.modules.cart.services import CartService

cart_service = CartService()


@cart_bp.route("/user/cart/view", methods=["GET"])
@login_required
def view_cart():
    return jsonify(cart_service.view_cart(current_user.id))


@cart_bp.route("/featuremodel/cart/add", methods=["POST"])
@login_required
def add_to_cart():
    data = request.get_json()
    item_id = data.get("item_id")
    if not item_id:
        return jsonify({"message": "No item_id provided"}), 400

    return jsonify(cart_service.add_to_cart(current_user.id, item_id))


@cart_bp.route("/user/cart/delete", methods=["POST"])
@login_required
def delete_from_cart():
    data = request.get_json()
    item_id = data.get("item_id")
    return jsonify(cart_service.delete_from_cart(current_user.id, item_id))


@cart_bp.route("/user/cart/create", methods=["GET", "POST"])
@login_required
def create_dataset():
    form = CartCreateDatasetForm()

    if request.method == "POST":
        if not form.validate_on_submit():
            return jsonify({"message": form.errors}), 400

        result, status_code = cart_service.create_dataset(current_user.id, form)
        return jsonify(result), status_code

    cart_items = cart_service.view_cart(current_user.id)
    return render_template("cart/create_dataset.html", form=form, cart_items=cart_items)
