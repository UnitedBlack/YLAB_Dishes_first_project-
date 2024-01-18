# YLAB_Dishes_first_project-
Проект на FastAPI с использованием PostgreSQL в качестве БД. В проекте следует реализовать REST API по работе с меню ресторана, все CRUD операции.

Написать проект на FastAPI с использованием PostgreSQL в качестве БД. В проекте следует реализовать REST API по работе с меню ресторана, все CRUD операции. Для проверки задания, к презентаций будет приложена Postman коллекция с тестами. Задание выполнено, если все тесты проходят успешно. 
Даны 3 сущности: Меню, Подменю, Блюдо.
Зависимости: 
●У меню есть подменю, которые к ней привязаны. 
●У подменю есть блюда. 
 
Условия: 
●Блюдо не может быть привязано напрямую к меню, минуя подменю. 
●Блюдо не может находиться в 2-х подменю одновременно. 
●Подменю не может находиться в 2-х меню одновременно. 
●Если удалить меню, должны удалиться все подменю и блюда этого меню. 
●Если удалить подменю, должны удалиться все блюда этого подменю. 
●Цены блюд выводить с округлением до 2 знаков после запятой. 
●Во время выдачи списка меню, для каждого меню добавлять кол-во подменю и блюд в этом меню. 
●Во время выдачи списка подменю, для каждого подменю добавлять кол-во блюд в этом подменю. 
●Во время запуска тестового сценария БД должна быть пуста.