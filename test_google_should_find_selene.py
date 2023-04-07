from selene import browser, query
from selene import be, have


def test_google_selene_search(open_browser):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_google_wrong_results(open_browser):
    browser.element('[name="q"]').should(be.blank).type('fwjfjdsjfjsdkjfsdfl3939').press_enter()
    result_text = browser.element('[id="result-stats"]').get(query.text)

    browser.element('[id="result-stats"]').should(have.text('About 0 results'))
    print('\nNo results')
    print(f"You've got a message: {result_text}")

