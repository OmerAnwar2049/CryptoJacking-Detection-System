class Process:
  def __init__(self, p):
    self.process = p
    self.history = []
    self.history.append(p['cpu_usage'])

  def usage_update(self,p):
    self.history.append(p)
    
