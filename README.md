# Todorite

![Todorite Logo](custom/logo.png) <!-- Если есть логотип -->

## Backend Todorite

Backend написан на **Koa**, работает под управлением **PM2**.  

## Технологии

- **Backend:** Node.js, Koa, PM2
- **Сервер:** Nginx
- **SSL:** Let's Encrypt (для HTTPS)

## Функциональность

- Регистрация и аутентификация пользователей
- Проверка токена
- Поддержка REST API
- Валидация по Joi
- MVC разделение

## Структура

backend/
├── src/
│   ├── controllers/
│   │   ├── authController.js
│   │   └── userController.js
│   ├── middleware/
│   │   ├── authChecker.js
│   │   ├── errorHandler.js
│   │   └── logger.js
│   ├── routes/
│   │   ├── authRoutes.js
│   │   ├── chatRoutes.js
│   │   ├── infoRoutes.js
│   │   └── userRoutes.js
│   ├── services/
│   │   ├── authServices.js
│   │   ├── chatServices.js
│   │   ├── infoServices.js
│   │   └── userServices.js
│   ├── utils/
│   │   ├── config.js
│   │   └── knex.js
├── index.js
package.json
package-lock.json
