class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = list()
        for index in range(1, n+1):
            str_element = ""
            
            if index%3 == 0:
                str_element += "Fizz"
                
            if index%5 == 0:
                str_element += "Buzz"
            
            if len(str_element) == 0:
                str_element += str(index)
            
            answer.append(str_element)
            
        return answer