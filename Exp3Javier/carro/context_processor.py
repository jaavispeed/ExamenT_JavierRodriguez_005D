def importe_total_carro(request):
    total=0
    if request.user.is_authenticated and request.session.__contains__('carro'):
        for key, value in request.session["carro"].items():
            total=total+int(value["precio"])

    return{"importe_total_carro":total}