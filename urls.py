from datetime import date
from views import Index, About, Contacts, Courses, StudyPrograms, CoursesList, CreateCourse, CreateCategory, CategoryList, CopyCourse


# front controller
def secret_front(request):
    request['date'] = date.today()


def other_front(request):
    request['key'] = 'key'


fronts = [secret_front, other_front]

routes = {
    '/': Index(),
    '/about/': About(),
    '/contacts/': Contacts(),
    '/courses/': Courses(),
    '/study_programs/': StudyPrograms(),
    '/courses-list/': CoursesList(),
    '/create-course/': CreateCourse(),
    '/create-category/': CreateCategory(),
    '/category-list/': CategoryList(),
    '/copy-course/': CopyCourse()
}
