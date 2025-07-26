AGE_CHOICES = [
    ('under_18_or_over_35', '<18 yoki >35 yosh'),
    ('between_18_and_35', '18–35 yosh'),
]

AGE_POINTS = {
    'under_18_or_over_35': 2,
    'between_18_and_35': 0,
}


# BMI (Tana vazn indeksi)
BMI_CHOICES = [
    ('ozgin', '<18.5 (Ozg‘inlik)'),
    ('normal', '18.5–24.9 (Normal)'),
    ('semiz', '≥25 (Ortiqcha vazn)'),
]

BMI_POINTS = {
    'ozgin': 2,
    'semiz': 1,
    'normal': 0,
}

# Ta’lim darajasi
EDUCATION_CHOICES = [
    ('oliy', 'Oliy'),
    ('orta_maxsus', 'O‘rta maxsus'),
    ('orta', 'O‘rta'),
]

EDUCATION_POINTS = {
    'oliy': 2,
    'orta_maxsus': 1,
    'orta': 0,
}

# Daromad darajasi
INCOME_CHOICES = [
    ('yuqori', 'Yuqori daromad'),
    ('ortacha', 'O‘rtacha daromad'),
    ('past', 'Past daromad (eng kam ish haqi)'),
]

INCOME_POINTS = {
    'yuqori': 0,
    'ortacha': 1,
    'past': 2,
}

# Parvarish bo‘yicha bilim darajasi
KNOWLEDGE_CHOICES = [
    ('yoq', 'Umuman yo‘q'),
    ('qisman', 'Qisman biladi'),
    ('bor', 'Biladi (gigiena, ovqatlantirish, g‘amxo‘rlik va h.k.)'),
]

KNOWLEDGE_POINTS = {
    'yoq': 2,
    'qisman': 1,
    'bor': 0,
}

# Onaning kayfiyati (oxirgi 2 hafta)
MOOD_CHOICES = [
    ('doimiy_tushkun', 'Doimo tushkun'),
    ('baʼzan_tushkun', 'Ba’zan tushkun'),
    ('yoq', 'Tushkunlik yo‘q'),
]

MOOD_POINTS = {
    'doimiy_tushkun': 2,
    'baʼzan_tushkun': 1,
    'yoq': 0,
}

# Tug‘ruq turi
BIRTH_CHOICES = [
    ('tabiiy', 'Tabiiy tug‘ruq'),
    ('kesarcha', 'Kesarcha kesish'),
]

# Homiladorlikda vitaminlar qabul qilish
VITAMIN_CHOICES = [
    ('olmagan', 'Umuman olmagan'),
    ('qisman', 'Qisman olgan (faqat 3 oy)'),
    ('muntazam', 'Muntazam olgan (9 oy)'),
]

VITAMIN_POINTS = {
    'olmagan': 2,
    'qisman': 1,
    'muntazam': 0,
}

# Bola bilan birga bo‘lish holati
CONTACT_CHOICES = [
    ('darhol', 'Tug‘ruqdan so‘ng darhol birga bo‘lgan'),
    ('24_soatdan_keyin', '24 soatdan keyin birga bo‘lgan'),
]

CONTACT_POINTS = {
    'darhol': 2,
    '24_soatdan_keyin': 0,
}

# Emizish holati
BREASTFEEDING_CHOICES = [
    ('umuman_emizmagan', 'Umuman emizmagan'),
    ('aralash', 'Aralash'),
    ('faqat_ona_suti', 'Faqat ona suti'),
]

BREASTFEEDING_POINTS = {
    'umuman_emizmagan': 2,
    'aralash': 1,
    'faqat_ona_suti': 0,
}

# Qo‘shimcha ovqat berish vaqti
FOOD_CHOICES = [
    ('6_oydan_keyin', '6 oydan keyin'),
    ('noto‘g‘ri_vaqt', '<6 yoki 6-oyda'),
]

FOOD_POINTS = {
    '6_oydan_keyin': 2,
    'noto‘g‘ri_vaqt': 0,
}
