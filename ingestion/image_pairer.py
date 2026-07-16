def pair_images(images):
    """
    Pair images sequentially.

    1,2
    3,4
    5,6

    Returns

    [
        (front, back),
        ...
    ]
    """

    pairs = []

    for i in range(0, len(images), 2):

        if i + 1 >= len(images):
            break

        pairs.append(
            (
                images[i],
                images[i + 1],
            )
        )

    return pairs