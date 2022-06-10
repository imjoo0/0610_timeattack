# product/models.py :

from django.db import models
from user import models as UserModel
from django.conf import settings


# Create your models here.
# <상품의 카테고리 이름>이 들어갈 수 있는 `Category` 라는 모델을 만들어보세요.
class Category(models.Model):
    class Meta:
        db_table = "categories"

    name = models.CharField(max_length=100)



# <상품 이름, 상품 카테고리, 이미지, 설명, 가격, 재고량>이 들어갈 수 있는 Product 이라는 모델을 만들어보세요.
class Product(models.Model):
    class Meta:
        db_table = "products"

    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='product/%Y/%m%d',blank=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,null=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    stok = models.IntegerField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# 유저가 주문한 상품의 개수를 저장하는 ProductOrder 하는 모델을 만들어 보세요
class ProductOrder(models.Model):
    class Meta:
        db_table = "product_orders"
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    product_count = models.IntegerField()

# 주문한 상태(주문 완료, 결제 완료, 취소, 배송출발, 배송완료) 을 저장할 수 있는
# OrderStatus라는 모델을 만들어보세요.
class OrderStatus(models.Model):
    class Meta:
        db_table = "order_status"
    status_name = models.CharField(max_length=100)

# 유저의 주문(배송주소, 주문시간, 전체 상품 가격, 할인율, 최종가격, 유효여부(boolean) )을 저장할 수 있는
# UserOrder라는 모델을 만들어보세요.
class UserOrder(models.Model):
    class Meta:
        db_table = "user_orders"
    user = models.ForeignKey(UserModel.User,on_delete=models.SET_NULL,null=True)
    product_order = models.ForeignKey(ProductOrder,on_delete=models.SET_NULL,null=True)
    order_status = models.ForeignKey(OrderStatus,on_delete=models.SET_NULL,null=True)
    delivery_address = models.CharField(max_length=100)
    order_time = models.DateTimeField()
    total_price = models.DecimalField(max_digits=20,decimal_places=2)
    discount = models.DecimalField(max_digits=20,decimal_places=2)
    final_price = models.DecimalField(max_digits=20,decimal_places=2)
    active = models.BooleanField()


