from django.urls import path
from .views import *



urlpatterns = [
    path('accessories_short/', ShortAccessListView.as_view(), name='short_a-list'),
    path('accessories_detail/<int:pk>/', AccessoriesDetailView.as_view(), name='access-detail'),
    path('accessories_create/', AccessCreateView.as_view(), name='access-create'),

    path('accessories_createSecond/', AccessSecondCreateView.as_view(), name='accesssecond-create'),

    path('accessories_createThord/', AccessThordCreateView.as_view(), name='accesstord-create'),

    path('similar_access/', AccessSimilarListView.as_view(), name='similar_access-list'),
    path('brand_access/', BrandAccessView.as_view(), name='brand-create'),
    path('category_access/', CategoryAccessView.as_view(), name='category-create'),

]
