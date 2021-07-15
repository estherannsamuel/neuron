class BallAndStick:
    def __init__(self, gid):
        self._gid = gid
        self.soma = h.Section(name="soma", cell=self)
        self.dend = h.Section(name="dend", cell=self)
        self.all = [self.soma, self.dend]
        self.dend.connect(self.soma())
        self.soma.L = self.soma.diam = 12.6157
        self.dend.L = 200
        self.dend.diam = 1
    def __repr__(self):
        return "BallAndStick [{}]".format(self._gid)
        
my_cell = BallAndStick(0)

import matplotlib.pyplot as plt

# h.PlotShape(False).plot(plt)
ps = h.PlotShape(False)
ps.plot(plt)
ps.show(0)

