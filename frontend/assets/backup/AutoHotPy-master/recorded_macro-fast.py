from AutoHotPy import AutoHotPy
from InterceptionWrapper import *
import time
def exitAutoHotKey(autohotpy,event):
    autohotpy.stop()
def recorded_macro(autohotpy, event):
    start = time.time()
    autohotpy.moveMouseToPosition(1680,807)
    autohotpy.sleep(0.0)
    autohotpy.RIGHT_SHIFT.down()
    autohotpy.sleep(2.60312557220459e-05)
    autohotpy.M.down()
    autohotpy.sleep(1.818530559539795e-05)
    autohotpy.RIGHT_SHIFT.up()
    autohotpy.sleep(3.636884689331055e-06)
    autohotpy.M.up()
    autohotpy.sleep(5.995454788208008e-05)
    autohotpy.Y.down()
    autohotpy.sleep(1.0668158531188965e-05)
    autohotpy.Y.up()
    autohotpy.sleep(8.129651546478272e-05)
    autohotpy.SPACE.down()
    autohotpy.sleep(1.5619683265686035e-05)
    autohotpy.SPACE.up()
    autohotpy.sleep(9.888982772827149e-06)
    autohotpy.N.down()
    autohotpy.sleep(1.1567139625549317e-05)
    autohotpy.N.up()
    autohotpy.sleep(6.49559497833252e-06)
    autohotpy.A.down()
    autohotpy.sleep(1.2889838218688966e-05)
    autohotpy.M.down()
    autohotpy.sleep(1.7061233520507813e-07)
    autohotpy.A.up()
    autohotpy.sleep(1.4650774002075196e-05)
    autohotpy.M.up()
    autohotpy.sleep(1.4352846145629883e-05)
    autohotpy.E.down()
    autohotpy.sleep(1.5276336669921875e-05)
    autohotpy.E.up()
    autohotpy.sleep(3.108501434326172e-06)
    autohotpy.SPACE.down()
    autohotpy.sleep(1.32645845413208e-05)
    autohotpy.SPACE.up()
    autohotpy.sleep(4.184865951538086e-05)
    autohotpy.I.down()
    autohotpy.sleep(1.1587953567504883e-05)
    autohotpy.I.up()
    autohotpy.sleep(1.409604549407959e-05)
    autohotpy.S.down()
    autohotpy.sleep(1.3340234756469727e-05)
    autohotpy.S.up()
    autohotpy.sleep(5.569195747375489e-06)
    autohotpy.SPACE.down()
    autohotpy.sleep(1.3287687301635743e-05)
    autohotpy.SPACE.up()
    autohotpy.sleep(7.497286796569825e-06)
    autohotpy.RIGHT_SHIFT.down()
    autohotpy.sleep(5.031015872955323e-05)
    autohotpy.RIGHT_SHIFT.down()
    autohotpy.sleep(3.1992197036743164e-06)
    autohotpy.RIGHT_SHIFT.down()
    autohotpy.sleep(4.609227180480957e-06)
    autohotpy.RIGHT_SHIFT.down()
    autohotpy.sleep(3.15091609954834e-06)
    autohotpy.RIGHT_SHIFT.down()
    autohotpy.sleep(1.0008811950683594e-07)
    autohotpy.R.down()
    autohotpy.sleep(1.231985092163086e-05)
    autohotpy.R.up()
    autohotpy.sleep(2.7777910232543945e-06)
    autohotpy.RIGHT_SHIFT.up()
    autohotpy.sleep(2.015564441680908e-05)
    autohotpy.U.down()
    autohotpy.sleep(1.0289502143859863e-05)
    autohotpy.U.up()
    autohotpy.sleep(9.053778648376465e-06)
    autohotpy.S.down()
    autohotpy.sleep(1.296062469482422e-05)
    autohotpy.S.up()
    autohotpy.sleep(7.249617576599121e-06)
    autohotpy.L.down()
    autohotpy.sleep(1.1693382263183594e-05)
    autohotpy.L.up()
    autohotpy.sleep(1.4264702796936035e-05)
    autohotpy.A.down()
    autohotpy.sleep(8.872818946838379e-06)
    autohotpy.A.up()
    autohotpy.sleep(1.0811948776245118e-05)
    autohotpy.N.down()
    autohotpy.sleep(1.0386919975280762e-05)
    autohotpy.N.up()
    autohotpy.sleep(7.617454528808594e-05)
    autohotpy.SPACE.down()
    autohotpy.sleep(1.2728309631347657e-05)
    autohotpy.SPACE.up()
    autohotpy.sleep(9.420967102050782e-06)
    autohotpy.RIGHT_SHIFT.down()
    autohotpy.sleep(9.666490554809571e-06)
    autohotpy.M.down()
    autohotpy.sleep(1.0744905471801758e-05)
    autohotpy.RIGHT_SHIFT.up()
    autohotpy.sleep(1.8702983856201174e-06)
    autohotpy.M.up()
    autohotpy.sleep(9.569096565246582e-06)
    autohotpy.A.down()
    autohotpy.sleep(1.106874942779541e-05)
    autohotpy.A.up()
    autohotpy.sleep(1.704065799713135e-05)
    autohotpy.G.down()
    autohotpy.sleep(1.1248779296875001e-05)
    autohotpy.G.up()
    autohotpy.sleep(1.3344621658325196e-05)
    autohotpy.A.down()
    autohotpy.sleep(8.705639839172363e-06)
    autohotpy.N.down()
    autohotpy.sleep(1.413416862487793e-06)
    autohotpy.A.up()
    autohotpy.sleep(8.808588981628418e-06)
    autohotpy.N.up()
    autohotpy.sleep(1.223444938659668e-06)
    autohotpy.A.down()
    autohotpy.sleep(1.0286092758178711e-05)
    autohotpy.A.up()
    end = time.time()
    print(end - start)
if __name__=="__main__":
    auto = AutoHotPy()
    auto.registerExit(auto.ESC,exitAutoHotKey)
    auto.registerForKeyDown(auto.F1,recorded_macro)
    auto.start()