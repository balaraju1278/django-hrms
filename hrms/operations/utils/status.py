from django.utils.translation import ugettext as _

CALL_STATUS = (
    ('P', _('Planned')),
    ('D', _('Delayed')),
    ('R', _('ToRecall')),
    ('F', _('Failed')),
    ('S', _('Success')),
)

DELIVER_NOTES_STATUS = (
    ('C', _('Ordered')),
    ('S', _('Sent')),
    ('R', _('Received')),
    ('L', _('Lost')),
)

PURCHASE_ORDER_STATUS = (
    ('O', _('Ordered')),
    ('D', _('Delayed')),
    ('I', _('Invoice Registered')),
    ('P', _('Invoice Payed')),
)

QUOTE_STATUS = (
    ('S', _('Success')),
    ('C', _('Quote Created')),
    ('Q', _('Quote Dent')),
    ('F', _('First Reminder Sent')),
    ('R', _('Second Reminder Sent')),
    ('D', _('Deleted')),
)

INVOICE_STATUS = (
    ('P', _('Payed')),
    ('C', _('Invoice Created')),
    ('I', _('Invoice Sent')),
    ('F', _('First Reminder Sent')),
    ('S', _('Second Reminder Sent')),
    ('U', _('Customer Cant Pay')),
    ('D', _('Deleted')),
)

