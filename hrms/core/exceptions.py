"""
"""


class HRMSTemplateSetMissed(Exception):
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return self.value
    
    def __repr__(self):
        return self.value


class HRMSTemplateMissingTemplateSet(Exception):
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return self.value
    
    def __repr__(self):
        return self.value


class HRMSTemplateFOPConfigMissed(Exception):
    def __init__(self, v):
        self.v=v
    
    def __str__(self):
        return self.v
    
    def __repr__(self):
        return self.v


class HRMSTemplateXSLTFileMissed(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value


class NoSerializationPatternFound(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class OpenInterestAccountMissing(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class IncompleteInvoice(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class InvoiceAlreadyRegistered(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class UserIsNoHumanResource(Exception):
    def __init__(self, value):
        self.value = value
        self.view = "/hrms/reporting/user_is_not_human_resource"

    def __str__(self):
        return repr(self.value)


class ReportingPeriodDoneDeleteNotPossible(Exception):
    def __init__(self, value):
        self.value = value
        self.view = "/hrms/reporting_period_done_delete_not_possible"

    def __str__(self):
        return repr(self.value)


class ReportingPeriodNotFound(Exception):
    def __init__(self, value):
        self.value = value
        self.view = "/hrms/views/reporting_period_missing"

    def __str__(self):
        return repr(self.value)