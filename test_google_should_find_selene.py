from selene import browser, query
from selene import be, have


def test_google_selene_search(open_browser):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_google_wrong_results(open_browser):
    browser.element('[name="q"]').should(be.blank).type('fwjfjdsjfjsdkjfsdfl3939').press_enter()
    result_text = browser.element('[id="result-stats"]').get(query.text)

    try:
        assert browser.element('[id="result-stats"]').should(have.text('About 0 results'))
        print(f"\nYou've got a message: {result_text}")

    except:
        print("\nSomething went wrong. Probably you've expected more than 0 results")
