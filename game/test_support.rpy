testsuite global:
    before testcase:
        $ _test.transition_timeout = 0.05
        $ _test.timeout = 8.0
        if not screen "main_menu":
            if eval main_menu:
                run ShowMenu("main_menu")
            else:
                run MainMenu(confirm=False)
    teardown:
        exit
