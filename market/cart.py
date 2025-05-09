from django.core.exceptions import ObjectDoesNotExist


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart
        self.cleanup()

    def add(self, product_id, quantity=1):
        product_id = str(product_id)
        if product_id in self.cart:
            self.cart[product_id]['quantity'] += quantity
        else:
            self.cart[product_id] = {'quantity': quantity}
        self.save()

    def remove(self, product_id):
        product_id = str(product_id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def clear(self):
        self.session['cart'] = {}
        self.save()

    def save(self):
        self.session.modified = True

    def cleanup(self):
        product_ids = list(self.cart.keys())
        for product_id in product_ids:
            try:
                Product.objects.get(id=product_id) # type: ignore
            except ObjectDoesNotExist:
                del self.cart[product_id]
        self.save()

    def __iter__(self):
        return iter(self.cart.items())

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
