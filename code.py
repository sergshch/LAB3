import lab1
import lab2
from fpdf import FPDF

#Данные из ЛР1, ЛР2
call_cost = 93.22
sms_cost = 21.00
internet_cost = 8048.10
cost = call_cost + sms_cost + internet_cost
value_added_tax = cost * 0.2

#Создание и подготовка файла и шрифтов
pdf = FPDF()
pdf.add_page()
pdf.add_font('Arial', '', 'C:\\Windows\\Fonts\\arial.ttf', True)
pdf.add_font('Arial Bold', '', 'C:\\Windows\\Fonts\\arialbd.ttf', True)

# Верхняя таблица
pdf.set_font('Arial', '', 10)
pdf.cell(85, 15, '', 1, 0)
pdf.cell(-85)
pdf.cell(85, 5, 'ООО БАНК ОРАНЖЕВЫЙ', 0, 0)
pdf.cell(20, 20, '', 1, 0)
pdf.cell(-20)
pdf.cell(20, 5, 'БИК', 1, 0)
pdf.cell(75, 20, '', 1, 0)
pdf.cell(-75)
pdf.cell(75, 5, '044030904', 0, 1)
pdf.cell(85)
pdf.cell(20, 5, 'Сч. №', 0, 0)
pdf.cell(75, 5, '3010180000000000904', 0, 1)
pdf.cell(0, 5, '', 0, 1)
pdf.cell(85, 5, 'Банк получателя', 1, 1)
pdf.cell(85, 25, '', 1, 0)
pdf.cell(-85)
pdf.cell(42, 5, 'ИНН   '+'156499494947', 1, 0)
pdf.cell(43, 5, 'КПП   '+'131644997569', 1, 0)
pdf.cell(20, 25, '', 1, 0)
pdf.cell(-20)
pdf.cell(20, 5, 'Сч. №', 0, 0)
pdf.cell(75, 25, '', 1, 0)
pdf.cell(-75)
pdf.cell(75, 5, '4514516487962645489', 0, 1)
pdf.cell(85, 5, 'Сергеев Сергей Сергеевич', 0, 1)
pdf.cell(0, 10, '', 0, 1)
pdf.cell(85, 5, 'Получатель', 1, 1)

# Заголовок счета
pdf.set_font('Arial Bold', '', 14)
pdf.cell(180, 10, 'Счет №2020 от 13 мая 2020 г.', 0, 1, 'C')
pdf.cell(180, 0, '', 1, 1)

# Счет
pdf.set_font('Arial', '', 10)
pdf.cell(0, 5, '', 0, 1)
pdf.cell(30, 5, 'Поставщик', 0, 0)
pdf.set_font('Arial Bold', '', 10)
pdf.cell(140, 5, 'Иванов Иван Иванович, г. Грозный', 0, 1)
pdf.set_font('Arial', '', 10)
pdf.cell(30, 5, '(Исполнитель):', 0, 1)
pdf.cell(0, 5, '', 0, 1)
pdf.cell(30, 5, 'Покупатель', 0, 0)
pdf.set_font('Arial Bold', '', 10)
pdf.cell(140, 5, 'Сергеев Сергей Сергеевич, г. Санкт-Петербург', 0, 1)
pdf.set_font('Arial', '', 10)
pdf.cell(30, 5, '(Заказчик):', 0, 1)
pdf.cell(0, 5, '', 0, 1)
pdf.cell(30, 5, 'Основание', 0, 0)
pdf.set_font('Arial Bold', '', 10)
pdf.cell(140, 5, 'Основной договор', 0, 1)
pdf.cell(0, 5, '', 0, 1)

# Нижняя таблица
pdf.cell(10, 10, '№', 1, 0, 'C')
pdf.cell(90, 10, 'Наименование работ, услуг', 1, 0, 'C')
pdf.cell(20, 10, 'Кол-во', 1, 0, 'C')
pdf.cell(15, 10, 'Ед.', 1, 0, 'C')
pdf.cell(20, 10, 'Цена', 1, 0, 'C')
pdf.cell(25, 10, 'Сумма', 1, 1, 'C')

pdf.set_font('Arial', '', 10)
pdf.cell(10, 5, '1', 1, 0, 'C')
pdf.cell(90, 5, 'Звонки', 1, 0)
pdf.cell(20, 5, '1', 1, 0, 'R')
pdf.cell(15, 5, '1', 1, 0, 'R')
pdf.cell(20, 5, "{:.2f}".format(call_cost), 1, 0, 'R')
pdf.cell(25, 5, "{:.2f}".format(call_cost), 1, 1, 'R')

pdf.cell(10, 5, '2', 1, 0, 'C')
pdf.cell(90, 5, 'СМС', 1, 0)
pdf.cell(20, 5, '1', 1, 0, 'R')
pdf.cell(15, 5, '1', 1, 0, 'R')
pdf.cell(20, 5, "{:.2f}".format(sms_cost), 1, 0, 'R')
pdf.cell(25, 5, "{:.2f}".format(sms_cost), 1, 1, 'R')

pdf.cell(10, 5, '3', 1, 0, 'C')
pdf.cell(90, 5, 'Интернет', 1, 0)
pdf.cell(20, 5, '1', 1, 0, 'R')
pdf.cell(15, 5, '1', 1, 0, 'R')
pdf.cell(20, 5, "{:.2f}".format(internet_cost), 1, 0, 'R')
pdf.cell(25, 5, "{:.2f}".format(internet_cost), 1, 1, 'R')

#Итог
pdf.cell(0, 5, '', 0, 1)
pdf.set_font('Arial Bold', '', 10)
pdf.cell(135)
pdf.cell(20, 5, 'Итого: ', 0, 0, 'R')
pdf.cell(25, 5, "{:.2f}".format(cost), 0, 1, 'R')

pdf.cell(135)
pdf.cell(20, 5, 'В том числе НДС: ', 0, 0, 'R')
pdf.cell(25, 5, "{:.2f}".format(value_added_tax), 0, 1, 'R')

pdf.cell(135)
pdf.cell(20, 5, 'Всего к оплате: ', 0, 0, 'R')
pdf.cell(25, 5, "{:.2f}".format(cost), 0, 1, 'R')

pdf.cell(0, 5, '', 0, 1)
pdf.set_font('Arial', '', 10)
pdf.cell(180, 5, 'Всего наименований '+'3, на сумму 8 162.32 руб.', 0, 1)

pdf.set_font('Arial Bold', '', 10)
pdf.cell(180, 5, 'Восемь тысяч сто шестьдесят два рубля 32 копейки', 0, 1)

pdf.set_font('Arial', '', 10)
pdf.cell(180, 5, '', 0, 1)
pdf.cell(180, 5, 'Внимание!', 0, 1)
pdf.cell(180, 5, 'Оплата данного счета означает согласие с условиями поставки товара.', 0, 1)
pdf.cell(180, 5, 'Уведомление об оплате обязательно, в противном случае не гарантируется наличие товара на складе.', 0, 1)
pdf.cell(180, 5, 'Товар отпускается по факту прихода денег на р/с Поставщика, самовывозом, при наличии доверенности и', 0, 1)
pdf.cell(180, 5, 'паспорта.', 0, 1)
pdf.cell(180, 5, '', 0, 1)
pdf.cell(180, 5, '', 0, 1)
pdf.cell(180, 0, '', 1, 1)

pdf.cell(180, 10, '', 0, 1)
pdf.set_font('Arial Bold', '', 10)
pdf.cell(170, 5, 'Руководитель   _____________________________________         Бухгалтер   _________________________', 0, 1)

pdf.output('Счет на оплату.pdf')
