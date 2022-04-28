# 1 грам мазнини = 9 калории
# 1 грам протеини = 4 калории
# 1 грам въглехидрати = 4 калории

fat_percentage = int(input())
proteins_percentage = int(input())
carbs_percentage = int(input())
calories_count = int(input())
water_percentage = int(input())


grams_fat = (calories_count * fat_percentage / 100) / 9
grams_protein = (calories_count * proteins_percentage / 100) / 4
grams_carbs = (calories_count * carbs_percentage / 100) / 4

food_weight = grams_fat + grams_protein + grams_carbs
calories_pre_gram = calories_count / food_weight

pure_calories = calories_pre_gram - (calories_pre_gram * water_percentage / 100)

print(f"{pure_calories:.4f}")