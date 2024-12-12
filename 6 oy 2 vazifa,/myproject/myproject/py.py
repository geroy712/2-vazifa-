import os

# App nomlari ro'yxati
app_names = [
    "app1", "app2", "app3", "app4", "app5",
    "app6", "app7", "app8", "app9", "app10"
]

# Django settings.py faylining joylashuvi
settings_path = os.path.join("myproject", "settings.py")

# App-larni yaratish
for app in app_names:
    os.system(f"python manage.py startapp {app}")
    print(f"{app} yaratildi!")

# settings.py fayliga app-larni qo'shish
with open(settings_path, "r") as file:
    settings = file.readlines()

# INSTALLED_APPS bo'limiga yangi app-larni qo'shish
for index, line in enumerate(settings):
    if "INSTALLED_APPS" in line:
        for app in app_names:
            settings.insert(index + 2, f"    '{app}',\n")
        break

# Yangilangan settings.py ni saqlash
with open(settings_path, "w") as file:
    file.writelines(settings)

print("Barcha app-lar INSTALLED_APPS ga qo'shildi!")
