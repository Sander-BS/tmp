from selene import browser, have, be


def open_elements():
    browser.open('/elements')


def test_elements_text_box():
    open_elements()

    browser.element('[href="/text-box"]').click()
    browser.element('#userName').type("SanderBS")
    browser.element('#userEmail').type("cfylth001@gmail.com")
    browser.element('#currentAddress').type("Kaz, Astana")
    browser.element('#permanentAddress').type("Earth")
    browser.element('#submit').click()

    browser.element('#output #name').should(have.text('Name:SanderBS'))
    browser.element('#output #email').should(have.text('Email:cfylth001@gmail.com'))
    browser.element('#output #currentAddress').should(have.text('Current Address :Kaz, Astana'))
    browser.element('#output #permanentAddress').should(have.text('Permananet Address :Earth'))


def test_elements_check_box():
    open_elements()

    browser.element('[href="/checkbox"]').click()

    plus_button = '.rc-tree-switcher'
    browser.all('[role="treeitem"]').element_by(have.text("Home")).element(plus_button).click()
    browser.all('[role="treeitem"]').element_by(have.text("Desktop")).element(plus_button).click()
    browser.all('[role="treeitem"]').element_by(have.text("Documents")).element(plus_button).click()
    browser.all('[role="treeitem"]').element_by(have.text("WorkSpace")).element(plus_button).click()


    browser.element('[aria-label="Select Notes"]').click()
    browser.element('[aria-label="Select React"]').click()
    browser.element('[aria-label="Select Veu"]').click()

    browser.element('#result').should(have.text('notes'))
    browser.element('#result').should(have.text('veu'))
    browser.element('#result').should(have.text('react'))


def test_elements_radio_button():
    open_elements()

    browser.element('[href="/radio-button"]').click()
    browser.element('#impressiveRadio').click()
    browser.element('[class="text-success"]').should(have.text('Impressive'))


def test_elements_web_tables():
    open_elements()

    browser.element('[href="/webtables"]').click()

    initial_rows_count = len(browser.all('tbody tr'))

    browser.element('#addNewRecordButton').click()
    browser.element('#firstName').type("Alexandr")
    browser.element('#lastName').type("Babenko")
    browser.element('#userEmail').type("cfylth001@gmail.com")
    browser.element('#age').type("31")
    browser.element('#salary').type('7500')
    browser.element('#department').type('todo')
    browser.element('#submit').click()

    browser.all('tbody tr').should(have.size(initial_rows_count + 1))

    new_row = browser.all('tbody tr').element_by(have.text("cfylth001@gmail.com"))
    new_row.all('td').should(have.exact_texts(
        'Alexandr',
        'Babenko',
        '31',
        'cfylth001@gmail.com',
        '7500',
        'todo',
        ''
    ))