def test_check_number_of_characters():
    phrase = input("Set a phrase less than 15 characters long: ")

    number_of_characters = len(phrase)

    expected_number = 15

    assert number_of_characters > 0, "Empty phrase"
    assert number_of_characters <= expected_number, f"Phrase length is not equal to {expected_number}. Phrase length is {number_of_characters}"

