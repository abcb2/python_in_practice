# -*- coding:utf-8 -*-

from lib.supporter import (
    Trouble, NoSupporter, LimitSupporter, OddSupporter, SpecialSupporter
)

supporter_01 = NoSupporter("taro")
supporter_02 = LimitSupporter(name="jiro", limit=3)
supporter_03 = OddSupporter(name="saburo")
supporter_04 = SpecialSupporter(name="hanako", num=8)

supporter_01.set_next_supporter(supporter_02).set_next_supporter(supporter_03).set_next_supporter(supporter_04)

for i in range(0, 11):
    trouble = Trouble(i)
    # print(trouble)
    supporter_01.support(trouble)
