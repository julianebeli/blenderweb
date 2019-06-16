import __init__
from api.requestor2 import API
import re

course_id_stem = re.compile(r"/courses/(\d+)")
course_id_number = re.compile(r"^(\d+)$")


def get_course_id(u):
    print('coursing', u)
    print(course_id_stem.findall(u))
    if not u:
        return [u]
    else:
        return course_id_stem.findall(u) + course_id_number.findall(u)
