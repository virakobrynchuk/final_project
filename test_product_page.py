from pages.product_page import ProductPage
link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"


def test_shellcoders_handbook(browser):
    page = ProductPage(browser, link)
    page.open()
    page.pass_test()
