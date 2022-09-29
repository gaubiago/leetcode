class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        
        # count how many valid zeros will be duplicated
        zero_count = 0
        # how long the array would be if added the valid zero duplicates
        resulting_arr_length = 0 
        # size of the input/output array
        arr_length = len(arr)
        # tells whether there is a zero at the edge
        edge_zero = False
    
        # loop through the whole array
        for num in arr:
            resulting_arr_length += 1
            
            # find out how many valid zeros will be duplicated
            # lower than secures one slot for the last zero's duplicate
            if num == 0 and resulting_arr_length < arr_length:    
                zero_count += 1
                resulting_arr_length += 1
                continue
            
            # edge case: register when 0 shows up at the cut-off slot 
            if num == 0 and resulting_arr_length == arr_length:
                edge_zero = True
            
        # size of the array saving the slots for the valid zero duplicates
        discounted_size = arr_length - zero_count
        
        # in-place operation indices
        i = arr_length - 1    # destination slot
        j = discounted_size - 1    # source slot
        
        while i >= 0:
            # keep last element the same, even if it is a 0 (zero)
            if i == arr_length - 1 and edge_zero:
                arr[i] = arr[j]
            # handle zero duplicates
            elif arr[j] == 0:
                arr[i] = arr[j]
                i -= 1
                arr[i] = 0
            # straight copy
            else:
                arr[i] = arr[j]
            # update indices
            i -= 1
            j -= 1