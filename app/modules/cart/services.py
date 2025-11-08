from app.modules.auth.services import AuthenticationService
from app.modules.cart.repositories import CartItemRepository, CartRepository
from app.modules.dataset.services import DataSetService
from core.services.BaseService import BaseService


class CartService(BaseService):
    def __init__(self):
        self.cart_repository = CartRepository()
        self.cart_item_repository = CartItemRepository()
        self.dataset_service = DataSetService()
        self.auth_service = AuthenticationService()
        super().__init__(self.cart_repository)

    def add_to_cart(self, user_id: int, item_id: int):
        cart = self.cart_repository.get_cart_by_user_id(user_id)
        if not cart:
            return {"message": "Cart not found."}, 404
        existing_item = self.cart_item_repository.find_by_cart_and_model(cart.id, item_id)
        if existing_item:
            return {"message": "Item already in cart."}, 400
        self.cart_item_repository.add_item(cart.id, item_id)
        return {"message": "Item added to cart."}, 200

    def view_cart(self, user_id: int):
        cart_items = self.cart_repository.get_cart_items(user_id)
        return [{"cart_item_id": item.id, "feature_model_id": item.feature_model_id} for item in cart_items]

    def delete_from_cart(self, user_id: int, item_id: int = None):
        cart = self.cart_repository.get_cart_by_user_id(user_id)
        if not cart:
            return {"message": "Cart not found."}, 404
        if item_id is None:
            self.cart_repository.clear_cart(user_id)
            return {"message": "Cart cleared."}, 200
        else:
            removed = self.cart_item_repository.remove_item(cart.id, item_id)
            if not removed:
                return {"message": "Item not found in cart."}, 404
        return {"message": "Item removed from cart."}, 200

    def create_dataset(self, user_id: int, form):
        cart = self.cart_repository.get_cart_by_user_id(user_id)
        if not cart or not cart.items:
            return {"message": "Cart is empty."}, 400
        user = self.auth_service.get_authenticated_user()
        if not user or user.id != user_id:
            return {"message": "User not authenticated."}, 401
        form.feature_models = [item.feature_model for item in cart.items]
        dataset = self.dataset_service.create_from_form(form, user)
        self.cart_repository.clear_cart(user_id)
        return {
            "message": "DataSet created successfully.",
            "dataset_id": dataset.id,
            "models_included": [fm.id for fm in dataset.feature_models],
        }, 201
