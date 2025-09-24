25 XPath локаторів
//input[@id='signinEmail'] – поле Email у модальному Sign In
//input[@id='signinPassword'] – поле Password у модальному Sign In
//button[@class='btn btn-primary' and text()='Login'] – кнопка Login
//button[@class='btn btn-link' and text()='Cancel'] – кнопка Cancel у модальному Sign In
//button[@class='hero-descriptor_btn btn btn-primary'] – кнопка Sign In на головній сторінці
//button[@class='btn btn-outline-white header_signin'] – кнопка Sign In у шапці сайту
//button[@class='btn btn-outline-white header_signup'] – кнопка Sign Up у шапці сайту
//h5[@class='modal-title' and text()='Sign In'] – заголовок модального вікна
//h5[@class='page-title' and text()='Garage'] – заголовок після входу
//button[@class='btn btn-primary' and text()='Add car'] – кнопка Add car
//select[@id='addCarBrand'] – селект вибору бренду
//select[@id='addCarModel'] – селект вибору моделі
//input[@id='addCarMileage'] – поле Mileage
//div[@class='modal-title h4' and text()='Add a car'] – заголовок модального додавання авто
//button[@class='btn btn-primary' and text()='Add'] – кнопка Add у модалці
//button[@class='btn btn-secondary' and text()='Cancel'] – кнопка Cancel у модалці
//div[@class='car__name'] – назва авто в гаражі
//div[@class='car__name']/../div[@class='car__actions']/button[@title='Edit'] – кнопка Edit для авто
//div[@class='car__name']/../div[@class='car__actions']/button[@title='Remove'] – кнопка Remove для авто
//nav//a[@href='/panel/garage'] – пункт меню Garage
//nav//a[@href='/panel/expenses'] – пункт меню Fuel expenses
//nav//a[@href='/panel/instructions'] – пункт меню Instructions
//nav//a[@href='/panel/profile'] – пункт меню Profile
//button[@class='btn btn-link btn-logout'] – кнопка Logout
//div[contains(@class,'toast-message')] – повідомлення (успіх/помилка)

25 CSS локаторів
input#signinEmail – поле Email
input#signinPassword – поле Password
button.btn.btn-primary – кнопка Login
button.btn.btn-link – кнопка Cancel у модальному Sign In
button.hero-descriptor_btn.btn.btn-primary – кнопка Sign In на головній
button.header_signin – кнопка Sign In у хедері
button.header_signup – кнопка Sign Up у хедері
h5.modal-title – заголовок Sign In
h5.page-title – заголовок Garage
button.btn.btn-primary – кнопка Add car
select#addCarBrand – селект бренду
select#addCarModel – селект моделі
input#addCarMileage – пробіг
div.modal-title.h4 – заголовок Add a car
div.modal-footer button.btn-primary – кнопка Add
div.modal-footer button.btn-secondary – кнопка Cancel
div.car__name – назва авто
div.car__actions button[title='Edit'] – кнопка Edit
div.car__actions button[title='Remove'] – кнопка Remove
nav a[href='/panel/garage'] – меню Garage
nav a[href='/panel/expenses'] – меню Fuel expenses
nav a[href='/panel/instructions'] – меню Instructions
nav a[href='/panel/profile'] – меню Profile
button.btn-logout – кнопка Logout
div.toast-message – повідомлення