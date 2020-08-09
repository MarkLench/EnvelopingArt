from django.shortcuts import render, get_object_or_404

class get_objects:
    model = None
    template = None

    def get(self, request):
        Model = self.model
        obj = Model.objects.order_by('-Date_time_added')
        return render(request, self.template, context={Model.__name__.lower(): obj})

class get_object:
    model = None
    template = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, Slug=slug)
        return render(request, self.template, context={self.model.__name__.lower(): obj})
