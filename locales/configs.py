import gettext

locales = {
  'ru': gettext.translation('hypeometer', 'locales/', ['ru'], fallback=True),
  'en': gettext.translation('hypeometer', 'locales/', ['en'], fallback=True)
}

def set_locale(locale = 'en'):
  locales[locale].install(names='ngettext')
