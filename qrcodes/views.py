import os
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import View
from qrcode import QRCode
import qrcode

p_id = []
n=1
class gcmmfqrgene(View):
    template_name = 'gcmmf_qr_generator.html'

    def get(self, request):
        data_elements = request.GET.getlist('data_elements[]')
        data_list = ','.join(data_elements)
        qr_code = QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L)
        for element in data_list:
            qr_code.add_data(element)
        if not p_id:
            p_id[0] = n
        else:
            p_id.append(n+1) 
            n += 1
        qr_code.make(fit=True)
        qr_code_image = qr_code.make_image()
        # Make sure that the `qr_codes` directory exists
        if not os.path.exists('qr_codes'):
            os.makedirs('qr_codes')
        qr_code_image.save('qr_codes/qr_code.png')

        return render(request, self.template_name)

class GenerateQRCodeView(View):
    template_name = 'generate_qr_code.html'

    def get(self, request):
        return render(request, self.template_name)
#list = map(datalis.split(','))