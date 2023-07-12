import calendar

def CalendarioTexto():
    calendarioTexto = calendar.TextCalendar(calendar.SUNDAY)
    txtCalendario = calendarioTexto.formatmonth(2023, 6)
    print(txtCalendario)
CalendarioTexto()

def CalendarioHtml():
    calendarioHtml = calendar.HTMLCalendar(calendar.SUNDAY)
    htmlCalendario = calendarioHtml.formatmonth(2023, 6)
    print(htmlCalendario)
CalendarioHtml()

def ImprimeMes():
    for mes in calendar.month_name:
        print(mes)

    for dia in calendar.day_name:
        print(dia)
ImprimeMes()