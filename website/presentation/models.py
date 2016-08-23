from __future__ import unicode_literals, absolute_import

from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.utils.translation import ugettext_lazy as _


from config.settings import common


# Create your models here.
@python_2_unicode_compatible
class UserRequest(models.Model):
    action_time = models.DateTimeField(
        _('action time'),
        default=timezone.now,
        editable=False,
    )
    user = models.ForeignKey(
        common.AUTH_USER_MODEL,
        models.CASCADE,
        verbose_name=_('user'),
    )
    req_national_id = models.TextField(_('national id'), blank=False, null=False)
    resp_cheque = models.TextField(_('response_cheque'), blank=True, null=True)
    resp_loans = models.TextField(_('response_loans'), blank=True , null=True)

    def __str__(self):
        return self.req_national_id + str(self.user)

    class Meta:
        ordering = ['action_time']
