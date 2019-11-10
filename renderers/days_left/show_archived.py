from .show import Show

class ShowArchived(Show):
  @property
  def header(self):
    return _('After "%(name)s" have passed:') % { 'name': self.event.name }
