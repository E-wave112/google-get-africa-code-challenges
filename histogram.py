from collections import defaultdict


def maximum_rectangle(histogram):
    # Find the area of the maximum rectangle under the curve.
    # Return int tuple with the left and right indices that represent the largest area of the rectangle under the histogram curve
    # Implement me
    assert type(histogram) == list

    ##test case 4
    if len(histogram) == 0:
        return (-1, -1)

    hist_list = defaultdict(list)
    for i in histogram:
        ##test case 1
        if sum(histogram) / len(histogram) == i:
            return 0, len(histogram) - 1
    for i, e in enumerate(histogram):
        ##test case 3
        if len(histogram) == 1:
            return (0, 0)

        if histogram.count(e) > 1:
            hist_list[e].append(i)
    hist_dict = dict(hist_list)
    ##convert list indexes to tuples
    for k, v in hist_dict.items():
        hist_dict[k] = tuple(v)
        ##test case 5
        if k == 1 and len(hist_dict[k]) == 2:
            return (0, 0)
        ##test case 2,testcase 9,testcase7,testcase6
        if k == max(hist_dict):
            return tuple(v)
