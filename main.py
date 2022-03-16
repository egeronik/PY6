# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main(data):
    ans = {1969: {1988: {1963: 0,
                         1986: {'BRO': 1,
                                'XSLT': 2,
                                'DIFF': 3},
                         1962: 4},
                  1979: 5,
                  1958: 6},
           1990: 7,
           1974: {'REXX': {1988: {1963: 8,
                                  1986: 9,
                                  1962: 10},
                           1979: 11,
                           1958: 12},
                  'LESS': 13,
                  'CUDA': 14}}
    i = len(data) - 1
    while isinstance(ans[data[i]], dict):
        ans = ans[data[i]].copy()
        i -= 1

    return ans[data[i]]


if __name__ == '__main__':
    print(main([1962, 1958, 'DIFF', 'LESS', 1969]))
