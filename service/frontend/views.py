# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from cStringIO import StringIO
import qrcode
import short_url
from django.http import HttpResponse
from django.shortcuts import render
from service.frontend.models import QRToken


def generate_qrcode(data, size=11):
    qr = qrcode.QRCode(version=1, box_size=size, border=1, error_correction=qrcode.constants.ERROR_CORRECT_L)
    qr.add_data(data)
    qr.make(fit=True)
    im = qr.make_image()

    return im


def q(request, uid):
    uid = short_url.decode_url(uid)
    url = 'http://' + request.get_host() + '/api/users/%s/invite/' % uid
    img = generate_qrcode(url)
    buf = StringIO()
    img.save(buf)

    stream = buf.getvalue()
    return HttpResponse(stream, content_type="image/jpeg")


def qs(request, key):
    # 生成扫码登陆图片
    url = 'http://' + request.get_host() + '/api/scan/%s/binding_code/' % key
    img = generate_qrcode(url)
    buf = StringIO()
    img.save(buf)

    stream = buf.getvalue()
    return HttpResponse(stream, content_type="image/jpeg")


def scan_login(request):
    # 生成token
    token = QRToken()
    token.save()

    # 生成url
    url = 'http://' + request.get_host() + '/check/%s/' % token.key
    url1 = 'http://' + request.get_host() + '/qs/%s/' % token.key
    success = 'http://' + request.get_host() + '/success/'

    return render(request, 'scanlogin.html', {'url': url, 'url1': url1, 'success': success})


def check(request, key):
    # 查看扫码状态
    try:
        obj = QRToken.objects.filter(key=key).get()
        if obj.owner is None:
            return HttpResponse('505')
        return HttpResponse('201')
    except QRToken.DoesNotExist:
        raise Exception()


def success(request):
    # 登陆成功返回的页面
    return render(request, 'success.html')
