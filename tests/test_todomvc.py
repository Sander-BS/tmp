from selene import browser, have, be


def test_complete_todo():

    browser.config.base_url = 'https://todomvc.com/examples/react/dist/'
    browser.open('/')

    browser.element('[data-testid=text-input]').type('asd').press_enter()
    browser.element('[data-testid=text-input]').type('bcd').press_enter()
    browser.element('[data-testid=text-input]').type('ced').press_enter()
    browser.all('[data-testid=todo-item-label]').should(have.size(3))

    browser.quit()
