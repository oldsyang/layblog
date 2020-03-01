from enum import Enum, IntEnum, EnumMeta


class IntEnumMixin(IntEnum):
    @classmethod
    def get_all_values(cls, not_in=None, join_items=None):
        if isinstance(not_in, (list, tuple)) and not_in:
            result = [each.value for each in cls.__members__.itervalues() if each.value not in not_in]
        else:
            result = [each.value for each in cls.__members__.itervalues()]
        if join_items and isinstance(join_items, list):
            result += join_items
        return result

    @classmethod
    def get_all_keys(cls):
        return cls.__members__.keys()

    @classmethod
    def get_all_values_string_format(cls, join_word=',', not_in=None, join_items=None):
        return join_word.join(map(str, cls.get_all_values(not_in, join_items)))

    @classmethod
    def get_name_by_value(cls, value):
        if isinstance(cls, EnumMeta):
            for k, v in cls.__members__.items():
                if isinstance(v, (tuple, list, dict)):
                    if value in v:
                        return k
                else:
                    if v == value:
                        return k


class ArticleFormat(IntEnumMixin):
    html = 1  # 富文本
    markdown = 2  # Markdown
    text = 3  # 字符串


class ArticleStatus(IntEnumMixin):
    default = 1  # 草稿
    publish = 2  # 发布
