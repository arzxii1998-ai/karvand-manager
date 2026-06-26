import json
import os

file_path = "data/karvands.json"

if os.path.exists(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
else:
    data = {"bootcamp": {"title": "AI Karvands", "year": "2026"}, "karvands": []}

karvands_list = data["karvands"]
if karvands_list:
    new_id = len(karvands_list) + 1
else:
    new_id = 1


print("==" * 10 + "Karvand Manager" + "==" * 10)

continuity = True
id = 0

while continuity:
    command = int(
        input("1. Add\n2. Show\n3. edit\n4. delete\n5. report\n6. exit\n------->> ")
    )

    # 1. Add section

    if command == 1:
        name = input("Esm Bede: ")
        mail = input("E-mail esh: ")
        city = input("Shahr: ")
        fieldd = input("tahsilat: ")
        degree = input("Sath: ")
        skills = input("Shirin Kari: ")

        # making Dictionary
        id += 1
        new_karvand = {
            "id": id,
            "full name": name,
            "city": city,
            "education": {
                "fieldd": fieldd,
                "degree": degree,
            },
            "skills": skills,
        }

        # Saving
        data["karvands"].append(new_karvand)

        with open(file_path, "w") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        print(f"{name} Zakhire Shod.\n")

    # Show Section
    elif command == 2:
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                data = json.load(file)
            karvands = data["karvands"]

            if not karvands:
                print("\n Hichi karvand vojud nadarad!")
            else:
                # How to Show
                print("List Karvand haa:\n")
                print("\n" + "=" * 50)
                for k in karvands:
                    print(f"\n ID: {k['id']}")
                    print(f"name: {k['full name']}")
                    print(f"City: {k['city']}")
                    print(
                        f"education: {k['education']['fieldd']} dar sathe {k['education']['degree']}"
                    )
                    print(f"skills: {k['skills']}")
                    print("\n" + "=" * 50 + "\n")
        else:
            print("file json karvand ha gom shode!")

    # Exit Section
    else:
        break
