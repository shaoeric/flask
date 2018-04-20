from flask import jsonify

class HttpCode(object):
    ok = 200
    unautherror = 401
    paramserror = 400
    servererror = 500

def restful_result(code, message, data):
    return jsonify({"code": code, "message": message, "data": data or {}})

def success(message='', data=None):
    return restful_result(code=HttpCode.ok, message=message, data=data)

def unauthorerror(message=""):
    return restful_result(code=HttpCode.unautherror, message=message, data=None)

def paramserror(message=''):
    return restful_result(code=HttpCode.paramserror, message=message, data=None)

def servererror(message=''):
    return restful_result(code=HttpCode.servererror, message=message or '服务器内部错误', data=None)
