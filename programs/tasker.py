import re

course_id_stem = re.compile(r"/courses/(\d+)")
course_id_number = re.compile(r"^(\d+)$")


def is_course_id(u):
    print('coursing', u)
    print(course_id_stem.findall(u))
    if not u:
        print(f'course is {u}')
        return [u]
    else:
        course_id = course_id_stem.findall(u) + course_id_number.findall(u)
        print(f'course is {course_id}')
        return course_id


def get_course(question):
    courses = []
    answer = input(f'{question} ->')
    if is_course_id(answer):
        courses.append(answer)
    return courses


def create_new_blueprint():
    print('Creating new blueprint')
    course = get_course('What is the id of the NEW blueprint course?')
    error = False
    return error


def use_blueprint():
    print('Using an existing blueprint')
    course = get_course('What is the id of the blueprint course?')
    error = False
    return error


def associate_courses():
    print('Associating courses to blueprint')
    error = True
    return error


def survey():
    program = []
    answer = input('Do you want to create a NEW blueprint course? [Y/N]')
    if answer.lower() != 'n':
        program = [create_new_blueprint]
        answer = input('Do you want to associate this blueprint course with other courses? [Y/N]')
        if answer.lower() != 'n':
            program.append(associate_courses)
    else:
        answer = input(
            'Do you want to associate some courses with an existing blueprint course? [Y/N]')
        if answer.lower() != 'n':
            program = [use_blueprint, associate_courses]
    return program


program = survey()
print(program)

# result = list(map(lambda x: x(), program))

for function in program:
    error = function()
    if not error:
        print("result no error")
    else:
        print(f"error in {function.__name__}")
        exit()
