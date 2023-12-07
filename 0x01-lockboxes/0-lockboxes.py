#!/urs/bin/python3
"""
This module is for function to onlock
"""


def can_unlock_all(boxes):
    """
    Determine if all boxes can be opened.

    Args:
        boxes (list of lists): Each box contains keys
        represented by positive integers.
                    The first box (boxes[0]) is unlocked.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """

    # Initialize a set to keep track of the boxes that can be opened
    unlocked_boxes = {0}

    # Iterate through the unlocked boxes and find new keys
    for box in unlocked_boxes:
        for key in boxes[box]:
            # Check if the key is within the valid
            # range and the box is not already unlocked
            if 0 <= key < len(boxes) and key not in unlocked_boxes:
                unlocked_boxes.add(key)

    # Check if all boxes can be opened
    return len(unlocked_boxes) == len(boxes)
