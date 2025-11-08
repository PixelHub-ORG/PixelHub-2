from flask import jsonify, render_template, request
from flask_login import current_user, login_required

from app.modules.cart import cart_bp
from app.modules.cart.forms import CartCreateDatasetForm
from app.modules.cart.services import CartService
from app.modules.featuremodel.services import FeatureModelService

cart_service = CartService()
fm_service = FeatureModelService()


@cart_bp.route("/user/cart/view_page", methods=["GET"])
@login_required
def view_cart_page():
    cart_items = cart_service.view_cart(current_user.id)
    models = []

    for item in cart_items:
        feature_model = fm_service.get_by_id(item["feature_model_id"])
        if feature_model:
            fm_meta = feature_model.fm_meta_data
            models.append(
                {
                    "id": feature_model.id,
                    "name": fm_meta.title if fm_meta else "No title",
                    "description": fm_meta.description if fm_meta else "",
                }
            )

    return render_template("cart/view_cart.html", models=models)


@cart_bp.route("/user/cart/count", methods=["GET"])
@login_required
def cart_count():
    cart_items = cart_service.view_cart(current_user.id)
    return jsonify({"count": len(cart_items)})


@cart_bp.route("/featuremodel/cart/add", methods=["POST"])
@login_required
def add_to_cart():
    data = request.get_json()
    item_id = data.get("item_id")
    if not item_id:
        return jsonify({"message": "No item_id provided"}), 400

    result, status_code = cart_service.add_to_cart(current_user.id, item_id)
    return jsonify(result), status_code


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
