from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from matching_app.models import Recruitment

RECRUITMENT_TIMELINE_PAGE_SIZE = 10


@login_required
@require_http_methods(["GET"])
def recruitment_timeline(request: HttpRequest) -> HttpResponse:
    recruitments = Recruitment.objects.select_related("user").all()
    pagenator = Paginator(recruitments, RECRUITMENT_TIMELINE_PAGE_SIZE)
    page_number = request.GET.get("page", default=1)
    page_obj = pagenator.page(page_number)

    return render(
        request,
        "recruitment_timeline.html",
        {"page_obj": page_obj},
    )
