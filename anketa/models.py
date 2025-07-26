from django.db import models
from .constants import (
    BMI_CHOICES, BMI_POINTS,
    EDUCATION_CHOICES, EDUCATION_POINTS,
    INCOME_CHOICES, INCOME_POINTS,
    KNOWLEDGE_CHOICES, KNOWLEDGE_POINTS,
    MOOD_CHOICES, MOOD_POINTS,
    BIRTH_CHOICES,
    VITAMIN_CHOICES, VITAMIN_POINTS,
    CONTACT_CHOICES, CONTACT_POINTS,
    BREASTFEEDING_CHOICES, BREASTFEEDING_POINTS,
    FOOD_CHOICES, FOOD_POINTS, AGE_CHOICES, AGE_POINTS
)

class Mother(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    fathers_name = models.CharField(max_length=100)

    age_category = models.CharField(max_length=20, choices=AGE_CHOICES)

    bmi_category = models.CharField(max_length=20, choices=BMI_CHOICES)
    education = models.CharField(max_length=20, choices=EDUCATION_CHOICES)
    income_level = models.CharField(max_length=20, choices=INCOME_CHOICES)
    has_chronic_illness = models.BooleanField()
    harmful_habits = models.BooleanField()
    knowledge_level = models.CharField(max_length=20, choices=KNOWLEDGE_CHOICES)
    mood_last_2_weeks = models.CharField(max_length=20, choices=MOOD_CHOICES)

    def __str__(self):
       return f"{self.last_name} {self.first_name} {self.fathers_name}"

class Child(models.Model):
    mother = models.ForeignKey(Mother, on_delete=models.CASCADE, related_name="children")
    birth_date = models.DateField()
    birth_weight = models.FloatField()

    def __str__(self):
        return f"{self.mother.last_name} {self.mother.first_name} {self.mother.fathers_name}- {self.birth_date}"

class AnketaResponse(models.Model):
    mother = models.ForeignKey(Mother, on_delete=models.CASCADE, related_name="anketa_responses")
    child = models.OneToOneField(Child, on_delete=models.CASCADE)

    # --- anketadagi maydonlar ---
    birth_type = models.CharField(max_length=20, choices=BIRTH_CHOICES)
    took_vitamins = models.CharField(max_length=20, choices=VITAMIN_CHOICES)
    pregnancy_complications = models.BooleanField()
    delivery_complications = models.BooleanField()
    contact_after_birth = models.CharField(max_length=20, choices=CONTACT_CHOICES)
    breastfeeding = models.CharField(max_length=20, choices=BREASTFEEDING_CHOICES)
    breastfeeding_difficulties = models.BooleanField()
    complementary_feeding_time = models.CharField(max_length=20, choices=FOOD_CHOICES)

    score = models.IntegerField(blank=True, null=True)
    risk_category = models.CharField(max_length=30, blank=True, null=True)

    def calculate_score(self):
        score = 0

        # 1. Onaning yoshi
        score += AGE_POINTS.get(self.mother.age_category, 0)

        # 2. BMI
        score += BMI_POINTS.get(self.mother.bmi_category, 0)

        # 3. Ta’lim
        score += EDUCATION_POINTS.get(self.mother.education, 0)

        # 4. Daromad
        score += INCOME_POINTS.get(self.mother.income_level, 0)

        # 5. Ekstragenital kasalliklar
        score += 2 if self.mother.has_chronic_illness else 0

        # 6. Vitamin qabul qilish
        score += VITAMIN_POINTS.get(self.took_vitamins, 0)

        # 7. Homiladorlikdagi asoratlar
        score += 0 if self.pregnancy_complications else 2

        # 8. Tug‘ruqdagi asoratlar
        score += 2 if self.delivery_complications else 0

        # 9. Bolaning tug‘ilgan vazni
        score += 2 if self.child.birth_weight < 2500 else 0

        # 10. Ona va bola birga bo‘lishi
        score += CONTACT_POINTS.get(self.contact_after_birth, 0)

        # 11. Emizish holati
        score += BREASTFEEDING_POINTS.get(self.breastfeeding, 0)

        # 12. Emizishdagi qiyinchiliklar
        score += 2 if self.breastfeeding_difficulties else 0

        # 13. Qo‘shimcha ovqat berish
        score += FOOD_POINTS.get(self.complementary_feeding_time, 0)

        # 14. Parvarish bilim darajasi
        score += KNOWLEDGE_POINTS.get(self.mother.knowledge_level, 0)

        # 15. Kayfiyat
        score += MOOD_POINTS.get(self.mother.mood_last_2_weeks, 0)

        # 16. Zararli odatlar
        score += 2 if self.mother.harmful_habits else 0

        return score


    def get_risk_category(self):
        score = self.score or self.calculate_score()

        if score <= 5:
            return "Past xavf"
        elif score <= 10:
            return "O‘rtacha xavf"
        elif score <= 20:
            return "Yuqori xavf"
        else:
            return "Juda yuqori xavf"

    def save(self, *args, **kwargs):
        self.score = self.calculate_score()
        self.risk_category = self.get_risk_category()
        super().save(*args, **kwargs)

