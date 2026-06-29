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
    try:
        command = int(
            input(
                "1. Add\n2. Show\n3. edit\n4. delete\n5. report\n6.Search with ID\n7.search with Skill\n-. Har adade dige= exit\n------->> "
            )
        )
    except ValueError:
        print("\nDadash?!... Khoobi?!\n")
        continue

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
                    while True:
                        try:
                            skill_score = int(input("  - Mizane Maharat: "))
                        except ValueError:
                            print("Mese Adam adad vared kon nadan!\n")
                            continue
                        if skill_score in range(0, 101):
                            break
                        print(
                            "\nAdam bash va score skill ro adad 0 ta 100 bezan azizam."
                        )
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

            print(f"\n:::::::::::::: [{name}] Zakhire Shod. ::::::::::::::\n")

            new_id += 1
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
                print(
                    ":::::::::::::::::" + " List Karvand haa: " + ":::::::::::::::::\n"
                )
                for k in karvands:
                    print(f"ID: {k['id']}")
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

            ids_list = []
            for k in karvands:
                print(f"  {k['id']}- {k['full name']}")
                ids_list.append(k["id"])

            # inputting the user id to edit without out of range user input
            while True:
                to_edit = int(input("\n----> "))
                if to_edit in ids_list:
                    break
                print("Adam bash va ID dorost vared kon azizam!")

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
            print("file json karvand-haa sakhte nashode!\n")

    # 4. ِDelete Section
    elif command == 4:
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                data = json.load(file)
            karvands = data["karvands"]
            print("Kio mikhay delete koni (ID-ish ro vared kon):\n")

            ids_list = []
            for k in karvands:
                print(f"  {k['id']}- {k['full name']}")
                ids_list.append(k["id"])

            # inputting the user id to delete without out of range user input
            while True:
                to_del = int(input("\n----> "))
                if to_del in ids_list:
                    break
                print("Adam bash va ID dorost vared kon azizam!")

            for k in karvands:
                if k["id"] == to_del:
                    karvands.remove(k)

            for k in karvands:
                if k["id"] >= to_del:
                    k["id"] -= 1

            with open(file_path, "w") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)

            print("\n:::::::::::::: Delete Shod. ::::::::::::::\n")

            with open(file_path, "r") as file:
                data = json.load(file)
            karvands = data["karvands"]
            for k in karvands:
                print(f"  {k['id']}- {k['full name']}")
            print("")

        else:
            print("file json karvand-haa sakhte nashode!\n")

    # 5. Report Section
    elif command == 5:
        if os.path.exists(file_path):
            print("::::::::::: The Report :::::::::::\n")

            with open(file_path, "r") as file:
                data = json.load(file)
            karvands = data["karvands"]
            karvands_num = len(karvands)
            skills_num = 0
            total_scores = 0
            total_scores_ave = 0
            per_ave = {}
            all_cities = {}
            all_skills = {}
            unique_skills = {}

            for k in karvands:
                skills_num += len(k["skills"])

                # Averages and skill scores
                per_tot_score = 0
                for skill, score in k["skills"].items():
                    total_scores += int(score)

                    per_tot_score += int(score)
                if len(k["skills"]) > 0:
                    per_karvand_skills_score_ave = per_tot_score / len(k["skills"])
                else:
                    per_karvand_skills_score_ave = 0
                per_ave[k["full name"]] = per_karvand_skills_score_ave

                # Counting Cities
                if k["city"] not in all_cities:
                    all_cities[k["city"]] = 1
                else:
                    all_cities[k["city"]] += 1

                # Counting Unique Skills
                for skill, score in k["skills"].items():
                    if skill not in all_skills:
                        all_skills[skill] = 1
                    else:
                        all_skills[skill] += 1

            # Whose are the Unique skills
            for k in karvands:
                for skill, score in k["skills"].items():
                    if all_skills[skill] == 1:
                        unique_skills[skill] = k["full name"]

            # total skill scores ave
            if skills_num > 0:
                total_scores_ave = total_scores / skills_num
            else:
                total_scores_ave = 0

            # Printing the Full Report
            print(f"  - Tedade kol Karvand-ha: {karvands_num}")
            print(f"  - Tedade kol Mahaarat-ha: {skills_num}")
            print(f"  - miangin kol sathe Mahaarat-ha: {total_scores_ave}")
            print("  - miangin sathe Mahaarat-ha be ezaye Karvand: ")
            i = 1
            for name, score in per_ave.items():
                print(f"    {i}- {name}: {score}")
                i += 1
            print("  - Shahr-haye Sabt Shode: ")
            i = 1
            for name, score in all_cities.items():
                print(f"    {i}- {name}: {score}")
                i += 1
            print("  - Mahaarat-haye Unique: ")
            i = 1
            for name, score in unique_skills.items():
                print(f"    {i}- {name}: {score}")
                i += 1

            # Saving in json data/report.json
            report_path = "data/report.json"

            report = {
                "tedade kol": karvands_num,
                "tedade kol skills": skills_num,
                "miangin kol sathe skills": total_scores_ave,
                "miangin sathe skills per karvand": per_ave,
                "shahr_haye sabt shode": all_cities,
                "mahaarat_haye unique": unique_skills,
            }

            with open(report_path, "w") as file:
                json.dump(report, file, ensure_ascii=False, indent=4)

            print("\n:::::::::::::: [report] Zakhire ham Shod. ::::::::::::::\n")

        else:
            print("file json karvand-haa sakhte nashode!\n")

    # 6. Search With ID section
    elif command == 6:
        while True:
            try:
                searching_id = int(input("Id bede karvand bede: "))
                print("")
                break
            except ValueError:
                print("\nGoftam shomare ID vared kon...\n")

        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                data = json.load(file)
            karvands = data["karvands"]

            # searching
            founded = False
            for k in karvands:
                if k["id"] == searching_id:
                    founded = True
                    print("-" * 20)
                    print("Karvand ba in ID:\n")
                    print(f"  -name: {k['full name']}")
                    print(f"  -Email: {k['mail']}")
                    print(f"  -City: {k['city']}")
                    print(
                        f"  -education: {k['education']['field']}, maghta: {k['education']['degree']}"
                    )
                    print("  -skills:")
                    for skills, score in k["skills"].items():
                        print(f"     - {skills}: {score}")
                    print("-" * 20)
                    print("")
                    break

            if not founded:
                print("Nadrim!\n")

        else:
            print("file json karvand-haa sakhte nashode!\n")

    # 7. Searching with Skill section
    elif command == 7:
        while True:
            skill_searching = input("donbale che skilly hasti?: ")
            if skill_searching.isdigit():
                print("boro aziat nakon, skill adad nist!\n")
                continue
            else:
                break

        # openning file
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                data = json.load(file)
            karvands = data["karvands"]

            # the searching
            founded_karvands = {}
            for k in karvands:
                for skill, score in k["skills"].items():
                    if skill.lower() == skill_searching.lower():
                        founded_karvands[k["full name"]] = score
                        break

            # printing
            if founded_karvands:
                print("\nin afrad in skill ro daran:")
                for name, score in founded_karvands.items():
                    print(f"  - jenabe: {name}, ba sathe: {score}")
                print("")
            else:
                print("Haji hichki nadare!")

        else:
            print("file json karvand-haa sakhte nashode!\n")

    # Exit Section
    else:
        break
