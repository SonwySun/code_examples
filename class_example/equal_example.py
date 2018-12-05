class Source(object):
    def __init__(self, source_type: str, create_time: str):
        """
        节点的数据来源类
        :param source_type: setting中定义的数据类型常量
        :param create_time: "%Y-%m-%d %H:%M:%S" 例："2018-11-22 10:00:00"
        """
        self.source_type = source_type
        self.create_time = create_time

    def __eq__(self, other):
        if isinstance(other, Source):
            is_same = True
            is_same = False if self.source_type != other.source_type else is_same
            is_same = False if self.create_time != other.create_time else is_same
            return is_same
        return False


class TaobaoSource(Source):
    def __init__(self, create_time, address: str):
        super().__init__('TAOBAO', create_time)
        self.address = address

    def __eq__(self, other):
        if isinstance(other, TaobaoSource):
            is_same = True
            is_same = False if self.source_type != other.source_type else is_same
            is_same = False if self.create_time != other.create_time else is_same
            is_same = False if self.address != other.address else is_same
            return is_same
        return False


n1 = Source('t', '2018')
n2 = Source('t', '2018')

# print('n1 == n2',n1 == n2)
# print('n1 != n2',n1 != n2)


n3 = TaobaoSource('2018', 'CHINA')
n4 = TaobaoSource('2018', 'CHINA')

print('n1 == n3', n1 == n3)
print('n3 == n1', n3 == n1)
print('n1 != n3', n1 != n3)
print('n3 != n1', n3 != n1)

print('n3 == n4', n3 == n4)
print('n3 != n4', n3 != n4)

# class to dict
print(vars(n1))
print(vars(n2))
print(vars(n3))
print(vars(n4))
