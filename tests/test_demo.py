def test_demo(browser):
    browser.get("https://plugins.jenkins.io/shiningpanda/")
    assert browser.find_element_by_xpath(
        "//div[@id='grid-box']/div/h1").text == "ShiningPanda"
