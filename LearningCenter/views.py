#from django.http import HttpResponse
from django.shortcuts import render
from .models import Center, Disciplines, Courses, Teachers, Types, Levels, Themes
from django.shortcuts import get_object_or_404

def index(request):
    #return HttpResponse("Головна сторінка сайту навчального центру.")
    center = get_object_or_404(Center, id=1)
    centerName = center.name

    list = {'centerName':centerName,}
    #return render(request, 'center.html', list)
    return render(request, 'index.html', list)

def center(request):
    center = get_object_or_404(Center, id=1)
    centerName = center.name
    centerAddress = center.address
    centerTel = center.phone
    centerEmail = center.eMail

    list = {'centerName':centerName,'centerAddress':centerAddress,
            'centerTel':centerTel,'centerEmail':centerEmail}
    return render(request, 'center.html', list)

def disciplines(request):
    #import pdb;
    #pdb.set_trace()
    center = get_object_or_404(Center, id=1)
    centerName = center.name
    discList = Disciplines.objects.all()
    context = {
        'centerName':centerName,
        'discList': discList,
    }
    return render(request, 'disciplines.html', context)

def courses(request):
    center = get_object_or_404(Center, id=1)
    centerName = center.name
    courList = Courses.objects.all()
    context = {
        'centerName':centerName,
        'courList': courList,
    }
    return render(request, 'courses.html', context)

def teachers(request):
    center = get_object_or_404(Center, id=1)
    centerName = center.name
    teachList = Teachers.objects.all()
    context = {
        'centerName':centerName,
        'teachList': teachList,
    }
    return render(request, 'teachers.html', context)

def discipline(request, disc_id):
    center = get_object_or_404(Center, id=1)
    centerName = center.name
    disc = get_object_or_404(Disciplines, id=disc_id)
    context = {
        'centerName':centerName,
        'disc':disc,
    }
    return render(request, 'discipline.html', context)

def coursesDisc(request, disc_id):
    center = get_object_or_404(Center, id=1)
    centerName = center.name
    disc = get_object_or_404(Disciplines, id=disc_id)
    courList = disc.courses_set.all()
    context = {
        'centerName':centerName,
        'disc':disc,
        'courList':courList,
    }
    return render(request, 'coursesDisc.html', context)

def course(request, cour_id):
    center = get_object_or_404(Center, id=1)
    centerName = center.name
    cour = get_object_or_404(Courses, id=cour_id)
    disc_id = cour.disciplineId.id
    disc = get_object_or_404(Disciplines, id=disc_id)
    type_id = cour.typeId.id
    type = get_object_or_404(Types, id=type_id)
    level_id = cour.levelId.id
    level = get_object_or_404(Levels, id=level_id)
    teacher_id = cour.teacherId.id
    teacher = get_object_or_404(Teachers,id=teacher_id)
    amount = cour.amount
    pages = cour.pages
    complexity = cour.complexity
    description = cour.description

    # import pdb;
    # pdb.set_trace()

    context = {
        'centerName':centerName,
        'cour':cour,
        'disc':disc,
        'type':type,
        'level':level,
        'teacher':teacher,
        'amount':amount,
        'pages':pages,
        'complexity':complexity,
        'description':description
    }
    return render(request, 'course.html', context)

def teacher(request, teach_id):
    center = get_object_or_404(Center, id=1)
    centerName = center.name
    teach = get_object_or_404(Teachers, id=teach_id)

    context = {
        'centerName':centerName,
        'teach':teach,
    }
    return render(request, 'teacher.html', context)

def courThemes(request, cour_id):
    center = get_object_or_404(Center, id=1)
    centerName = center.name
    cour = get_object_or_404(Courses, id=cour_id)
    themList = cour.themes_set.all()

    context = {
        'centerName':centerName,
        'cour':cour,
        'themList':themList,
    }
    return render(request, 'courThemes.html', context)

def theme(request, theme_id):
    center = get_object_or_404(Center, id=1)
    centerName = center.name
    them = get_object_or_404(Themes, id=theme_id)
    course_id = them.courseId.id
    cour = get_object_or_404(Courses, id=course_id)
    notEmptyDescr = (them.description.strip() != '')
    context = {
        'centerName':centerName,
        'cour':cour,
        'them':them,
        'notEmptyDescr':notEmptyDescr
    }
    return render(request, 'theme.html', context)
