def ft_filter(function, iterable):
    """Filter elements from iterable based on function.
    
    Args:
        function: A function that returns True or False (can be None)
        iterable: Any iterable collection (list, tuple, etc.)
    
    Returns:
        A list containing items from iterable where function(item) is True.
        If function is None, returns items that evaluate to True.
    """
    if function is not None:
        return [item for item in iterable if function(item)]
    else:
        return [item for item in iterable if item]
    


