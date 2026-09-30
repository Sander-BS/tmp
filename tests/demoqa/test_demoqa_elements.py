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

    browser.element('[href = "/checkbox"]').click()

    plus_button = '[class="rc-tree-switcher rc-tree-switcher_close"]'
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