class CouralLegacyDBRouter(object):
    """
    A router to control coural_legacy db operations
    """
    def db_for_read(self, model, **hints):
        "Point all operations on coural_legacy models to 'db_coural_legacy'"
        from django.conf import settings
        if not 'db_coural_legacy' in settings.DATABASES:
            return None
        if model._meta.app_label == 'coural_legacy':
            return 'db_coural_legacy'
        return None

    def db_for_write(self, model, **hints):
        "Point all operations on coural_legacy models to 'db_coural_legacy'"
        from django.conf import settings
        if not 'db_coural_legacy' in settings.DATABASES:
            return None
        if model._meta.app_label == 'coural_legacy':
            return 'db_coural_legacy'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        "Allow any relation if a model in coural_legacy is involved"
        from django.conf import settings
        if not 'db_coural_legacy' in settings.DATABASES:
            return None
        if obj1._meta.app_label == 'coural_legacy' or obj2._meta.app_label == 'coural_legacy':
            return True
        return None

    def allow_syncdb(self, db, model):
        "Make sure the coural_legacy app only appears on the 'coural_legacy' db"
        from django.conf import settings
        if not 'db_coural_legacy' in settings.DATABASES:
            return None
        if db == 'db_coural_legacy':
            return model._meta.app_label == 'coural_legacy'
        elif model._meta.app_label == 'coural_legacy':
            return False
        return None
