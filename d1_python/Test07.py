def shui(xinzi):
    jisuan = int(xinzi) * 0.75
    jiaoshui = int(xinzi) - jisuan
    # print("税前薪资是：" + str(xinzi) + " 缴税" + str(jiaoshui) + " 税后薪资是：" + str(jisuan))
    # print("税前薪资是：%s，缴税：%s，税后薪资是：%s" % (xinzi, jiaoshui, jisuan))
    print(f"税前薪资是：{xinzi:<012.2f}元，缴税：{jiaoshui:<012.2f}元，税后薪资是：{jisuan:<012.2f}元")


# xinzi = input("请输入薪资：")
yg1 = 100
yg2 = 1000
yg3 = 10000
shui(yg1)
shui(yg2)
shui(yg3)
