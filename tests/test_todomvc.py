from selene import browser, have, be, by


def test_complete_todo():
    browser.open('/')

    browser.element('[data-testid=text-input]').type('asd').press_enter()
    browser.element('[data-testid=text-input]').type('bcd').press_enter()
    browser.element('[data-testid=text-input]').type('ced').press_enter()
    browser.all('[data-testid=todo-item-label]').should(have.size(3))

    assert len(browser.driver.find_elements(*by.css('[data-testid=todo-item-label]')))==3