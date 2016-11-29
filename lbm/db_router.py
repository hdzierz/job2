class LBMDBRouter(object):
    """
    A router to control lbm db operations
    """
    def db_for_read(self, model, **hints):
        "Point all operations on lbm models to 'db_lbm'"
        from django.conf import settings
        if not 'db_lbm' in settings.DATABASES:
            return None
        if model._meta.app_label == 'lbm':
            return 'db_lbm'
        return None

    def db_for_write(self, model, **hints):
        "Point all operations on lbm models to 'db_lbm'"
        from django.conf import settings
        if not 'db_lbm' in settings.DATABASES:
            return None
        if model._meta.app_label == 'lbm':
            return 'db_lbm'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        "Allow any relation if a model in lbm is involved"
        from django.conf import settings
        if not 'db_lbm' in settings.DATABASES:
            return None
        if obj1._meta.app_label == 'lbm' or obj2._meta.app_label == 'lbm':
            return True
        return None

    def allow_syncdb(self, db, model):
        "Make sure the lbm app only appears on the 'lbm' db"
        from django.conf import settings
        if not 'db_lbm' in settings.DATABASES:
            return None
        if db == 'db_lbm':
            return model._meta.app_label == 'lbm'
        elif model._meta.app_label == 'lbm':
            return False
        return None
