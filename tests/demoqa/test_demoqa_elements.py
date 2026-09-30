from selene import browser, have, be


def test_elements_text_box():

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