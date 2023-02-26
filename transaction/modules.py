from product.models import Product
from rest_framework.response import Response

def calculateTotalPrice(items):
    list_price = []
    
    for item in items:
        try:
            list_product = Product.objects.values_list('price', flat=True).filter(id=item["product_id"])
            if (len(list_product) >= 1):
                calculate_items = list_product[0] * item["quantity"]
                list_price.append(calculate_items)
            else:
                list_price = []
        except Product.DoesNotExist:
            return Response(status=404)
        
    return sum(list_price)
