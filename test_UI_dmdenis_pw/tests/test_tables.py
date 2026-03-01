good1_name = "Customizable Desk"
good2_name = "Acoustic Bloc Screens"
good3_name = "[FURN_0096] Customizable Desk (Steel, White)"


def test_search_by_name(table):
    table.open_page()
    table.send_query_in_search_field(good1_name)
    table.click_search_button()
    table.check_found_good("750.00", good1_name)


def test_sort_by_name(table):
    table.open_page()
    table.sort_by_name(good1_name)
    table.check_good_name(good2_name)


def test_add_to_card(table):
    table.open_page()
    table.put_into_basket(good3_name)
