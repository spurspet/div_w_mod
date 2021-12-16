# 计算有余数的除法

a = int(input('请输入被除数： '))
b = int(input('请输入除数： '))
div = a // b
mod =  a % b
print('{} / {} = {} ... {}'.format(a , b , div, mod))
