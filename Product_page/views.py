from django.views.generic import ListView, TemplateView, DetailView
from Product_page.models import Product, ProductCategory

from django.views.generic import ListView

class ProductPage(ListView):
    model = Product
    template_name = "product_page/product_page.html"
    context_object_name = "products"
    ordering = ['-rating']
    paginate_by = 6

    def get_queryset(self):
        queryset = Product.objects.filter(is_active=True)

        selected_categories = self.request.GET.getlist("category")

        if selected_categories:
            queryset = queryset.filter(
                category__url_title__in=selected_categories
            )

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["categories"] = ProductCategory.objects.filter(
            is_active=True,
            is_delete=False
        )

        context["selected_categories"] = self.request.GET.getlist("category")

        query_params = self.request.GET.copy()
        query_params.pop("page", None)

        context["query_params"] = query_params.urlencode()

        return context



class ProductDetailView(DetailView):
    model = Product
    template_name = "product_page/product_detail_page.html"
    context_object_name = "product"


