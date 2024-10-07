
# Форма регистрации
registration_name_input = "//input[@name='name']"# Поле ввода имени пользователя
registration_email_input = "(//input[@name='name'])[2]"# Поле ввода почты пользователя
registration_password_input = "//input[@name='Пароль']"# Поле ввода пароля пользователя
registration_button = "//button[contains(text(),'Зарегистрироваться')]"# Кнопка Отправки данных в форме регистрации
registration_password_error = ".input__error.text_type_main-default"# Ошибка неверного пароля

# Кнопки входа на сайт
login_button_on_mane_page = "//button[contains(text(),'Войти в аккаунт')]"# Кнопка перехода к форме авторизации на главной странице
login_header_button = "//p[contains(text(),'Личный Кабинет')]"# Кнопка "Личный Кабинет" в хедере
login_button_in_registration = ".//a[text()='Войти']"# Кнопка входа в форме регистрации
login_button_in_forgot_password = ".//a[@class='Auth_link__1fOlj']"# Кнопка входа в форме восстановления пароля

# Форма входа на сайт
login_email_input = ".//input[@name='name']"# Поле ввода  почты
login_password_input = ".//input[@name='Пароль']" # Поле ввода пароля
login_button = "//button[contains(text(),'Войти')]"# Кнопка войти

# Личный кабинет
personal_account_button = "//*[@id='root']/div/header/nav/a"# Кнопка перехода в ЛК
logout_button = "//button[contains(text(),'Выход')]"# Кнопка выхода из аккаунта

# Главная страница
bread_button = "//span[contains(text(),'Булки')]/parent::div" # Кнопка раздела "Булки" в конструкторе
source_button = "//span[contains(text(),'Соусы')]/parent::div" # Кнопка раздела "Соусы" в конструкторе
topping_button = "//span[contains(text(),'Начинки')]/parent::div" # Кнопка раздела "Начинки" в конструкторе

current_element = "//div[contains(@class,'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect')]" # Класс нажатого раздела

# Прочие эл-ты
element_on_main_page = ".text.text_type_main-large.mb-5.mt-10"# Заголовок на главной странице
login_heading = "//h2[contains(text(),'Вход')]"# Заголовок на странице логина
logo_button = "svg[xmlns='http://www.w3.org/2000/svg'][width='290']"# Логотип
constructor_button = ".AppHeader_header__link__3D_hX" # Кнопка конструктора в хедере
text_in_profile = "//p[@class='Account_text__fZAIn text text_type_main-default']" # Текст в профиле
