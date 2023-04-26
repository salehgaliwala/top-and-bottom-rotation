def minDominoRotations(top, bottom):
    # check if it's possible to make all values in top or bottom the same
    if all(x == top[0] for x in top) or all(x == bottom[0] for x in bottom):
        # count the number of rotations needed to make all values in the top half the same
        rotations_top = sum(x != top[0] for x in top)
        # count the number of rotations needed to make all values in the bottom half the same
        rotations_bottom = sum(x != bottom[0] for x in bottom)
        # return the minimum of the two
        return min(rotations_top, rotations_bottom)
    else:
        return -1
