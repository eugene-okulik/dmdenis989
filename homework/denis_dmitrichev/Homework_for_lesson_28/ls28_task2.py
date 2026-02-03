from playwright.sync_api import sync_playwright, Page


def fill_form(page: Page):
    page.goto('https://demoqa.com/automation-practice-form')
    name_field = page.get_by_placeholder('First Name')
    name_field.fill('Denis')
    last_name_field = page.get_by_placeholder('Last Name')
    last_name_field.fill('Dmitrichev')
    email_field = page.get_by_placeholder('name@example.com')
    email_field.fill('dmdenis899@gmail.com')
    male_gender_radiobutton = page.locator('[for="gender-radio-1"]')
    male_gender_radiobutton.click()
    phone_number_field = page.get_by_placeholder('Mobile Number')
    phone_number_field.fill('0123745670')
    date_of_birth_field = page.locator('//*[@id="dateOfBirthInput"]')
    date_of_birth_field.click()
    date_of_birth_field.press('Control+a')
    date_of_birth_field.fill('05 Aug 1989')
    date_of_birth_field.press('Enter')
    subject_field = page.locator('[id="subjectsContainer"]')
    subject_field.click()
    subject_field.press_sequentially('English', delay=100)
    subject_field.press('Enter')
    sports_check = page.locator('[for="hobbies-checkbox-1"]')
    sports_check.click()
    address_field = page.get_by_placeholder("Current Address")
    address_field.fill('Kazan, Abbasov Street 8')
    state_field = page.locator('#react-select-3-input')
    state_field.fill('NCR')
    state_field.press('Enter')
    city_field = page.locator('#react-select-4-input')
    city_field.fill('Noida')
    city_field.press('Enter')
    submit_button = page.locator('[id="submit"]')
    submit_button.click()


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        fill_form(page)
        browser.close()


if __name__ == "__main__":
    main()
