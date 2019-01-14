from flask import jsonify


def make_resp(status_code, name, results):
    status_code = status_code.__dict__
    result = {
        'status': {
            'code': status_code['code'],
            'msg': status_code['msg'],
            'error_code': status_code['error_code']
        },
        name: results
    }
    return jsonify(result)