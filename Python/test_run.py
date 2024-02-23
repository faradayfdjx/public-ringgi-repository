from LoginPage import test_ver_title, test_ver_elem, test_do_login, test_check_login, test_click_product, test_invalid_uname

importarray = [test_ver_title,
               test_ver_elem,
               test_do_login,
               test_check_login,
               test_click_product,
               test_invalid_uname]

def run_test_suite():
    # Run test A
    result_A = importarray[0].run_test()  # Example function that executes test A
    outcome_A = "Passed" if result_A else "Failed"

    # Run test B
    result_B = test_ver_elem.run_test()  # Example function that executes test B
    outcome_B = "Passed" if result_B else "Failed"

    # Run test C
    result_C = test_do_login.run_test()  # Example function that executes test C
    outcome_C = "Passed" if result_C else "Failed"

    # Run test D
    result_D = test_check_login.run_test()  # Example function that executes test C
    outcome_D = "Passed" if result_D else "Failed"

    # Run test D
    result_E = test_click_product.run_test()  # Example function that executes test C
    outcome_E = "Passed" if result_E else "Failed"

    # Run test D
    result_F = test_invalid_uname.run_test()  # Example function that executes test C
    outcome_F = "Passed" if result_F else "Failed"

    return {
        "Test A": outcome_A,
        "Test B": outcome_B,
        "Test C": outcome_C,
        "Test D": outcome_D,
        "Test E": outcome_E,
        "Test F": outcome_F
    }

if __name__ == "__main__":
    test_suite_results = run_test_suite()

    print("Test Suite Report:")
    for test_name, test_result in test_suite_results.items():
        print(f"{test_name}: {test_result}")
