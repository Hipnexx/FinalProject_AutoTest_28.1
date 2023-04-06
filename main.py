import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome("C:/Users/User/Desktop/Selenium/chromedriver.exe")
    # Задаем размер открываемого окна браузера
    pytest.driver.set_window_size(1920, 1080)
    # Переходим на страницу авторизации
    pytest.driver.get('https://b2c.passport.rt.ru')
    yield
    pytest.driver.quit()

#Тест с негативным сценарием (неправильный телефон и пароль) авторизации с помощью номера телефона
def test_phone_authorization_with_negative_scenario():
    # Нажимаем на кнопку авторизации по телефону
    pytest.driver.implicitly_wait(5)
    pytest.driver.find_element(By.ID, 't-btn-tab-phone').click()
    pytest.driver.implicitly_wait(5)
    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-tab.rt-tab--small.rt-tab--active').text == "Телефон"
    # Вводим невалидный номер телефона
    pytest.driver.find_element(By.ID, 'username').send_keys('1234567890')
    # Вводим невалидный пароль
    pytest.driver.find_element(By.ID, 'password').send_keys('12345678')
    # Нажимаем кнопку войти
    pytest.driver.find_element(By.ID, 'kc-login').click()
    pytest.driver.implicitly_wait(2)
    # Проверяем, что нам отказано в доступе и выведенно сообщение о том что логин и пароль не верны
    assert pytest.driver.find_element(By.ID, 'form-error-message').text == "Неверный логин или пароль"

#Тест с позитивным сценарием (правильный телефон и пароль) авторизации с помощью номера телефона
def test_phone_authorization_with_positive_scenario():
    # Нажимаем на кнопку авторизации по телефону
    pytest.driver.implicitly_wait(5)
    pytest.driver.find_element(By.ID, 't-btn-tab-phone').click()
    pytest.driver.implicitly_wait(5)
    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-tab.rt-tab--small.rt-tab--active').text == "Телефон"
    # Вводим невалидный номер телефона
    pytest.driver.find_element(By.ID, 'username').send_keys('89198564769')
    # Вводим невалидный пароль
    pytest.driver.find_element(By.ID, 'password').send_keys('Ahuy6alpjwq')
    # Нажимаем кнопку войти
    pytest.driver.find_element(By.ID, 'kc-login').click()
    pytest.driver.implicitly_wait(2)
    # Проверяем, что мы успешно вошли в аккаунт, т.к. у нас на странице есть кнопка выхода из него
    assert pytest.driver.find_element(By.ID, 'logout-btn').text == "Выйти"

# Тест с негативным сценарием (неправильная почта и пароль) авторизации с помощью почты
def test_mail_authorization_with_negative_scenario():
    # Нажимаем на кнопку авторизации по почте
    pytest.driver.implicitly_wait(5)
    pytest.driver.find_element(By.ID, 't-btn-tab-mail').click()
    pytest.driver.implicitly_wait(5)
    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-tab.rt-tab--small.rt-tab--active').text == "Почта"
    # Вводим невалидный номер телефона
    pytest.driver.find_element(By.ID, 'username').send_keys('1234567890@mail.ru')
    # Вводим невалидный пароль
    pytest.driver.find_element(By.ID, 'password').send_keys('12345678')
    # Нажимаем кнопку войти
    pytest.driver.find_element(By.ID, 'kc-login').click()
    pytest.driver.implicitly_wait(2)
    # Проверяем, что нам отказано в доступе и выведенно сообщение о том что логин и пароль не верны
    assert pytest.driver.find_element(By.ID, 'form-error-message').text == "Неверный логин или пароль"

# Тест с позитивным сценарием (правильная почта и пароль) авторизации с помощью почты
def test_mail_authorization_with_positive_scenario():
    # Нажимаем на кнопку авторизации по почте
    pytest.driver.implicitly_wait(5)
    pytest.driver.find_element(By.ID, 't-btn-tab-mail').click()
    pytest.driver.implicitly_wait(5)
    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-tab.rt-tab--small.rt-tab--active').text == "Почта"
    # Вводим невалидный номер телефона
    pytest.driver.find_element(By.ID, 'username').send_keys('knitter.come-0c@icloud.com')
    # Вводим невалидный пароль
    pytest.driver.find_element(By.ID, 'password').send_keys('Ahuy6alpjwq')
    # Нажимаем кнопку войти
    pytest.driver.find_element(By.ID, 'kc-login').click()
    pytest.driver.implicitly_wait(2)
    # Проверяем, что мы успешно вошли в аккаунт, т.к. у нас на странице есть кнопка выхода из него
    assert pytest.driver.find_element(By.ID, 'logout-btn').text == "Выйти"

# Тест с негативным сценарием (неправильный логин и пароль) авторизации с помощью логина
def test_login_authorization_with_negative_scenario():
    # Нажимаем на кнопку авторизации по логину
    pytest.driver.implicitly_wait(5)
    pytest.driver.find_element(By.ID, 't-btn-tab-login').click()
    pytest.driver.implicitly_wait(5)
    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-tab.rt-tab--small.rt-tab--active').text == "Логин"
    # Вводим невалидный номер телефона
    pytest.driver.find_element(By.ID, 'username').send_keys('ивановиваниванович')
    # Вводим невалидный пароль
    pytest.driver.find_element(By.ID, 'password').send_keys('12345678')
    # Нажимаем кнопку войти
    pytest.driver.find_element(By.ID, 'kc-login').click()
    pytest.driver.implicitly_wait(2)
    # Проверяем, что нам отказано в доступе и выведенно сообщение о том что логин и пароль не верны
    assert pytest.driver.find_element(By.ID, 'form-error-message').text == "Неверный логин или пароль"

# Тест с позитивным сценарием (правильный логин и пароль) авторизации с помощью логина
def test_login_authorization_with_positive_scenario():
    # Нажимаем на кнопку авторизации по логину
    pytest.driver.implicitly_wait(5)
    pytest.driver.find_element(By.ID, 't-btn-tab-login').click()
    pytest.driver.implicitly_wait(5)
    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-tab.rt-tab--small.rt-tab--active').text == "Логин"
    # Вводим невалидный номер телефона
    pytest.driver.find_element(By.ID, 'username').send_keys('Тестимя Тестфамилия')
    # Вводим невалидный пароль
    pytest.driver.find_element(By.ID, 'password').send_keys('Ahuy6alpjwq')
    # Нажимаем кнопку войти
    pytest.driver.find_element(By.ID, 'kc-login').click()
    pytest.driver.implicitly_wait(2)
    # Проверяем, что мы успешно вошли в аккаунт, т.к. у нас на странице есть кнопка выхода из него
    assert pytest.driver.find_element(By.ID, 'logout-btn').text == "Выйти"

# Тест с негативным сценарием (неправильный логин и пароль) авторизации с помощью лицевого счета
def test_personal_account_authorization_with_negative_scenario():
    # Нажимаем на кнопку авторизации по лицевому счету
    pytest.driver.implicitly_wait(5)
    pytest.driver.find_element(By.ID, 't-btn-tab-ls').click()
    pytest.driver.implicitly_wait(5)
    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-tab.rt-tab--small.rt-tab--active').text == "Лицевой счёт"
    # Вводим невалидный номер телефона
    pytest.driver.find_element(By.ID, 'username').send_keys('121232132321')
    # Вводим невалидный пароль
    pytest.driver.find_element(By.ID, 'password').send_keys('12345678')
    # Нажимаем кнопку войти
    pytest.driver.find_element(By.ID, 'kc-login').click()
    pytest.driver.implicitly_wait(2)
    # Проверяем, что нам отказано в доступе и выведенно сообщение о том что логин и пароль не верны
    assert pytest.driver.find_element(By.ID, 'form-error-message').text == "Неверный логин или пароль"

# Тест с позитивным сценарием (правильный счет и пароль) авторизации с помощью лицевого счета
def test_personal_account_authorization_with_positive_scenario():
    # Нажимаем на кнопку авторизации по лицевому счету
    pytest.driver.implicitly_wait(5)
    pytest.driver.find_element(By.ID, 't-btn-tab-ls').click()
    pytest.driver.implicitly_wait(5)
    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-tab.rt-tab--small.rt-tab--active').text == "Лицевой счёт"
    # Вводим невалидный номер телефона
    pytest.driver.find_element(By.ID, 'username').send_keys('1670664309008')
    # Вводим невалидный пароль
    pytest.driver.find_element(By.ID, 'password').send_keys('Ahuy6alpjwq')
    # Нажимаем кнопку войти
    pytest.driver.find_element(By.ID, 'kc-login').click()
    pytest.driver.implicitly_wait(2)
    # Проверяем, что мы успешно вошли в аккаунт, т.к. у нас на странице есть кнопка выхода из него
    assert pytest.driver.find_element(By.ID, 'logout-btn').text == "Выйти"

# Тест с негативным сценарием восстановления пароля по номеру телефона
def test_password_recovery_phone_number_with_negative_scenario():
    # Нажимаем на кнопку забыл пароль
    pytest.driver.implicitly_wait(5)
    pytest.driver.find_element(By.ID, 'forgot_password').click()
    pytest.driver.implicitly_wait(5)
    #Проверяем что перешли на страницу восстановления
    assert pytest.driver.find_element(By.CLASS_NAME, 'card-container__title').text == "Восстановление пароля"
    # Нажимаем на кнопку Телефон
    pytest.driver.implicitly_wait(5)
    pytest.driver.find_element(By.ID, 't-btn-tab-phone').click()
    pytest.driver.implicitly_wait(5)
    # Проверяем что переключили вкладку для указания номера телефона
    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-tab rt-tab--small rt-tab--active').text == "Телефон"
    # Вводим валидный номер телефона
    pytest.driver.find_element(By.ID, 'username').send_keys('919234580669')
    # Нажимаем кнопку Продолжить
    pytest.driver.find_element(By.ID, 'reset').click()
    pytest.driver.implicitly_wait(2)
    assert pytest.driver.find_element(By.CLASS_NAME, 'form-error-message').text == "Неверный логин или текст с картинки"

# Тест с положительным сценарием регистрации
def test_registration_positiv_scenario():
    # Нажимаем на кнопку зарегистрироватся
    pytest.driver.implicitly_wait(5)
    pytest.driver.find_element(By.ID, 'kc-register').click()
    pytest.driver.implicitly_wait(5)
    #Проверяем что перешли на страницу регистрации
    assert pytest.driver.find_element(By.CLASS_NAME, 'card-container__title').text == "Регистрация"

    # Заполняем все поля для регистрации:
    pytest.driver.find_element(By.NAME, 'firstName').send_keys("Тестимя")
    pytest.driver.find_element(By.NAME, 'lastName').send_keys("Тестфамилия")
    pytest.driver.find_element(By.id, 'address').send_keys("knitter.come-0c@icloud.com") 
    pytest.driver.find_element(By.NAME, 'password').send_keys("Ahuy6alpjwq") 
    pytest.driver.find_element(By.NAME, 'password-confirm').send_keys("Ahuy6alpjwq") 
    # Нажимаем на кнопку зарегистрироваться
    pytest.driver.find_element(By.CLASS_NAME, 'register').click()
    pytest.driver.implicitly_wait(5)
    assert pytest.driver.find_element(By.CLASS_NAME, 'card-container__title').text == "Подтверждение email"

# Тест с негативным сценарием регистрации, невалидные имя(на латинице), невалидные почта или телефон(не в формате ...@email.ru и не +7ХХХХХХХХХХ)
#невалидный пароль (менее 8 символов)
def test_registration_negative_scenario():
    # Нажимаем на кнопку зарегистрироватся
    pytest.driver.implicitly_wait(5)
    pytest.driver.find_element(By.ID, 'kc-register').click()
    pytest.driver.implicitly_wait(5)
    #Проверяем что перешли на страницу регистрации
    assert pytest.driver.find_element(By.CLASS_NAME, 'card-container__title').text == "Регистрация"

    # Заполняем все поля для регистрации:
    pytest.driver.find_element(By.NAME, 'firstName').send_keys("asdsd") 
    pytest.driver.find_element(By.NAME, 'lastName').send_keys("sdasda") 
    # Проверяем что повилось сообщение о недопустимости ввода
    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-input-container__meta rt-input-container__meta--error').text == "Необходимо заполнить поле кириллицей. От 2 до 30 символов." 

    pytest.driver.find_element(By.id, 'address').send_keys("dfdsf") 
    # Проверяем что повилось сообщение о недопустимости ввода
    assert pytest.driver.find_element(By.CLASS_NAME,'rt-input-container__meta rt-input-container__meta--error').text == "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru" 
    pytest.driver.find_element(By.NAME, 'password').send_keys("Ahuy6alpjwq") 
    pytest.driver.find_element(By.NAME, 'password-confirm').send_keys("Ahuy6alpjwq") 
    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-input-container__meta rt-input-container__meta--error').text == "Длина пароля должна быть не менее 8 символов"
    # Нажимаем на кнопку зарегистрироваться
    pytest.driver.find_element(By.CLASS_NAME, 'register').click() 
    pytest.driver.implicitly_wait(5)
    #Убеждаемся что она не сработала и мы остались на той же странице
    assert pytest.driver.find_element(By.CLASS_NAME, 'card-container__title').text == "Регистрация"

# Тест с положительным сценарием входа по соцсети VK
def test_social_vk_login_positiv_scenario():
    # Нажимаем на кнопку зарегистрироватся
    pytest.driver.implicitly_wait(5)
    pytest.driver.find_element(By.ID, 'kc-register').click()
    pytest.driver.implicitly_wait(5)
    #Проверяем что перешли на страницу регистрации
    assert pytest.driver.find_element(By.CLASS_NAME, 'card-container__title').text == "Регистрация"
    # Заполняем все поля для регистрации:
    pytest.driver.find_element(By.id, 'oidc_vk').click()
    pytest.driver.implicitly_wait(5)
    # Проверяем что перешли на страницу входа по соцсети вконтакте
    assert pytest.driver.find_element(By.CLASS_NAME, 'box_msg_gray box_msg_padded').text == "Для продолжения вам необходимо войти ВКонтакте"
    pytest.driver.find_element(By.NAME, 'email').send_keys("knitter.come-0c@icloud.com")
    pytest.driver.find_element(By.NAME, 'pass').send_keys("Ahuy6alpjwq")
    # Нажимаем на кнопку войти
    pytest.driver.find_element(By.ID, 'install_allow').click()
    pytest.driver.implicitly_wait(5)
    # Проверяем, что мы успешно вошли в аккаунт, т.к. у нас на странице есть кнопка выхода из него
    assert pytest.driver.find_element(By.ID, 'logout-btn').text == "Выйти"

# Тест с положительным сценарием входа по соцсети Одноклассники
def test_social_ok_login_positiv_scenario():
    # Нажимаем на кнопку зарегистрироватся
    pytest.driver.implicitly_wait(5)
    pytest.driver.find_element(By.ID, 'kc-register').click()
    pytest.driver.implicitly_wait(5)
    #Проверяем что перешли на страницу регистрации
    assert pytest.driver.find_element(By.CLASS_NAME, 'card-container__title').text == "Регистрация"
    # Заполняем все поля для регистрации:
    pytest.driver.find_element(By.id, 'oidc_ok').click()
    pytest.driver.implicitly_wait(5)
    # Проверяем что перешли на страницу входа по соцсети Одноклассники
    assert pytest.driver.find_element(By.CLASS_NAME, 'ext-widget_h_tx').text == "Одноклассники"
    pytest.driver.find_element(By.ID, 'field_email').send_keys("knitter.come-0c@icloud.com")
    pytest.driver.find_element(By.ID, 'field_password').send_keys("Ahuy6alpjwq")
    # Нажимаем на кнопку войти
    pytest.driver.find_element(By.CLASS_NAME, 'button-pro __wide form-actions_yes').click()
    pytest.driver.implicitly_wait(5)
    # Проверяем, что мы успешно вошли в аккаунт, т.к. у нас на странице есть кнопка выхода из него
    assert pytest.driver.find_element(By.ID, 'logout-btn').text == "Выйти"

# Тест с положительным сценарием входа по соцсети Мой мир
def test_social_myworld_login_positiv_scenario():
    # Нажимаем на кнопку зарегистрироватся
    pytest.driver.implicitly_wait(5)
    pytest.driver.find_element(By.ID, 'kc-register').click()
    pytest.driver.implicitly_wait(5)
    #Проверяем что перешли на страницу регистрации
    assert pytest.driver.find_element(By.CLASS_NAME, 'card-container__title').text == "Регистрация"
    # Заполняем все поля для регистрации:
    pytest.driver.find_element(By.id, 'oidc_mail').click()
    pytest.driver.implicitly_wait(5)
    # Проверяем что перешли на страницу входа по соцсети Одноклассники
    assert pytest.driver.find_element(By.CLASS_NAME, 'header__logo').text == "Мой Мир@Mail.Ru"
    pytest.driver.find_element(By.ID, 'login').send_keys("knitter.come-0c")
    pytest.driver.find_element(By.ID, 'password').send_keys("Ahuy6alpjwq")
    # Нажимаем на кнопку войти и разрешить
    pytest.driver.find_element(By.CLASS_NAME, 'ui-button-main').click()
    pytest.driver.implicitly_wait(5)
    # Проверяем, что мы успешно вошли в аккаунт, т.к. у нас на странице есть кнопка выхода из него
    assert pytest.driver.find_element(By.ID, 'logout-btn').text == "Выйти"

# Тест с проверкой ссылки пользовательского соглашения в футере
def test_footer_use_agreement_link_positiv_scenario():
    # Нажимаем на кнопку зарегистрироватся
    pytest.driver.implicitly_wait(5)
    pytest.driver.find_element(By.ID, 'kc-register').click()
    pytest.driver.implicitly_wait(5)
    #Проверяем что перешли на страницу регистрации
    assert pytest.driver.find_element(By.CLASS_NAME, 'card-container__title').text == "Регистрация"
    #Кликаем по кнопке Пользовательским соглашением в футере
    buttonUserAgreement = pytest.driver.find_element(By.CLASS_NAME, 'rt-footer-left__item-accent').text == " Пользовательским соглашением "
    buttonUserAgreement.click()
    pytest.driver.implicitly_wait(5)
    # Проверяем что перешли на страницу с пользовательским соглашением
    assert pytest.driver.find_element(By.CLASS_NAME, 'offer-title').text == "Публичная оферта о заключении Пользовательского соглашения на использование Сервиса «Ростелеком ID» "



