def life_in_weeks(age):
    expected = 90 * 52
    spended = age * 52
    remaining = expected - spended
    print(f"You have {remaining} weeks left.")

life_in_weeks(48)