from rest_framework.routers import DefaultRouter
from rest_framework_extensions.routers import NestedRouterMixin
from demo.views import AuthorViewSet, BookViewSet, EditionViewSet


class NestedDefaultRouter(NestedRouterMixin, DefaultRouter):
    pass

router = NestedDefaultRouter()

router.register('authors', AuthorViewSet)
authors_router = router.register('authors', AuthorViewSet)
authors_router.register('books', BookViewSet,
    base_name='author-books',
    parents_query_lookups=['author']).register('editions', EditionViewSet, base_name='author-book-edition',
                                               parents_query_lookups=['book_author', 'book'])

router.register('books', BookViewSet)
