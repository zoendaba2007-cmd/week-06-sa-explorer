PROVINCES = {
    "Gauteng": {
        "population": 16100000,
        "capital": "Johannesburg",
        "area": 18178,
        "languages": "Zulu, English, Afrikaans"
    },
    "KwaZulu-Natal": {
        "population": 11500000,
        "capital": "Pietermaritzburg",
        "area": 94361,
        "languages": "Zulu, English"
    },
    "Western Cape": {
        "population": 7400000,
        "capital": "Cape Town",
        "area": 129449,
        "languages": "Afrikaans, English, Xhosa"
    },
    "Eastern Cape": {
        "population": 6700000,
        "capital": "Bhisho",
        "area": 168966,
        "languages": "Xhosa, Afrikaans, English"
    },
    "Limpopo": {
        "population": 5900000,
        "capital": "Polokwane",
        "area": 125754,
        "languages": "Sepedi, Venda, Tsonga"
    },
    "Mpumalanga": {
        "population": 4700000,
        "capital": "Mbombela",
        "area": 76495,
        "languages": "Swati, Zulu, Ndebele"
    },
    "North West": {
        "population": 4100000,
        "capital": "Mahikeng",
        "area": 104882,
        "languages": "Setswana, Afrikaans"
    },
    "Free State": {
        "population": 2900000,
        "capital": "Bloemfontein",
        "area": 129825,
        "languages": "Sesotho, Afrikaans"
    },
    "Northern Cape": {
        "population": 1300000,
        "capital": "Kimberley",
        "area": 372889,
        "languages": "Afrikaans, Setswana, Xhosa"
    }
}


# Display the menu
def show_menu():
    print("\nSA Data Explorer")
    print("1. List all provinces")
    print("2. Show province details")
    print("3. Largest by population")
    print("4. Largest by area")
    print("5. Total SA population")
    print("0. Quit")


while True:
    show_menu()
    choice = input("Choose: ").strip()

    if choice == "0":
        print("Goodbye!")
        break

    elif choice == "1":
        for name in PROVINCES:
            print(f"- {name}")

    elif choice == "2":
        province = input("Province name: ").strip().lower()

        if province == "gauteng":
            p = PROVINCES["Gauteng"]
        elif province == "kwazulu-natal":
            p = PROVINCES["KwaZulu-Natal"]
        elif province == "western cape":
            p = PROVINCES["Western Cape"]
        elif province == "eastern cape":
            p = PROVINCES["Eastern Cape"]
        elif province == "limpopo":
            p = PROVINCES["Limpopo"]
        elif province == "mpumalanga":
            p = PROVINCES["Mpumalanga"]
        elif province == "north west":
            p = PROVINCES["North West"]
        elif province == "free state":
            p = PROVINCES["Free State"]
        elif province == "northern cape":
            p = PROVINCES["Northern Cape"]
        else:
            p = None

        if p:
            print(f"\nCapital: {p['capital']}")
            print(f"Population: {p['population']:,}")
            print(f"Area: {p['area']:,} km²")
            print(f"Languages: {p['languages']}")
        else:
            print("Province not found.")

    elif choice == "3":
        top = max(PROVINCES, key=lambda n: PROVINCES[n]["population"])
        print(f"\nLargest by population: {top}")
        print(f"Population: {PROVINCES[top]['population']:,}")

    elif choice == "4":
        top = max(PROVINCES, key=lambda n: PROVINCES[n]["area"])
        print(f"\nLargest by area: {top}")
        print(f"Area: {PROVINCES[top]['area']:,} km²")

    elif choice == "5":
        total = sum(p["population"] for p in PROVINCES.values())
        print(f"\nTotal SA population: {total:,}")

    else:
        print("Invalid choice.")