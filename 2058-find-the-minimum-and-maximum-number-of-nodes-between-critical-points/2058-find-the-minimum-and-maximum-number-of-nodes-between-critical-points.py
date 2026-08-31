class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        
        prev = head
        curr = head.next
        position = 2
        
        first_critical = -1
        prev_critical = -1
        
        min_distance = float('inf')
        
        while curr and curr.next:
            
            # Check if current node is a critical point
            is_maxima = (
                curr.val > prev.val and 
                curr.val > curr.next.val
            )
            
            is_minima = (
                curr.val < prev.val and 
                curr.val < curr.next.val
            )
            
            if is_maxima or is_minima:
                
                # First critical point
                if first_critical == -1:
                    first_critical = position
                
                # Not the first critical point
                else:
                    min_distance = min(
                        min_distance,
                        position - prev_critical
                    )
                
                # Update latest critical point
                prev_critical = position
            
            # Move pointers forward
            prev = curr
            curr = curr.next
            position += 1
        
        # Less than two critical points
        if min_distance == float('inf'):
            return [-1, -1]
        
        max_distance = prev_critical - first_critical
        
        return [min_distance, max_distance]