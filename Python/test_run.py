from LoginPage import test_ver_title, test_ver_elem, test_do_login, test_check_login, test_click_product, test_invalid_uname, test_invalid_passw, test_fail_login, test_empty_uname, test_empty_passw

importarray = [
    test_ver_title,
    test_ver_elem,
    test_do_login,
    test_check_login,
    test_click_product,
    test_invalid_uname,
    test_invalid_passw, 
    test_fail_login, 
    test_empty_uname, 
    test_empty_passw
]

result = [0] * len(importarray)
outcome = []

def run_test_suite():
    for test_func in importarray:
        result = test_func.run_test()
        outcome.append("Passed" if result else "Failed")

    return {f"Test {i + 1}": outcome[i] for i in range(len(outcome))}

if __name__ == "__main__":
    test_suite_results = run_test_suite()

    print("Test Suite Report:")
    for test_name, test_result in test_suite_results.items():
        print(f"{test_name}: {test_result}")
