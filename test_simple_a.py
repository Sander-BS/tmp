from selene import browser, have, be


def test_duckduckgo_search_positive():
    browser.open('https://duckduckgo.com')
    browser.element('[name="q"]').type('pytest selene').press_enter()
    browser.element('#r1-0').should(have.text('Selene'))


def test_duckduckgo_search_negative():
    browser.open('https://duckduckgo.com')
    random_query = '┤'
    browser.element('[name="q"]').type(random_query).press_enter()
    browser.element('#r1-0').should(be.not_.visible)