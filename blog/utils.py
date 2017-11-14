from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponseRedirect

class ObjectCreateMixin:
    form_class = None
    template_name = ''

    def get_object(self, year, month, slug):
        return get_object_or_404(
            self.model,
            pub_date__year=year,
            pub_date__month=month,
            slug=slug)

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class()})

    def post(self, request):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            new_object = bound_form.save()
            return redirect(new_object)
        else:
            return render(request, self.template_name, {'form': bound_form})

class ObjectUpdateMixin:
    form_class = None
    model = None
    template_name = ''

    def get_object(self, year, month, slug):
        return get_object_or_404(self.model, pub_date__year=year, pub_date__month=month, slug=slug)

    def get(self, request, year, month, slug):
        post = self.get_object(year, month, slug)
        context = {'form': self.form_class(instance=post), 'post': post, }
        return render(request, self.template_name, context)

    def post(self, request, year, month, slug):
        post = self.get_object(year, month, slug)
        bound_form = self.form_class(request.POST, instance=post)
        if bound_form.is_valid():
            new_post = bound_form.save()
            return redirect(new_post)
        else:
            context = {'form': bound_form, 'post': post, }
            return render(request, self.template_name, context)

class ObjectDeleteMixin:
    model = None
    success_url = ''
    template_name = ''

    def get(self, request, year, month, slug):
        post = get_object_or_404(self.model, pub_date__year=year, pub_date__month=month, slug__iexact=slug)
        return render(request, self.template_name, {'post': post})

    def post(self, request, year, month, slug):
        post = get_object_or_404(self.model, pub_date__year=year, pub_date__month=month, slug__iexact=slug)
        post.delete()
        return HttpResponseRedirect(self.success_url)
