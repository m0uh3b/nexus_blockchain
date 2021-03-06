#
# API URLs
#
"""API URLs"""

from django.urls import path, include, re_path
from rest_framework import routers
from blockchain import api_views

# pylint: disable=C0103
router = routers.DefaultRouter()
router.register(
    r'get-raw-transaction',
    api_views.GetRawTransaction,
    base_name='raw_tx'
)
router.register(
    r'proof-of-nexus', api_views.ProofOfNexusAPI,
    base_name='proof_of_nexus'
)

app_name = 'api'
urlpatterns = [
    path('', include(router.urls)),
    path(
        'genesis',
        api_views.GenesisBlockAPI.as_view({
            'get': 'list',
            'post': 'create'
        }),
        name='genesis'
    ),
    re_path(
        r'block/(?P<height>[0-9a-fA-F]{,64})',
        api_views.GetBlockAPI.as_view({
            'get': 'list'
        }),
        name='block'
    ),
    re_path(
        r'transaction/(?P<_tx>[0-9a-fA-F]{,64})',
        api_views.TransactionAPI.as_view({
            'get': 'list'
        }),
        name='transaction'
    ),
    re_path(
        r'address/(?P<address>0x[0-9a-fA-F]{,64})',
        api_views.AddressAPI.as_view({
            'get': 'list'
        }),
        name='address'
    ),
    re_path(
        r'last-blocks',
        api_views.LastFiveBlocks.as_view({
            'get': 'list'
        }),
        name='last_blocks'
    ),
    re_path(
        r'mempool',
        api_views.MemPool.as_view({
            'get': 'list'
        }),
        name='mempool'
    )
]
