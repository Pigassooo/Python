import argparse

# 创建解析器
parser = argparse.ArgumentParser(description='这是一个示例程序.')

# 添加一个命令行参数
parser.add_argument('echo', help='回显提供的值')

# 执行解析命令行
args = parser.parse_args()

# 使用命令行参数（在这个例子中，打印出来）
print(args.echo)
