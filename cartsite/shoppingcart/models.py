from django.db import models

class food_type(models.Model):
# ie american, mexican, etc
    foodType = models.CharField(max_length=50)


class food_item(models.Model):
# actual food item from menu
    foodCost = models.DecimalField(max_digits=5, decimal_places=2)
    foodName = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    popular = models.BooleanField()
    mealType = models.ForeignKey(meal_type, on_delete=models.CASCADE)

class meal_type(models.Model):
# ie soups & salads, entree, etc
    mType = models.CharField(max_length=50)

class menu(models.Model):
# populated by meal_type the food_item to corresponding meal_type
    mealType = models.ForeignKey(meal_type, on_delete=models.CASCADE)
    foodItem = models.OneToOneField(food_item, on_delete=models.CASCADE)


class rating(models.Model):
#rating data for restaurant
    RATING_SCORE = (
        ('1', '*'),
        ('2', '**'),
        ('3', '***'),
	('4', '****'),
	('5', '*****'),
    )
    comment = models.CharField(max_length=100)
	#quick summary comment
    rating_score = models.CharField(max_length=1, choices=RATING_SCORE)
    thoughts = models.CharField(max_length=400)
	#more extensive thoughts/comments

class restaurant(models.Model):
#full listing of restaurant info
    foodType = models.ManyToManyField(food_type, on_delete=models.CASCADE)
    menu = models.OneToOneField(menu, on_delete=models.CASCADE)
    deliveryTime = models.DurationField()
    COST_SCORE = (
        ('1', '$'),
        ('2', '$$'),
        ('3', '$$$'),
	('4', '$$$$'),
	('5', '$$$$$'),
    )
    cost_score = models.CharField(max_length=1, choices=COST_SCORE)
    minPurchase = models.DecimalField(max_digits=5, decimal_places=2)
    deliveryCost = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.CharField(max_length=100)
    rating = models.ForeignKey(food_type, on_delete=models.CASCADE)
    logo = models.ImageField(upload_to=None,height_field=100,width_field=100, max_length=100)
    address = models.CharField(max_length=150)
    phoneNum = models.CharField(max_length=30)
    restID = models.IntegerField()
	#restID is used for url mapping
