import __init__
from api.requestor2 import API
import re

api = API('beta')

course_id_stem = re.compile(r"/courses/(\d+)")
course_id_number = re.compile(r"^(\d+)$")


def prepare_response(result, error, props):
    if error:
        result = [x['message'] for x in result[0]['errors']]
    else:
        result = dict(zip(props, map(lambda x: result[0][x], props)))

    return dict(result=result, error=error)


def get_course_id(u):
    print('coursing', u)
    print(course_id_stem.findall(u))
    if not u:
        return None
    else:
        return course_id_stem.findall(u) + course_id_number.findall(u)


def get_course_name(course_id):
    methodname = "get_single_course_courses"
    id = get_course_id(course_id)
    print('ID-------------------->', id)
    if id:
        api.add_method(**dict(methodname=methodname, id=id[0]))
        api.do()
        print(api.results)
        print(api.response_error)
        return prepare_response(api.results, api.response_error, ['id', 'name'])
    else:
        return(dict(result=['No course ID specified'], id='True'))
