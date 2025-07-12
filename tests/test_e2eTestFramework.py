
# pytest -m smoke   // Tagging
#pytest -n 10 //pytest-xdist plugin you need to run in parallel

# pytest -n 2 -m smoke --browser_name firefox --html=reports/report.html


import json
import os
import sys

import pytest

sys.path.append( os.path.dirname( os.path.dirname( os.path.abspath( __file__ ) ) ) )

from pageObjects.login import LoginPage

test_data_path = os.path.join('test_e2eTestFramework.json')
print(os.path.abspath('conftest.py'))
with open( test_data_path ) as f:
    test_data = json.load( f )
    test_list = test_data["data"]


@pytest.mark.smoke
@pytest.mark.parametrize( "test_list_item", test_list )
def test_e2e(browserInstance, test_list_item):
    driver = browserInstance
    loginPage = LoginPage( driver )
    print(loginPage.getTitle())
    shop_page = loginPage.login( test_list_item["userEmail"], test_list_item["userPassword"] )
    shop_page.add_product_to_cart( test_list_item["productName"] )
    print( shop_page.getTitle())
    checkout_confirmation = shop_page.goToCart()
    checkout_confirmation.checkout()
    checkout_confirmation.enter_delivery_address( "ind" )
    checkout_confirmation.validate_order()
