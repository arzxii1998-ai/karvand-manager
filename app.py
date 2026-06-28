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


print(
    "*" * 57
    + "\n"
    + "==" * 10
    + " Karvand Manager "
    + "==" * 10
    + "\n"
    + "*" * 57
    + "\n"
)

continuity = True

while continuity:
    command = int(
        input("1. Add\n2. Show\n3. edit\n4. delete\n5. report\n6. exit\n------->> ")
    )

    # 1. Add section

    if command == 1:
        nafar_badi_hast = str()
        avvalin = True
        while True:
            if avvalin:
                name = input("\nEsm Bede: ")
            else:
                name = nafar_badi_hast
            mail = input("E-mail esh: ")
            city = input("Shahr: ")
            fieldd = input("tahsilat: ")
            degree = input("maghta: ")

            # Skills input
            skills = {}
            print("Mahaarat (harvaght tamoom shod ye adad bezan):")
            while True:
                skill_name = input("  - Mahaarat: ")
                if not skill_name.isdigit():
                    skill_score = input("  - Mizane Maharat: ")
                    skills[skill_name] = int(skill_score)
                    print("  +++++++++")
                else:
                    break

            # making Dictionary
            new_karvand = {
                "id": new_id,
                "full name": name,
                "mail": mail,
                "city": city,
                "education": {
                    "field": fieldd,
                    "degree": degree,
                },
                "skills": skills,
            }

            # Saving
            data["karvands"].append(new_karvand)

            with open(file_path, "w") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)

            print(f"\n:::::::::::::: {name} Zakhire Shod. ::::::::::::::\n")

            new_id = +1
            avvalin = False
            nafar_badi_hast = input("Bazam Hast? (adad bezan agar nist): ")
            if nafar_badi_hast.isdigit():
                print("\n")
                break

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
                    print(f"\nID: {k['id']}")
                    print(f"name: {k['full name']}")
                    print(f"Email: {k['mail']}")
                    print(f"City: {k['city']}")
                    print(
                        f"education: {k['education']['field']}\nmaghta: {k['education']['degree']}"
                    )
                    print("skills:")
                    for skills, score in k["skills"].items():
                        print(f"   - {skills}: {score}")
                    print("\n" + "=" * 50 + "\n")
        else:
            print("file json karvand-haa sakhte nashode!\n")

    # Edit Section
    elif command == 3:
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                data = json.load(file)
            karvands = data["karvands"]
            print("Kio mikhay edit koni (ID-ish ro vared kon):\n")
            for k in karvands:
                print(f"  {k['id']}- {k['full name']}")
            to_edit = int(input("\n----> "))

            for k in karvands:
                if k["id"] == to_edit:
                    print("\n- Edit kon...: ")
                    k["full name"] = input("New name: ")
                    k["mail"] = input("New email: ")
                    k["city"] = input("New city: ")
                    k["education"]["field"] = input("New field: ")
                    k["education"]["degree"] = input("New degree: ")

                    skills = {}
                    print("New Mahaarat (harvaght tamoom shod ye adad bezan):")
                    while True:
                        skill_name = input("  - Mahaarat: ")
                        if not skill_name.isdigit():
                            skill_score = input("  - Mizane Maharat: ")
                            skills[skill_name] = int(skill_score)
                            print("  +++++++++")
                        else:
                            break

                    k["skills"] = skills

            with open(file_path, "w") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)

            print("\n:::::::::::::: Zakhire Shod. ::::::::::::::\n")

        else:
            print("file json karvand-haa sakhte nashode!")

    # Exit Section
    else:
        break
