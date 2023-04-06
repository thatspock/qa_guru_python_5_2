from selene import browser
from selene import be, have


def test_google_selene_search(open_browser):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_google_wrong_results(open_browser):
    searching_text = 'config.driver.maximize_window()'
    browser.element('[name="q"]').should(be.blank).type('selene maximize window').press_enter()

    try:
        assert browser.element('[id="search"]').should(have.text(searching_text))

    except:
        print('\nNo results')
