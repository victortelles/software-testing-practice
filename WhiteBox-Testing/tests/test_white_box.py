# -*- coding: utf-8 -*-

"""
White-box unit testing examples.
"""
import io
import unittest
from unittest import mock

from src.white_box import (
    BankAccount,
    BankingSystem,
    DocumentEditingSystem,
    ElevatorSystem,
    Product,
    ShoppingCart,
    TrafficLight,
    UserAuthentication,
    VendingMachine,
    authenticate_user,
    calculate_items_shipping_cost,
    calculate_order_total,
    calculate_quantity_discount,
    calculate_shipping_cost,
    calculate_total_discount,
    categorize_product,
    celsius_to_fahrenheit,
    check_file_size,
    check_flight_eligibility,
    check_loan_eligibility,
    check_number_status,
    divide,
    get_grade,
    get_weather_advisory,
    grade_quiz,
    is_even,
    is_triangle,
    validate_credit_card,
    validate_date,
    validate_email,
    validate_login,
    validate_password,
    validate_url,
    verify_age,
)

# from src.white_box import VendingMachine, divide, get_grade, is_even, is_triangle


class TestWhiteBoxIsEven(unittest.TestCase):
    """White-box unittest class."""

    # Test cases 0.1 = "is_even(num)"
    def test_is_even_with_even_number(self):
        """Checks if a number is even."""
        self.assertTrue(is_even(0))

    def test_is_even_with_odd_number(self):
        """Checks if a number is not even."""
        self.assertFalse(is_even(7))

    def test_is_even_with_zero(self):
        """Check if zero is considered even"""
        self.assertTrue(is_even(0))

    def test_is_even_with_negative_even_number(self):
        """Check if a negative even number is even"""
        self.assertTrue(is_even(-4))

    def test_is_even_with_negative_odd_number(self):
        """Checks if a negative odd number is not event."""
        self.assertFalse(is_even(-3))


class TestWhiteBoxDivide(unittest.TestCase):
    """White-box unittest class."""

    # Test cases 0.2 = "divide(a, b)"
    def test_divide_by_non_zero(self):
        """Checks the divide function works as expected."""
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_zero(self):
        """Checks the divide function returns 0 when dividing by 0."""
        self.assertEqual(divide(10, 0), 0)

    def test_divide_positive_numbers(self):
        """Check division of two positive numbers."""
        self.assertEqual(divide(10, 2), 5)

    def test_divide_negative_numbers(self):
        """Checks division of two negative numbers"""
        self.assertEqual(divide(-10, -2), 5)

    def test_divide_positive_by_negative(self):
        """Checks division of a positive numbers by a negative number."""
        self.assertEqual(divide(10, -2), -5)

    def test_divide_negative_by_positive(self):
        """Checks division of a negative number by a positive number."""
        self.assertEqual(divide(-10, 2), -5)

    def test_divide_by_one(self):
        """Checks division of a number by one"""
        self.assertEqual(divide(10, 1), 10)

    def test_divide_zero_by_number(self):
        """Checks division of zero by any number returns zero."""
        self.assertEqual(divide(0, 10), 0)


class TestWhiteBoxGrades(unittest.TestCase):
    """White-box unittest class."""

    # Test cases 0.3 = "get_grade(score)"
    def test_get_grade_a(self):
        """Checks if a score of 90 or higher returns grade 'A'."""
        self.assertEqual(get_grade(95), "A")

    def test_get_grade_b(self):
        """Checks if a score between 80-89 returns grade 'B'."""
        self.assertEqual(get_grade(85), "B")

    def test_get_grade_c(self):
        """Checks if a score between 70-79 returns grade 'C'."""
        self.assertEqual(get_grade(75), "C")

    def test_get_grade_f(self):
        """Checks if a score below 70 returns grade 'F'."""
        self.assertEqual(get_grade(65), "F")


class TestWhiteBoxTriangle(unittest.TestCase):
    """White-box unittest class."""

    # Test cases 0.4 = "is_triangle(a, b, c)"
    def test_is_triangle_yes(self):
        """Checks the three inputs can form a triangle."""
        self.assertEqual(is_triangle(3, 4, 5), "Yes, it's a triangle!")

    def test_is_triangle_no_1(self):
        """Checks the three inputs can't form a triangle when C is greater or equal than A + B."""
        self.assertEqual(is_triangle(3, 4, 7), "No, it's not a triangle.")

    def test_is_triangle_no_2(self):
        """Checks the three inputs can't form a triangle when B is greater or equal than A + C."""
        self.assertEqual(is_triangle(2, 3, 1), "No, it's not a triangle.")

    def test_is_triangle_no_3(self):
        """Checks the three inputs can't form a triangle when A is greater or equal than B + C."""
        self.assertEqual(is_triangle(2, 1, 1), "No, it's not a triangle.")

    def test_is_triangle_equilateral(self):
        """Checks if three equal sides form a valid triangle."""
        self.assertEqual(is_triangle(1, 1, 1), "Yes, it's a triangle!")

    def test_is_triangle_zero_side(self):
        """Checks behaivor when one side is zero"""
        self.assertEqual(is_triangle(0, 4, 5), "No, it's not a triangle.")


class TestWhiteBoxCheckNum(unittest.TestCase):
    """White-box unittest class."""

    # Test cases 1 = "check_number_status(number)"
    def test_check_number_status_positive(self):
        """Checks if a positive number returns "Positive"."""
        self.assertEqual(check_number_status(10), "Positive")

    def test_check_number_status_negative(self):
        """Checks if a negative number returns "Negative"."""
        self.assertEqual(check_number_status(-10), "Negative")

    def test_check_number_status_decimal_positive(self):
        """Checks if a positive number returns "Positive"."""
        self.assertEqual(check_number_status(0.1), "Positive")

    def test_check_number_status_decimal_negative(self):
        """Checks if a negative number returns "Negative"."""
        self.assertEqual(check_number_status(-0.1), "Negative")

    def test_check_number_status_zero(self):
        """Checks if zero returns "Zero"."""
        self.assertEqual(check_number_status(0), "Zero")


class TestWhiteBoxValidatePass(unittest.TestCase):
    """White-box unittest class - #2 Validate_password."""

    # Test cases 2 = "validate_password(password)"
    def test_validate_password_valid(self):
        """Checks if a valid password thats meets all requerimetns returns True."""
        self.assertTrue(validate_password("Password1!"))

    def test_validate_password_too_short(self):
        """Checks if a password with less than 8 characters returns False"""
        self.assertFalse(validate_password("Pa1!"))

    def test_validate_password_no_uppercase(self):
        """Check if a password without uppercase letters returns False"""
        self.assertFalse(validate_password("password1!"))

    def test_validate_password_no_lowercase(self):
        """Check if a password without lowercase letters returns False"""
        self.assertFalse(validate_password("PASSWORD1!"))

    def test_validate_password_no_digit(self):
        """Check if a password without digits returns False"""
        self.assertFalse(validate_password("Password!"))

    def test_validate_password_no_special_char(self):
        """Check if a password without special characters returns False"""
        self.assertFalse(validate_password("Password1"))

    def test_validate_password_exact_length(self):
        """Check if a password with exactly 8 characters returns True"""
        self.assertTrue(validate_password("Password1!"))

    def test_validate_password_long_password(self):
        """Check if a password with more than 8 characters returns True"""
        self.assertTrue(validate_password("Password1!Password1!"))

    def test_validate_password_with_invalid_special_char(self):
        """Checks if a password with special characters not in the required set returns False."""
        self.assertFalse(validate_password("Password1*"))


class TestWhiteBoxCalculatorTotalDiscount(unittest.TestCase):
    """White-box unittest class - #3 Calculator_total_discount."""

    # Test cases 3 = "calculate_total_discount(total_amount)"
    def test_calculate_total_discount_below_shreshold(self):
        """Checks if amounts below 100 receive no discount."""
        self.assertEqual(calculate_total_discount(99), 0)

    def test_calculate_total_discount_at_lower_threshould(self):
        """Checks if amount exactly at 100 receives 10% discount."""
        self.assertEqual(calculate_total_discount(100), 10)

    def test_calculate_total_discount_in_first_range(self):
        """Checks if amount in the first range (100-500) range receives 10% discount."""
        self.assertEqual(calculate_total_discount(200), 20)

    def test_calculate_total_discount_at_upper_threshold(self):
        """Checks if amount exactly at 500 receives 10% discount."""
        self.assertEqual(calculate_total_discount(500), 50)

    def test_calculate_total_discount_above_threshold(self):
        """Checks if amount above 500 receive 20% discount."""
        self.assertEqual(calculate_total_discount(600), 120)

    def test_calculate_total_discount_large_amount(self):
        """Checks if very large amounts receive 20% discount correctly"""
        self.assertEqual(calculate_total_discount(10000), 2000)

    def test_calculate_total_discount_zero(self):
        """Checks if zero amount receives no discount"""
        self.assertEqual(calculate_total_discount(0), 0)

    def test_calculate_total_discount_negative(self):
        """Checks handling of negative amounts."""
        self.assertEqual(calculate_total_discount(-100), 0)


class TestWhiteBoxCalculateOrderTotal(unittest.TestCase):
    """White-box unittest class - #4 calculate_order_total."""

    # Test cases 4 = "calculate_order_total(items)"
    def test_calculate_order_total_empty(self):
        """Checks if an empty items list returns zero total."""
        self.assertEqual(calculate_order_total([]), 0)

    def test_calculate_order_total_single_item_no_discount(self):
        """Checks calculation for a single item with quantity in the no-discount range (1-5)."""
        items = [{"quantity": 3, "price": 10}]
        self.assertEqual(calculate_order_total(items), 30)

    def test_calculate_order_total_single_item_small_discount(self):
        """Checks calculation for a single item with quantity in the 5% discount range (6-10)"""
        items = [{"quantity": 8, "price": 10}]
        self.assertEqual(calculate_order_total(items), 76)

    def test_calculate_order_total_single_item_large_discount(self):
        """Checks calculation for a single item with quantity in the 10% discount range (> 10)."""
        items = [{"quantity": 15, "price": 10}]
        self.assertEqual(calculate_order_total(items), 135)

    def test_calculate_order_total_zero_quantity(self):
        """Checks Handling of zero quantity items"""
        items = [{"quantity": 0, "price": 10}]
        self.assertEqual(calculate_order_total(items), 0)


class TestWhiteBoxCalculateItemsShipingCost(unittest.TestCase):
    """White-box unittest class - #5 calculate_items_shipping_cost."""

    # Test cases 5 = "calculate_items_shipping_cost(items)"
    def test_calculate_items_shipping_cost_standard_low_weight(self):
        """Checks standard shipping cost for weight <= 5."""
        items = [{"weight": 2}, {"weight": 1}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 10)

    def test_calculate_items_shipping_cost_standard_medium_weight(self):
        """Checks standard shipping cost for weight between 5 and 10"""
        items = [{"weight": 3}, {"weight": 5}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 15)

    def test_calculate_items_shipping_cost_standard_high_weight(self):
        """Checks standard shipping cost for weight > 10"""
        items = [{"weight": 11}, {"weight": 12}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 20)

    def test_calculate_items_shipping_cost_express_low_weight(self):
        """Checks express shipping cost for weight <= 5"""
        items = [{"weight": 2}, {"weight": 2.5}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 20)

    def test_calculate_items_shipping_cost_express_medium_weight(self):
        """Checks express shipping cost for weight between 5 and 10"""
        items = [{"weight": 3}, {"weight": 6}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 30)

    def test_calculate_items_shipping_cost_exppress_high_weight(self):
        """Checks express shipping cost for weight > 10"""
        items = [{"weight": 11}, {"weight": 12}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 40)

    def test_calculate_items_shipping_cost_empty_items(self):
        """Check shipping cost for an empty items list"""
        self.assertEqual(calculate_items_shipping_cost([], "standard"), 10)


class TestWhiteBoxValidateLogin(unittest.TestCase):
    """White-box unittest class - #6 validate_login."""

    # Test cases 6 = "validate_login(username, password)"
    def test_validate_login_successful(self):
        """Checks if valid username and password combination returns 'Login Successful'."""
        self.assertEqual(validate_login("validuser", "password123"), "Login Successful")

    def test_validate_login_username_too_short(self):
        """Checks if username shorter than 5 characters returns 'Login Failed'."""
        self.assertEqual(validate_login("user", "password123"), "Login Failed")

    def test_validate_login_username_too_long(self):
        """Checks if username longer than 20 characters returns 'Login Failed'."""
        self.assertEqual(
            validate_login("thisusernameiswaytoolong", "password123"), "Login Failed"
        )

    def test_validate_login_password_too_short(self):
        """Checks if password shorter than 5 characters returns 'Login Failed'."""
        self.assertEqual(validate_login("validuser", "pass"), "Login Failed")

    def test_validate_login_password_too_long(self):
        """Checks if password longer than 15 characters returns 'Login Failed'."""
        self.assertEqual(validate_login("validuser", "pass"), "Login Failed")

    def test_validate_login_boundary_username_min(self):
        """Checks login with username at minimum length boundary (5 characters)."""
        self.assertEqual(validate_login("user1", "password123"), "Login Successful")

    def test_validate_login_boundary_username_max(self):
        """Checks login with username at maximum length boundary (20 characters)."""
        self.assertEqual(
            validate_login("usernameistwentychar", "password123"), "Login Successful"
        )

    def test_validate_login_boundary_password_min(self):
        """Checks login with password at minimum length boundary (8 characters)."""
        self.assertEqual(validate_login("validuser", "pass1234"), "Login Successful")

    def test_validate_login_boundary_password_max(self):
        """Checks login with password at maximum length boundary (15 characters)."""
        self.assertEqual(
            validate_login("validuser", "passwordfifteen"), "Login Successful"
        )


class TestWhiteBoxVerifyAge(unittest.TestCase):
    """White-box unittest class - #7 verify_age."""

    # Test cases 7 = "verify_age(age)"
    def test_verify_age_eligible_minimum(self):
        """Checks if age at lower boundary (18) returns 'Eligible'."""
        self.assertEqual(verify_age(18), "Eligible")

    def test_verify_age_eligible_maximum(self):
        """Checks if age at upper boundary (65) returns 'Eligible'."""
        self.assertEqual(verify_age(65), "Eligible")

    def test_verify_age_not_elegible_below(self):
        """Checks if age below lower boundary (17) returns 'Not Eligible'."""
        self.assertEqual(verify_age(17), "Not Eligible")

    def test_verify_age_zero(self):
        """Checks if age zero returns 'Not Eligible'."""
        self.assertEqual(verify_age(0), "Not Eligible")

    def test_verify_age_very_old(self):
        """Checks if age above upper boundary (100) returns 'Not Eligible'."""
        self.assertEqual(verify_age(100), "Not Eligible")


class TestWhiteBoxCategorizeProduct(unittest.TestCase):
    """White-box unittest class - #8 categorize_product."""

    # Test cases 8 = "categorize_product(product_name)"
    def test_categorize_product_lower_boundary(self):
        """Checks if price at lower boundary of Category A (10) returns 'Category A'."""
        self.assertEqual(categorize_product(10), "Category A")

    def test_categorize_product_a_upper_boundary(self):
        """Checks if price at upper boundary of Category A (50) returns 'Category A'."""
        self.assertEqual(categorize_product(50), "Category A")

    def test_categorize_product_b_lower_boundary(self):
        """Checks if price at lower boundary of Category B (51) returns 'Category B'."""
        self.assertEqual(categorize_product(51), "Category B")

    def test_categorize_product_b_upper_boundary(self):
        """Checks if price at upper boundary of Category B (100) returns 'Category B'."""
        self.assertEqual(categorize_product(100), "Category B")

    def test_categorize_product_c_lower_boundary(self):
        """Checks if price at lower boundary of Category C (101) returns 'Category C'."""
        self.assertEqual(categorize_product(101), "Category C")

    def test_categorize_product_c_upper_boundary(self):
        """Checks if price at upper boundary of Category C (200) returns 'Category C'."""
        self.assertEqual(categorize_product(200), "Category C")

    def test_categorize_product_d_below(self):
        """Checks if price below lower boundary of Category D (9) returns 'Category D'."""
        self.assertEqual(categorize_product(9), "Category D")

    def test_categorize_product_d_above(self):
        """Checks if price above upper boundary of Category D (201) returns 'Category D'."""
        self.assertEqual(categorize_product(201), "Category D")


class TestWhiteBoxValidateEmail(unittest.TestCase):
    """White-box unittest class - #9 validate_email."""

    # Test cases 9 = "validate_email(email)"
    def test_validate_email_valid(self):
        """Checks if a properly formatted email returns  'Valid Email'."""
        self.assertEqual(validate_email("test@example.com"), "Valid Email")

    def test_validate_email_too_short(self):
        """Checks if email shorter than 5 characters returns 'Invalid Email'."""
        self.assertEqual(validate_email("t@e."), "Invalid Email")

    def test_validate_email_too_long(self):
        """Checks if email longer than 50 characters returns 'Invalid Email'."""
        self.assertEqual(
            validate_email(
                "thisisaverylongemailthatexceedsfiftycharacters@example.com"
            ),
            "Invalid Email",
        )

    def test_validate_email_no_at_symbol(self):
        """Checks if email without @ symbol returns 'Invalid Email'."""
        self.assertEqual(validate_email("testexample.com"), "Invalid Email")

    def test_validate_email_no_dot(self):
        """Checks if email without dot returns 'Invalid Email'."""
        self.assertEqual(validate_email("test@examplecom"), "Invalid Email")

    def test_validate_email_minium_length(self):
        """Checks if email with exact minium length (5) returns 'Valid Email'."""
        self.assertEqual(validate_email("test@.com"), "Valid Email")

    def test_validate_email_maxium_length(self):
        """Checks if email with exact maximum length (50) returns 'Valid Email'."""
        self.assertEqual(
            validate_email("testemailexampleforlongcharacterssssss@example.com"),
            "Valid Email",
        )

    def test_validate_email_empty_string(self):
        """Checks if empty string returns 'Invalid Email'."""
        self.assertEqual(validate_email(""), "Invalid Email")


class TestWhiteBoxCelsiusToFahrenheit(unittest.TestCase):
    """White-box unittest class - #10 celsius_to_fahrenheit."""

    # Test cases 10 = "celsius_to_fahrenheit(celsius)"
    def test_celsius_to_fahrenheit_zero(self):
        """Checks conversion of 0°C to Fahrenheit"""
        self.assertEqual(celsius_to_fahrenheit(0), 32)

    def test_celsius_to_fahrenheit_positive(self):
        """Checks conversion of positive Celsius temperature to Fahrenheit"""
        self.assertEqual(celsius_to_fahrenheit(20), 68)

    def test_celsius_to_fahrenheit_negative(self):
        """Checks conversion of negative Celsius temperature to Fahrenheit"""
        self.assertEqual(celsius_to_fahrenheit(-10), 14)

    def test_celsius_to_fahrenheit_lower_boundary(self):
        """Checks conversion at lower boundary (-100°C) of valid range"""
        self.assertEqual(celsius_to_fahrenheit(-100), -148)

    def test_celsius_to_fahrenheit_upper_boundary(self):
        """Checks conversion at upper boundary (100°C) of valid range"""
        self.assertEqual(celsius_to_fahrenheit(100), 212)

    def test_celsius_to_fahrenheit_below_range(self):
        """Checks handling of temperature below valid range."""
        self.assertEqual(celsius_to_fahrenheit(-101), "Invalid Temperature")

    def test_celsius_to_fahrenheit_above_range(self):
        """Checks handling of temperature above valid range."""
        self.assertEqual(celsius_to_fahrenheit(101), "Invalid Temperature")


class TestWhiteBoxValidateCreditCard(unittest.TestCase):
    """White-box unittest class - #11 validate_credit_card."""

    # Test cases 11 = "validate_credit_card(card_number)"
    def test_validate_credit_card_valid_min(self):
        """Checks if credit card with minimum valid length (13 digits) return 'Valid Card'."""
        self.assertEqual(validate_credit_card("1234567890123"), "Valid Card")

    def test_validate_credit_card_valid_max(self):
        """Checks if credit card with maximum valid length (16 digits) return 'Valid Card'."""
        self.assertEqual(validate_credit_card("1234567890123456"), "Valid Card")

    def test_validate_credit_card_too_short(self):
        """Checks if credit card number too short (12 digits) returns 'Invalid Card'."""
        self.assertEqual(validate_credit_card("123456789012"), "Invalid Card")

    def test_valdiate_credit_card_too_long(self):
        """Checks if credit card number too long (17 digits) returns 'Invalid Card'."""
        self.assertEqual(validate_credit_card("12345678901234567"), "Invalid Card")

    def test_validate_credit_card_non_digit(self):
        """Checks if credit card with non-digit characters returns 'Invalid Card'."""
        self.assertEqual(validate_credit_card("a1234567890123"), "Invalid Card")

    def test_validate_credit_card_with_spaces(self):
        """Checks if credit card with spaces returns 'Invalid Card'."""
        self.assertEqual(validate_credit_card(" 12345 6789 0123"), "Invalid Card")

    def test_validate_credit_card_empty_string(self):
        """Checks if empty string returns 'Invalid Card'."""
        self.assertEqual(validate_credit_card(""), "Invalid Card")


class TestWhiteBoxValidateDate(unittest.TestCase):
    """White-box unittest class - #12 validate_date."""

    # Test cases 12 = "validate_date(date_string)"
    def test_validate_date_valid(self):
        """Checks if a valid date returns 'Valid Date'."""
        self.assertEqual(validate_date(2022, 1, 1), "Valid Date")

    def test_validate_date_year_too_early(self):
        """Checks if year before 1900 returns 'Invalid Date'."""
        self.assertEqual(validate_date(1899, 5, 15), "Invalid Date")

    def test_validate_date_year_too_late(self):
        """Checks if year after 2100 returns 'Invalid Date'."""
        self.assertEqual(validate_date(2101, 5, 15), "Invalid Date")

    def test_validate_date_month_too_low(self):
        """Checks if month below 1 returns 'Invalid Date'."""
        self.assertEqual(validate_date(2000, 0, 15), "Invalid Date")

    def test_validate_date_month_too_high(self):
        """Checks if mont above 12 returns 'Invalid Date'."""
        self.assertEqual(validate_date(2000, 13, 15), "Invalid Date")

    def test_validate_date_day_too_low(self):
        """Checks if day below 1 returns 'Invalid Date'."""
        self.assertEqual(validate_date(2000, 5, 0), "Invalid Date")

    def test_validate_date_day_too_high(self):
        """Checks if day above 31 returns 'Invalid Date'."""
        self.assertEqual(validate_date(2000, 5, 32), "Invalid Date")

    def test_validate_date_year_boundary_min(self):
        """Checks if year lower boundary (1900) returns 'Valid Date'"""
        self.assertEqual(validate_date(1900, 5, 15), "Valid Date")

    def test_validate_date_year_boundary_max(self):
        """Checks if year upper boundary (2100) returns 'Valid Date"""
        self.assertEqual(validate_date(2100, 5, 15), "Valid Date")

    def test_validate_date_month_boundary_min(self):
        """Checks if month at lower boundary (1) returns 'Valid Date'."""
        self.assertEqual(validate_date(2000, 1, 15), "Valid Date")

    def test_validate_date_month_boundary_max(self):
        """Checks if month at upper boundary (12) return 'Valid Date'."""
        self.assertEqual(validate_date(2000, 12, 15), "Valid Date")

    def test_validate_date_day_boundary_min(self):
        """Checks if day at lower boundary (1) returns 'Valid Date'."""
        self.assertEqual(validate_date(2000, 5, 1), "Valid Date")

    def test_validate_date_day_boundary_max(self):
        """Checks if day at upper boundary (31) returns 'Valid Date."""
        self.assertEqual(validate_date(2000, 5, 31), "Valid Date")


class TestWhiteBoxCheckFlightEligibility(unittest.TestCase):
    """White-box unittest class - #13 check_flight_eligibility(age, frequent_flyer)."""

    # Test cases 12 = "validate_date(date_string)"

    def test_check_flight_eligible_age_not_frequent_flyer(self):
        """Checks if eligible age (18-65) but not frequent flyer returns 'Eligible to Book'."""
        self.assertEqual(check_flight_eligibility(30, False), "Eligible to Book")

    def test_check_flight_not_elegible_age_not_frequent_flyer(self):
        """Checks if not eligible age <18 or >65 and not frequent flyer '."""
        self.assertEqual(check_flight_eligibility(16, False), "Not Eligible to Book")
        self.assertEqual(check_flight_eligibility(70, False), "Not Eligible to Book")

    def test_check_flight_eligible_age_and_frequent_flyer(self):
        """Checks if elihible age and frequent flyer returns 'Eligible to Book'."""
        self.assertEqual(check_flight_eligibility(30, True), "Eligible to Book")

    def test_check_flight_eligibility_boundary_lower_age_not_frequent_flyer(self):
        """Checks if age at lower boundary (18) and not frequent flyer."""
        self.assertEqual(check_flight_eligibility(18, False), "Eligible to Book")

    def test_check_flight_eligibility_boundary_upper_age_not_frequent_flyer(self):
        """Checks if age at upper boundary (65) and not frequent flyer."""
        self.assertEqual(check_flight_eligibility(65, False), "Eligible to Book")

    def test_check_flight_eligibility_just_below_min_age_not_frequent_flyer(self):
        """Check if age just below minimum (17) and not frequent flyer."""
        self.assertEqual(check_flight_eligibility(17, False), "Not Eligible to Book")

    def test_check_flight_elegibility_just_above_max_age_not_frequent_flyer(self):
        """Check if age just above maximum (66) and not frequent flyer."""
        self.assertEqual(check_flight_eligibility(66, False), "Not Eligible to Book")


class TestWhiteBoxValidateURL(unittest.TestCase):
    """White-box unittest class - #14 validate_url(url)."""

    # Test cases 14 = "validate_url(url)"
    def test_validate_url_http(self):
        """Check if a valid HTTP URL returns 'Valid URL'."""
        self.assertEqual(validate_url("http://example.com"), "Valid URL")

    def test_validate_url_valid_https(self):
        """Check if a valid HTTPS URL returns 'Valid URL'"""
        self.assertEqual(validate_url("https://example.ccom"), "Valid URL")

    def test_validate_url_no_protocol(self):
        """Checks if URL Without protocol returns 'Invalid URL'."""
        self.assertEqual(validate_url("example.com"), "Invalid URL")

    def test_validate_url_invalid_protocol(self):
        """Checks if URL with invalid protocol returns 'Invalid URL'."""
        self.assertEqual(validate_url("www://example.com"), "Invalid URL")

    def test_validate_url_too_long(self):
        """Checks if URL longer than 255 characters returns 'Invalid URL'."""
        long_url = "http://" + "a" * 250 + ".com"
        self.assertEqual(validate_url(long_url), "Invalid URL")

    def test_validate_url_max_lenght(self):
        """Checks if URL at maximum length (255) returns 'Valid URL'."""
        max_url = "http://" + "a" * 244 + ".com"
        self.assertEqual(validate_url(max_url), "Valid URL")

    def test_validate_url_empty(self):
        """Checks if empty string returns 'Invalid URL'."""
        self.assertEqual(validate_url(""), "Invalid URL")


class TestWhiteBoxCalculateQuantityDiscount(unittest.TestCase):
    """White-box unittest class - #15 calculate_quantity_discount(quantity)."""

    # Test cases 15 = "calculate_quantity_discount(quantity)"
    def test_calculate_quantity_discount_no_discount_lower_bound(self):
        """Checks if quantity at lower bound (1) returns 'No discount'."""
        self.assertEqual(calculate_quantity_discount(1), "No Discount")

    def test_calculate_quantity_discount_no_discount_upper_bound(self):
        """Checks if quantity at upper bound (5) returns 'No Discount'"""
        self.assertEqual(calculate_quantity_discount(5), "No Discount")

    def test_calculate_quantity_discount_small_discount_lower_bound(self):
        """Check if quantity at lower bound of 5% discount range (6) returns '5% Discount'."""
        self.assertEqual(calculate_quantity_discount(6), "5% Discount")

    def test_calculate_quantity_discount_small_discount_upper_bound(self):
        """Checks if quantity at upper bound of 5% discount range (10) returns '5% Discount'."""
        self.assertEqual(calculate_quantity_discount(10), "5% Discount")

    def test_calculate_quantity_discount_large_discount_minimum(self):
        """Checks if quantity at minimum for 10% discount (11) returns '10% Discount'."""
        self.assertEqual(calculate_quantity_discount(11), "10% Discount")


class TestWhiteBoxCheckFileSize(unittest.TestCase):
    """White-box unittest class - #16 check_file_size(size_in_bytes)."""

    # Test cases 16 = "check_file_size(size_in_bytes)"
    def test_check_file_size_zero(self):
        """Checks if zero bytes returns 'Valid File Size'."""
        self.assertEqual(check_file_size(0), "Valid File Size")

    def test_check_file_size_max(self):
        """Checks if maximum allowed size (1 MB) returns 'Valid File Size'."""
        self.assertEqual(check_file_size(1048576), "Valid File Size")

    def test_check_file_size_exceeded(self):
        """Checks if supported maximum allowe size (+1MB) returns 'Invalid File Size'."""
        self.assertEqual(check_file_size(1048577), "Invalid File Size")

    def test_check_file_size_negative(self):
        """Checks if negative size returns 'Invalid File Size'."""
        self.assertEqual(check_file_size(-1), "Invalid File Size")


class TestWhiteBoxCheckLoanEligibility(unittest.TestCase):
    """White-box unittest class - #17 check_loan_eligibility(income, credit_score)."""

    # Test cases 17 = "check_loan_eligibility(income, credit_score)"
    def test_check_loan_eligibility_with_icome_below_minimum(self):
        """Check if loan is denied when income is below the minimum threshold."""
        self.assertEqual(check_loan_eligibility(29999, 800), "Not Eligible")
        self.assertEqual(check_loan_eligibility(0, 800), "Not Eligible")
        self.assertEqual(check_loan_eligibility(-5000, 800), "Not Eligible")

    def test_check_loan_eligibility_with_medium_income_high_credit(self):
        """Checks if standard loan is granted with medium income and high credit score."""
        self.assertEqual(check_loan_eligibility(30000, 701), "Standard Loan")
        self.assertEqual(check_loan_eligibility(45000, 750), "Standard Loan")
        self.assertEqual(check_loan_eligibility(60000, 800), "Standard Loan")

    def test_check_loan_eligibility_with_medium_income_low_credit(self):
        """Checks if secured loan is granted with medium income and low credit score."""
        self.assertEqual(check_loan_eligibility(30000, 700), "Secured Loan")
        self.assertEqual(check_loan_eligibility(45000, 650), "Secured Loan")
        self.assertEqual(check_loan_eligibility(60000, 500), "Secured Loan")

    def test_check_loan_eligibility_with_high_income_high_credit(self):
        """Check if premium loan is granted with high income and very high credit score"""
        self.assertEqual(check_loan_eligibility(60001, 751), "Premium Loan")
        self.assertEqual(check_loan_eligibility(100000, 800), "Premium Loan")

    def test_check_loan_eligibility_with_high_income_medium_credit(self):
        """Check if standard loan is granted with high income but medium credit score."""
        self.assertEqual(check_loan_eligibility(60001, 750), "Standard Loan")
        self.assertEqual(check_loan_eligibility(100000, 700), "Standard Loan")
        self.assertEqual(check_loan_eligibility(80000, 600), "Standard Loan")


class TestWhiteBoxCalculateShippingCost(unittest.TestCase):
    """White-box unittest class - #18 check_loan_eligibility(income, credit_score)."""

    # Test cases 18 = "calculate_shipping_cost(weight, length, width, height)"
    def test_calculate_shipping_cost_with_smalal_package(self):
        """Check shipping cost for small package"""
        self.assertEqual(calculate_shipping_cost(1, 10, 10, 10), 5)

    def test_calculate_shipping_cost_with_medium_package(self):
        """Check shipping cost for medium package."""
        self.assertEqual(calculate_shipping_cost(5, 30, 30, 30), 10)

    def test_calculate_shipping_cost_with_large_package(self):
        """Check shipping cost for large package."""
        self.assertEqual(calculate_shipping_cost(6, 31, 31, 31), 20)

    def test_calculate_shipping_cost_with_mixed_dimensions(self):
        """Check shipping cost when some dimensions are in different categories."""
        self.assertEqual(calculate_shipping_cost(2, 10, 15, 20), 20)


class TestWhiteBoxGradeQuiz(unittest.TestCase):
    """White-box unittest class - #19 check_loan_eligibility(income, credit_score)."""

    # Test cases 19 = "grade_quiz(correct_answers, incorrect_answers)"
    def test_grade_quiz_with_pass(self):
        """Check if quiz passes with sufficient correct answer and few incorrect answer."""
        self.assertEqual(grade_quiz(7, 2), "Pass")

    def test_grade_quiz_with_conditional_pass(self):
        """Check if quiz gets conditional pass with moderate correct answers and few incorrect"""
        self.assertEqual(grade_quiz(5, 3), "Conditional Pass")

    def test_grade_quiz_with_fail(self):
        """Check if quiz fails with insufficient correct answers or too many incorrect answers."""
        self.assertEqual(grade_quiz(4, 4), "Fail")


class TestWhiteBoxAuthenticateUser(unittest.TestCase):
    """White-box unittest class - #20 authenticate_user(username, password)."""

    # Test cases 20 = "authenticate_user(username, password)"
    def test_authenticate_user_with_admin_credentials(self):
        """Check Authentication with admin credentials."""
        self.assertEqual(authenticate_user("admin", "admin123"), "Admin")

    def test_authenticate_user_with_valid_user_credentials(self):
        """Checks autentication with valid user credentials."""
        self.assertEqual(authenticate_user("username", "password123"), "User")

    def test_authenticate_user_with_invalid_credentials(self):
        """Checks authentication with invalid credentials."""
        self.assertEqual(authenticate_user("user", "pass"), "Invalid")


class TestWhiteBoxGetWeatherAdvisory(unittest.TestCase):
    """White-box unittest class - #21 get_weather_advisory(temperature, humidity)."""

    # Test cases 21 = "get_weather_advisory(temperature, humidity)"
    def test_get_weather_advisory_with_high_temperature_and_humidity(self):
        """Check weather advisory for high temperature and humidity"""
        self.assertEqual(
            get_weather_advisory(31, 71),
            "High Temperature and Humidity. Stay Hydrated.",
        )

    def test_get_weather_advisory_with_low_temperature(self):
        """Check weather advisory for low temperature."""
        self.assertEqual(get_weather_advisory(-1, 50), "Low Temperature. Bundle Up!")

    def test_get_weather_advisory_with_no_specific_condition(self):
        """Check weather advisory for normal conditions."""
        self.assertEqual(get_weather_advisory(20, 50), "No Specific Advisory")


class TestWhiteBoxVendingMachine(unittest.TestCase):
    """White-box unittest class - class for Vending Machine."""

    # Test cases 22 = VendingMachine"
    def test_vending_machine_initial_state(self):
        """Check if vending machine initializes in 'Ready' State"""
        machine = VendingMachine()
        self.assertEqual(machine.state, "Ready")

    def test_vending_machine_insert_coin_when_ready(self):
        """Check insert_coin behavior when in 'Ready' state"""
        machine = VendingMachine()
        self.assertEqual(machine.insert_coin(), "Coin Inserted. Select your drink.")
        self.assertEqual(machine.state, "Dispensing")

    def test_vending_machine_insert_coin_when_dispensing(self):
        """Check insert_coin behavior when id 'Dispensing' state."""
        machine = VendingMachine()
        machine.state = "Dispensing"
        self.assertEqual(machine.insert_coin(), "Invalid operation in current state.")
        self.assertEqual(machine.state, "Dispensing")

    def test_vending_machine_select_drink_when_dispensing(self):
        """Check select_drink behavior when in 'Dispensing' state"""
        machine = VendingMachine()
        machine.state = "Dispensing"
        self.assertEqual(machine.select_drink(), "Drink Dispensed. Thank you!")
        self.assertEqual(machine.state, "Ready")

    def test_vending_select_drink_when_ready(self):
        """Check select_drink behavior when in 'Ready' state"""
        machine = VendingMachine()
        self.assertEqual(machine.select_drink(), "Invalid operation in current state.")
        self.assertEqual(machine.state, "Ready")


class TestWhiteBoxTrafficLight(unittest.TestCase):
    """White-box unittest class - #23 TrafficLight."""

    # Test cases 23 = "TrafficLight"
    def test_traffic_light_initial_state(self):
        """Check if traffic light initializes in 'Red' State"""
        light = TrafficLight()
        self.assertEqual(light.get_current_state(), "Red")

    def test_traffic_light_change_state_from_red(self):
        """Check state change behaivor when in 'Red' State"""
        light = TrafficLight()
        light.change_state()
        self.assertEqual(light.get_current_state(), "Green")

    def test_traffic_light_change_state_from_green(self):
        """Check state change behaivor when in 'Green' state"""
        light = TrafficLight()
        light.state = "Green"
        light.change_state()
        self.assertEqual(light.get_current_state(), "Yellow")

    def test_traffic_light_change_state_from_yellow(self):
        """Check state change behaivor when in 'Yellow' State."""
        light = TrafficLight()
        light.state = "Yellow"
        light.change_state()
        self.assertEqual(light.get_current_state(), "Red")


class TestWhiteBoxUserAuthentication(unittest.TestCase):
    """White-box unittest class - #24 UserAuthentication."""

    # Test cases 24 = "UserAuthentication"
    def test_user_authentication_initial_state(self):
        """Check if user Authentication initializes in 'Logged Out' state."""
        auth = UserAuthentication()
        self.assertEqual(auth.state, "Logged Out")

    def test_user_authentication_login_when_logged_out(self):
        """Check login behaivor when in 'Logged Out'state."""
        auth = UserAuthentication()
        self.assertEqual(auth.login(), "Login successful")
        self.assertEqual(auth.login(), "Invalid operation in current state")

    def test_user_authentication_login_when_logged_in(self):
        """Check login behavior when in 'Logged In' state."""
        auth = UserAuthentication()
        auth.state = "Logged In"
        self.assertEqual(auth.login(), "Invalid operation in current state")
        self.assertEqual(auth.state, "Logged In")

    def test_user_authentication_logout_when_logged_in(self):
        """Check logout behavior when in 'Logged In" state."""
        auth = UserAuthentication()
        auth.state = "Logged In"
        self.assertEqual(auth.logout(), "Logout successful")
        self.assertEqual(auth.state, "Logged Out")

    def test_user_authentication_logout_when_logged_out(self):
        """Check logout behavior when in 'Logged Out' state."""
        auth = UserAuthentication()
        self.assertEqual(auth.logout(), "Invalid operation in current state")
        self.assertEqual(auth.state, "Logged Out")


class TestWhiteBoxDocumentEditingSystem(unittest.TestCase):
    """White-box unittest class - #25 DocumentEditingSystem."""

    # Test cases 25 = "DocumentEditingSystem"
    def test_document_editing_system_initial_state(self):
        """Check if document editing system initializes in 'Editing'state."""
        document = DocumentEditingSystem()
        self.assertEqual(document.state, "Editing")

    def test_document_editing_system_save_when_editing(self):
        """Check save_Document behavior when in 'Editing' state."""
        document = DocumentEditingSystem()
        self.assertEqual(document.save_document(), "Document saved successfully")
        self.assertEqual(document.state, "Saved")

    def test_document_editing_system_save_when_saved(self):
        """Check save_document behavior when in 'Saved' state."""
        document = DocumentEditingSystem()
        document.state = "Saved"
        self.assertEqual(document.save_document(), "Invalid operation in current state")
        self.assertEqual(document.state, "Saved")

    def test_document_editing_system_edit_when_saved(self):
        """Check edit_document behavior when in  'Saved' state."""
        document = DocumentEditingSystem()
        document.state = "Saved"
        self.assertEqual(document.edit_document(), "Editing resumed")
        self.assertEqual(document.state, "Editing")

    def test_document_editing_system_edit_when_editing(self):
        """Check edit_document behavior when in 'Editing' state."""
        document = DocumentEditingSystem()
        self.assertEqual(document.edit_document(), "Invalid operation in current state")
        self.assertEqual(document.state, "Editing")


# pylint: disable=too-many-lines
class TestWhiteBoxElevatorSystem(unittest.TestCase):
    """White-box unittest class - #26 ElevatorSystem."""

    # Test cases 26 = "ElevatorSystem"
    def test_elevator_initial_state(self):
        """Check if elevator system initializes in 'Idle' state."""
        elevator = ElevatorSystem()
        self.assertEqual(elevator.state, "Idle")

    def test_elevator_system_move_up_when_idle(self):
        """Check move_up behavior when in 'Idle' state."""
        elevator = ElevatorSystem()
        self.assertEqual(elevator.move_up(), "Elevator moving up")
        self.assertEqual(elevator.state, "Moving Up")

    def test_elevator_system_move_down_when_idle(self):
        """Check move_down behavior when in 'Idle' state."""
        elevator = ElevatorSystem()
        self.assertEqual(elevator.move_down(), "Elevator moving down")
        self.assertEqual(elevator.state, "Moving Down")

    def test_elevator_system_stop_when_movin_up(self):
        """Check stop behavior when in 'Moving Up' state."""
        elevator = ElevatorSystem()
        elevator.state = "Moving Up"
        self.assertEqual(elevator.stop(), "Elevator stopped")
        self.assertEqual(elevator.state, "Idle")

    def test_elevator_system_stop_when_moving_down(self):
        """Check stop behavior when in 'Moving Down' state."""
        elevator = ElevatorSystem()
        elevator.state = "Moving Down"
        self.assertEqual(elevator.stop(), "Elevator stopped")
        self.assertEqual(elevator.state, "Idle")

    def test_elevator_system_stop_when_idle(self):
        """Check stop behavior when in 'Idle' state."""
        elevator = ElevatorSystem()
        self.assertEqual(elevator.stop(), "Invalid operation in current state")
        self.assertEqual(elevator.state, "Idle")

    def test_elevator_system_move_up_when_moving(self):
        """Check move_up behavior when already moving."""
        elevator = ElevatorSystem()
        elevator.state = "Moving Up"
        self.assertEqual(elevator.move_up(), "Invalid operation in current state")
        elevator.state = "Moving Down"
        self.assertEqual(elevator.move_up(), "Invalid operation in current state")


# pylint: disable=too-few-public-methods
class TestWhiteBoxBankAccount(unittest.TestCase):
    """White-box unittest class - #27 BankAccount."""

    # Test cases 27 = "BankAccount"
    def test_bank_account_initialization(self):
        """Check if bank account initializes with correct values."""
        account = BankAccount("12345", 1000)
        self.assertEqual(account.account_number, "12345")
        self.assertEqual(account.balance, 1000)

    def test_bank_account_view_account(self):
        """Check view_Account output using mock."""
        account = BankAccount("67890", 500)
        with mock.patch("sys.stdout", new=io.StringIO()) as fake_stdout:
            account.view_account()
            self.assertEqual(
                fake_stdout.getvalue().strip(), "The account 67890 has a balance of 500"
            )


class TestWhiteBoxBankingSystem(unittest.TestCase):
    """White-box unittest class - #28 BankingSystem."""

    # Test cases 28 = "BankingSystem"
    def setUp(self):
        """Setup BankingSystem instance for each test case."""
        self.banking_system = BankingSystem()
        self.mock_account = mock.patch(
            "src.white_box.BankAccount", return_value=mock.Mock(balance=1000)
        ).start()

    def tearDown(self):
        """Clean up after each test."""
        mock.patch.stopall()

    def test_banking_system_authenticate_success(self):
        """Check sucessful authentication"""
        with mock.patch("sys.stdout", new=io.StringIO()) as fake_stdout:
            result = self.banking_system.authenticate("user123", "pass123")
            self.assertTrue(result)
            self.assertIn("user123", self.banking_system.logged_in_users)
            self.assertIn(
                "User user123 authenticated successfully", fake_stdout.getvalue()
            )

    def test_banking_system_authenticate_already_logged_in(self):
        """Check authentication when user is already logged in"""
        self.banking_system.logged_in_users.add("user123")
        with mock.patch("sys.stdout", new=io.StringIO()) as fake_stdout:
            result = self.banking_system.authenticate("user123", "pass123")
            self.assertFalse(result)
            self.assertIn("User already logged in", fake_stdout.getvalue())

    def test_banking_system_authenticate_failure(self):
        """Check failed authentication"""
        with mock.patch("sys.stdout", new=io.StringIO()) as fake_stdout:
            result = self.banking_system.authenticate("wrong_user", "wrong_pass")
            self.assertFalse(result)
            self.assertNotIn("wrong_user", self.banking_system.logged_in_users)
            self.assertIn("Authentication failed", fake_stdout.getvalue())

    def test_banking_system_transfer_money_sender_not_authenticated(self):
        """Check money transfer when sender is not authenticated"""
        with mock.patch("sys.stdout", new=io.StringIO()) as fake_stdout:
            result = self.banking_system.transfer_money(
                "user123", "user456", 100, "regular"
            )
            self.assertFalse(result)
            self.assertIn("Sender not authenticated", fake_stdout.getvalue())

    def test_banking_system_transfer_money_invalid_type(self):
        """Check money transfer with invalid transaction type."""
        self.banking_system.logged_in_users.add("user123")
        with mock.patch("sys.stdout", new=io.StringIO()) as fake_stdout:
            result = self.banking_system.transfer_money(
                "user123", "user456", 100, "invalid"
            )
            self.assertFalse(result)
            self.assertIn("Invalid transaction type", fake_stdout.getvalue())

    def test_banking_system_transfer_money_insufficient_funds(self):
        """Check money transfer with insufficient funds."""
        self.banking_system.logged_in_users.add("user123")
        self.mock_account.return_value.balance = 50  # Set low balance
        with mock.patch("sys.stdout", new=io.StringIO()) as fake_stdout:
            result = self.banking_system.transfer_money(
                "user123", "user456", 100, "regular"
            )
            self.assertFalse(result)
            self.assertIn("Insufficient funds", fake_stdout.getvalue())

    def test_banking_system_transfer_money_success(self):
        """Check successful money transfer with different transaction types."""
        self.banking_system.logged_in_users.add("user123")
        with mock.patch("sys.stdout", new=io.StringIO()) as fake_stdout:
            result = self.banking_system.transfer_money(
                "user123", "user456", 100, "regular"
            )
            self.assertTrue(result)
            self.assertIn(
                "Money transfer of $100 (regular transfer)", fake_stdout.getvalue()
            )


class TestWhiteBoxProduct(unittest.TestCase):
    """White-box unittest class - #29 Product."""

    # Test cases 29 = "Product"
    def test_product_initialization(self):
        """Check if product initializes with correct values."""
        product = Product("Laptop", 1000)
        self.assertEqual(product.name, "Laptop")
        self.assertEqual(product.price, 1000)

    def test_product_view_product(self):
        """Check view_product output and return value."""
        product = Product("Phone", 500)
        with mock.patch("sys.stdout", new=io.StringIO()) as fake_stdout:
            return_value = product.view_product()
            self.assertEqual(
                fake_stdout.getvalue(), "The product Phone has a price of 500\n"
            )
            self.assertEqual(return_value, "The product Phone has a price of 500")


class TestWhiteBoxShoppingCart(unittest.TestCase):
    """White-box unittest class - #30 ShoppingCart."""

    # Test cases 30 = "ShoppingCart"
    def setUp(self):
        """Set up test environment before each test"""
        self.cart = ShoppingCart()
        self.product1 = Product("Laptop", 1000)
        self.product2 = Product("Phone", 50)

    def test_shopping_cart_initialization(self):
        """Check if shopping cart initializes with empty items list"""
        self.assertEqual(self.cart.items, [])

    def test_shopping_cart_add_new_product(self):
        """Check adding a new product to the cart"""
        self.cart.add_product(self.product1)
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0]["product"], self.product1)
        self.assertEqual(self.cart.items[0]["quantity"], 1)

    def test_shopping_cart_add_existing_prodcut(self):
        """Check adding more of an existing product"""
        self.cart.add_product(self.product1)
        self.cart.add_product(self.product1, 2)
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0]["quantity"], 3)

    def test_shopping_cart_remove_product_completely(self):
        """Check removing a product completely"""
        self.cart.add_product(self.product1, 2)
        self.cart.remove_product(self.product1, 2)
        self.assertEqual(len(self.cart.items), 0)

    def test_shopping_cart_remove_product_partially(self):
        """Check removing some quantity of a product."""
        self.cart.add_product(self.product1, 3)
        self.cart.remove_product(self.product1, 1)
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0]["quantity"], 2)

    def test_shopping_cart_view_cart(self):
        """Check view_cart output"""
        self.cart.add_product(self.product1, 2)
        self.cart.add_product(self.product2, 1)
        with mock.patch("sys.stdout", new=io.StringIO()) as fake_stdout:
            self.cart.view_cart()
            output = fake_stdout.getvalue()
            self.assertIn("2 x Laptop - $2000", output)
            self.assertIn("1 x Phone - $50", output)

    def test_shopping_cart_checkout(self):
        """Check checkout calculation and output."""
        self.cart.add_product(self.product1, 1)
        self.cart.add_product(self.product2, 2)
        with mock.patch("sys.stdout", new=io.StringIO()) as fake_stdout:
            self.cart.checkout()
            output = fake_stdout.getvalue()
            self.assertIn("Total: $1100", output)
            self.assertIn("Checkout completed", output)
