# -*- coding: utf-8 -*

from django.utils.translation import ugettext as _

PURPOSESADDRESSINCONTRACT = (
    ('D', _('Delivery Address')),
    ('B', _('Billing Address')),
    ('C', _('Contact Address')),
)

PURPOSESADDRESSINCUSTOMER = (
    ('P', _('Private')),
    ('B', _('Business')),
    ('MP', _('Mobile Private')),
    ('MB', _('Mobile Business')),
)

PURPOSESTEXTPARAGRAPHINDOCUMENTS = (
    ('BS', _('Before subject')),
    ('AS', _('After subject')),
    ('BT', _('Before total')),
    ('AT', _('After total')),
    ('BW', _('Before wishes')),
    ('AW', _('After wishes')),
    ('C1', _('Custom 1')),
    ('C2', _('Custom 2')),
    ('C3', _('Custom 3')),
    ('C4', _('Custom 4')),
)

PURPOSECALLINCUSTOMER = (
    ('FCA', _('First commercial call')),
    ('PCA', _('Planned commercial call')),
    ('AC', _('Assistance call')),
)

PURPOSEVISITINCUSTOMER = (
    ('FCV', _('First commercial visit')),
    ('SCV', _('Second commercial visit')),
    ('I', _('Installation')),
)