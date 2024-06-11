# 連長圧縮(Run Length Encoding)を行う関数を提供するモジュール
# encode: 連長圧縮を行う
# decode: 連長圧縮を解く
# encode_to_string: 連長圧縮を行い、文字列に変換する
# 例:
# RLE =  RunLengthEncoding()
# RLE.encode("aaabbbcc") -> [('a', 3), ('b', 3), ('c', 2)]
# RLE.decode([('a', 3), ('b', 3), ('c', 2)]) -> "aaabbbcc"
# RLE.encode_to_string("aaabbbcc") -> "a3b3c2"


class RunLengthEncoding:
    def encode(self, s):
        # 連長圧縮を行う
        return [(k, v) for k, v in self._groupby(s)]

    @staticmethod
    def decode(lst):
        # 連長圧縮を解く
        return "".join(c * n for c, n in lst)

    def encode_to_string(self, s):
        # 連長圧縮を行い、文字列に変換する
        return "".join(str(k) + str(v) for k, v in self._groupby(s))

    @staticmethod
    def _groupby(s):
        temp = [s[0], 1]
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                temp[-1] += 1
            else:
                yield temp
                temp = [s[i], 1]
        yield temp
